import unittest
import main


class MyTestCase(unittest.TestCase):

    def test_init(self):
        c = main.CmdSubclass()
        c.do_init('0.5 2')
        c.floatSum = main.sum_dict(c.floatChange)
        actual = c.floatSum
        expected = 1.0
        self.assertEqual(actual, expected)

    def test_fast_init(self):
        c = main.CmdSubclass()
        c.do_fastinit('')
        actual = c.floatChange
        expected = {'20': 5, '10': 5, '5': 5, '2': 5, '1': 5, '0.50': 5,
                            '0.20': 5, '0.10': 5, '0.05': 5, '0.01': 5}
        self.assertDictEqual(actual, expected)

    def test_buy(self):
        c = main.CmdSubclass()
        c.do_fastinit('')
        c.do_buy('0.5')
        actual = c.currentCost
        expected = 0.5
        self.assertEqual(actual, expected)

    def test_deposit(self):
        c = main.CmdSubclass()
        c.do_fastinit('')
        c.do_buy('0.55')
        c.do_deposit('0.6')
        actual = c.changeDue['0.01']
        expected = 5
        self.assertEqual(actual, expected)

    def test_get_float(self):
        c = main.CmdSubclass()
        c.do_init('0.5 3')
        c.floatSum = main.sum_dict(c.floatChange)
        actual = c.do_getfloat('')
        expected = 'Total Float: ' + "£1.50"
        self.assertEqual(actual, expected)

    def test_get_change(self):
        c = main.CmdSubclass()
        c.do_fastinit('')
        c.do_buy('0.55')
        c.do_deposit('0.65')
        actual = c.do_getchange('')
        expected = 'Change due: ' + "£0.10"
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(buffer=True)
