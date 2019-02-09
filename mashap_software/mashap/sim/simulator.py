from palamut.models import ModelDefinition
from copy import deepcopy
from sim.bunch import Bunch
import re
from numpy import *
from numpy import array, zeros
from run_kut4 import integrate
from sim import graphics
import scipy
from sim import excelexporter
import numpy
from palamut.models import VariableRunData
import math

class Simulator(object):
    """
    Simulator object runs the simulation.
    Usage: configure Simulator object with the model object. This might be either ModelDef or ModelIns.
    """
    def __init__(self, model):
        self.model = model
        self.differentials = model.differentials
        self.excel = excelexporter.ExcelExporter(model)
        self.runkut_call_number = 0
        self.calls = []

    def is_time_included(self, t):
        return math.fmod(t, self.model.record_period) == 0

    def add_stock_data(self, stock_data, time_data):
        for step_no,t in enumerate(time_data):
            if not self.is_time_included(t): continue # todo: use filter/map on time_data and stock_data
            current_stocks = stock_data[step_no]
            for i,stock_name in enumerate(self.model.stock_names):
                self.store_variable_run_data(self.model.stock_map[stock_name], current_stocks[i], t)

    def store_variable_run_data(self, variable, value, time):
        vrd = VariableRunData()
        vrd.variable = variable
        vrd.game_instance = self.model.game_instance
        vrd.value = value
        vrd.time = self.model.game_instance.current_time + time
        vrd.save()

    def simulate(self):
        gi = self.model.game_instance
        (self.time, self.X) = integrate(self.dX_dt, 0.0, array(gi.init_values()),
                                        self.model.decision_period, self.model.time_step)
        current_stocks = list(self.X[-1,:])
        gi.store_current_stock_values(current_stocks)
        self.excel.add_stock_data(self.X, self.time)
        self.excel.write_csv()
        self.add_stock_data(self.X, self.time)
        return self.X

    def dX_dt(self, t, stock_var__):
        self.calls.append(t)
        for eqn in self.model.eqns_sorted:
            exec(eqn)
        results = [eval(diff) for diff in self.differentials]
        if self.runkut_call_number == 0 and self.is_time_included(t):
            var_names = set()
            for og in self.model.output_groups:
                for var in og.variables.all():
                    if var.name in var_names: continue
                    if var.is_stock: continue # eval doesn't work for stocks
                    var_names.add(var.name)
                    self.store_variable_run_data(var, eval(var.name), t)
        if self.runkut_call_number == 0 and self.excel.is_time_included(t): # store for F(x,y) only in runkut
            # add data to csv
            self.excel.add('time_',t)
            for key in self.model.levels:
                self.excel.add(key,eval(key))
#            for i,key in enumerate(self.model.stock_names):
#                self.excel.add(key,results[i])
        self.runkut_call_number = (self.runkut_call_number + 1) % 4 # mod 4 since runkut4 is used.
        return array( results )