from redisdict import RedisDict
import unittest

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.testdict = RedisDict('dict_testing', zip(['caffeine', 'fridays'],['necessary', 'fun']), beer = "mothersmilk")
        self.testdict.update({'coffee': 'good', 'redbull':'better'})

    def tearDown(self):
        self.testdict = RedisDict('dict_testing')
        self.testdict.clear()

    def test_creation(self):
        self.assertEqual(dict(self.testdict), {'coffee': 'good', 'redbull':'better', 'beer': 'mothersmilk', 'caffeine': 'necessary', 'fridays':'fun'})

    def test_get_item(self):
        self.assertEqual(self.testdict['coffee'], 'good')
        with self.assertRaises(KeyError):
            self.testdict['greg']
        ##test .get

    def test_contains(self):
        self.assertTrue('beer' in self.testdict)
        self.assertFalse('milk' in self.testdict)

    def test_set_item(self):
        self.testdict['champagne'] = 'ideal'
        self.testdict['coffee'] = 'latte'
        self.assertEqual(self.testdict['champagne'], 'ideal')
        self.assertEqual(self.testdict['coffee'], 'latte')

    def test_len(self):
        self.assertEqual(len(self.testdict), 5)

    def test_views(self):
        self.assertEqual(list(dict(self.testdict).items()), self.testdict.items())
        self.assertEqual(list(dict(self.testdict).keys()).sort(), self.testdict.keys().sort())
        self.assertEqual(list(dict(self.testdict).values()).sort(), self.testdict.values().sort())

    def test_pop(self):
        pass

    def test_update(self):
        pass

if __name__ == '__main__':
    unittest.main()
