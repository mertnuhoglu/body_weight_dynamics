import unittest
from palamut import service

class ServiceTest(unittest.TestCase):
    def test(self):
        self.assertTrue(False)
        sim_manager = service.SimManager()
        mp = sim_manager.convert_vensim_file(open('test/test_vensim_01.mdl').read())
        model = sim_manager.build_model(mp)
        expected = {u'p': u'pi_g-gngp_o-pox_a-pox_s', u'c': u'ci_g+gngf_i+gngp_i-cox_a-dnl_o-cox_s',
                    u'at': u'atf', u'f': u'+fi_g-fox_a+dnl_i-gngf_o-fox_s'}
        self.assertEquals(model.stocks, expected)

if __name__ == "__main__":
    unittest.main()
