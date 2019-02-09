# t = tester.Tester()
# t.test_last_files()

from sim import graphics
from sim.simulator import Simulator
from sim.modelreader import ModelReader
import os
import re

class Tester(object):
    def __init__(self):
        pass

    def test_last_files(self):
        template = '%(name)s%(count)03d.%(ext)s'
        path = u'tester/'
        name = 'eqns_'
        (max_count, ext) = self.find_last_file(path, name)
        filename_eqns = os.path.join(path, template % {'name':name, 'count':int(max_count), 'ext':ext})
        name = 'stock_inits_'
        (max_count, ext) = self.find_last_file(path, name)
        filename_inits = os.path.join(path, template % {'name':name, 'count':int(max_count), 'ext':ext})
        name = 'eqns_stocks_'
        (max_count, ext) = self.find_last_file(path, name)
        filename_stock = os.path.join(path, template % {'name':name, 'count':int(max_count), 'ext':ext})
        self.test(filename_eqns, filename_stock, filename_inits)

    def test(self, file_eqns='eqns.txt', file_stocks='eqns_stocks.txt', file_inits='stock_inits.txt'):
        reader = ModelReader(file_eqns, file_stocks, file_inits)
        sim = Simulator(reader.model)
        X = sim.simulate()
        sim.draw_graph(self.next_filename(u'tester/'))
    
    def next_filename(self, path=u'tester/', name=''):
        (max_count, ext) = self.find_last_file(path, name)
        template = '%(name)s%(count)03d.%(ext)s'
        filename = template % {'name':name, 'count':int(max_count)+1, 'ext':ext}
        return os.path.join(path, filename)
        
    def find_last_file(self, path, name):
        files = os.listdir(path)
        p = re.compile(r'\b' + name + r'(?P<count>\d+)\.(?P<ext>\w+)\b')
        numbers = [0]
        ext = 'png'
        for file in files:
            m = p.search(file)
            if m:
                count, ext = m.group('count', 'ext')
                numbers.append(count)
        max_count = max(numbers)
        return (max_count, ext)