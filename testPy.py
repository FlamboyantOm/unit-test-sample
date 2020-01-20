import unittest


#exception rise function
def raises_error(*args, **kwds):
    raise ValueError('Invalid value: %s%s' % (args, kwds))



class SimplisticTest(unittest.TestCase):

    def test_assert_true(self):
        self.assertTrue(True)
        a,b = 1,2
        self.assertTrue((a == b), str(a)+' is not equal to '+str(b))

    def test_assert_false(self):
      self.assertFalse(False)

    def test_not_equal(self):
      self.assertNotEqual(1, 3 - 2)

    def test_equal(self):
      self.assertEqual(2, 3 - 2)

    def test_trap_locally(self):
        try:
            raises_error('a', "{a='1',b='2'}")
        except ValueError:
            pass
        else:
            self.fail('Did not see ValueError')

    def test_assert_raises(self):
        self.assertRaises(ValueError, raises_error, 'a', b='c')



# fixture Test function
class FixturesTest(unittest.TestCase):

    def setUp(self):
        print('In setUp()')
        self.fixture = range(1, 10)

    def tearDown(self):
        print('In tearDown()')
        del self.fixture

    def test(self):
        print('In test()')
        self.assertEqual(self.fixture, range(1, 10))


# runtime error function
class OutcomesTest(unittest.TestCase):

    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)

    def test_error(self):
        raise RuntimeError('Test error!')



if __name__ == '__main__':
    unittest.main()
