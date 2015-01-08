from item import RedisList
import unittest

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.list = RedisList('testing')
        self.list.append('rak', 'cassie', 'chuyu', 'kai')
        self.list.unshift('armen', 'greg')

    def tearDown(self):
        self.list = RedisList('testing')
        self.list.clear()

    def test_creation(self):
        self.assertEqual(self.list[:], ['greg', 'armen', 'rak', 'cassie', 'chuyu', 'kai'])

    def test_get_item(self):
        self.assertEqual(self.list[0], 'greg')
        self.assertEqual(self.list[-1], 'kai')
        self.assertEqual(self.list[1:2], ['armen'])
        self.assertEqual(self.list[3:6], ['cassie', 'chuyu', 'kai'])
        self.assertTrue('kai' in self.list)
        self.assertFalse('richard' in self.list)

    def test_set_item_int(self):
        self.list[0] = 'patrick duffy'
        self.assertEqual(self.list[0:], ['patrick duffy', 'armen', 'rak', 'cassie', 'chuyu', 'kai'])
        with self.assertRaises(IndexError):
            self.list[10] = 'billy'

    def test_set_item_slice(self):
        self.list[0:2] = 'patrick duffy', 'tom selleck'
        self.assertEqual(self.list[:], ['patrick duffy', 'tom selleck', 'rak', 'cassie', 'chuyu', 'kai'])
        self.list[0:1] = ['warren beatty']
        self.assertEqual(self.list[:], ['warren beatty', 'tom selleck', 'rak', 'cassie', 'chuyu', 'kai'])
        with self.assertRaises(TypeError):
            self.list[0:1] = "walker texas ranger"
            self.list[0:] = ['greg', 'armen']

    def test_len(self):
        self.assertEqual(len(self.list), 6)

    def test_sort(self):
        self.assertEqual(self.list.sort(), ['armen', 'cassie', 'chuyu', 'greg', 'kai', 'rak'])

    def test_pop(self):
        self.assertEqual(self.list.pop(), 'kai')
        self.assertEqual(self.list[:], ['greg', 'armen', 'rak', 'cassie', 'chuyu'])

if __name__ == '__main__':
    unittest.main()
