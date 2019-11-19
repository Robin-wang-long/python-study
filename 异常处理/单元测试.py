from myStack import Stack
import unittest
class TestStack(unittest.TestCase):
    def setUp(self):
        self.fp=open('test_Stack_return.txt','a+')
    def tearDown(self):
        self.fp.close()
    def test_isEmpty(self):
        try:
            s=Stack()
            self.assertTrue(s.isEmpty())
            self.fp.write('isEmpty passed\n')
        except Exception as e:
            self.fp.write('isEmpty failed\n')
    def test_clear(self):
        try:
            s=Stack(5);
            for i in ['a','b','c']:
                s.push(i)
            s.clear()
            self.assertTrue(s.isEmpty())
            self.fp.write('clear passed\n')
        except Exception as e:
            self.fp.write('clear failed\n')
    def test_isFull(self):
        try:
            s=Stack(3)
            s.push(1)
            s.push(2)
            s.push(3)
            self.assertTrue(s.isFull())
            self.fp.write('isFull passed\n')
        except Exception as e:
            self.fp.write('isFull failed\n')
    def test_pushpop(self):
        try:
            s=Stack()
            s.push(3)
            self.assertEqual(s.pop(),3)
            s.push('a')
            self.assertEqual(s.pop(),'a')
            self.fp.write('push and pop passed\n')
        except Exception as e:
            self.fp.write('push or pop failed\n')
    def test_setSize(self):
        try:
            s=Stack(8)
            for i in range(s):
                s.push(i)
            self.assertTrue(s.isFull())
            s.setSize(9)
            s.push(8)
            self.assertTrue(s.isFull())
            self.assertEqual(s.pop(),8)
            s.setSize(4)
            self.assertEqual(s._size,9)
            self.fp.write('setSize passed\n')
        except Exception as e:
            self.fp.write('setSize failed\n')
if __name__=='__main__':
    unittest.main()
