from palamut.models import ModelDefinition
from palamut.models import Variable
from palamut.models import ModelPython
from sim.bunch import Bunch

def build_model_from_files(file_eqns='eqns.txt', file_stocks='eqns_stocks.txt', file_inits='stock_inits.txt'):
    eqns_readable = open(file_eqns)
    eqns_stocks = open(file_stocks)
    eqns_inits = open(file_inits)
    model_python = ModelPython(eqns=eqns_readable,eqns_stocks=eqns_stocks,stock_inits=eqns_inits)
    model_python.save()
# todo: burada mappings_in verileri de gonderilmeli:
    return build_model_from_model_python(model_python)
    
def build_model_from_model_python(model_python, mappings_in):
    return ModelReader(model_python, mappings_in).model
    
class ModelReader(object):
    def __init__(self, model_python, mappings_bunch):
        self.model = self.read_file(model_python, mappings_bunch)

    def read_file(self, model_python, mappings_bunch):
        model_ = ModelDefinition()
        model_.model_python = model_python
        model_.save()
        variables_str = self.build_variables(model_python.eqns.splitlines()) # {var_name: formula}
        variables_str['time_step'] = '0.5'
        stocks_str = dict([tuple([s.strip() for s in line.strip().split('=',1)]) # {stock_name: formula}
                          for line in model_python.eqns_stocks.splitlines()])
        stock_inits = dict([tuple([s.strip() for s in line.strip().split('=',1)]) # {stock_name: init_value}
                          for line in model_python.stock_inits.splitlines()])
        variables = []
        var_mappings = mappings_bunch.var_mappings
        stock_mappings = mappings_bunch.stock_mappings
        var_mappings['time_step'] = Bunch(name='time_step', formula='0.5', unit='', description='')
        for item in variables_str.items():
            var_name = item[0]
            bunch = var_mappings[var_name]
            var = Variable(name=var_name, formula=item[1], model=model_, unit=bunch.unit, description=bunch.description)
            var.save()
            variables.append(var)
        stocks = []
        for item in stocks_str.items():
            init_value_ = stock_inits[item[0]]
            stock_name=item[0]
            bunch = stock_mappings[stock_name]
            stock = Variable(name=stock_name, formula=item[1], model=model_, init_value=init_value_, is_stock = True,
                    unit=bunch.unit, description=bunch.description)
            stock.save()
            stocks.append(stock)
        return model_

    def build_variables(self, eqns_readable):
        variables = {}
        is_exogeneous_input_variable = lambda line: line.find('=') == -1
        for line in eqns_readable:
            if is_exogeneous_input_variable(line):
                variables[line.strip()] = '0.0'    # make formula empty
            else:
                variables.update([tuple([s.strip() for s in line.strip().split('=',1)])])
        return variables