from mylist import MyList
import unittest
import sys
from contextlib import contextmanager
from io import StringIO


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class Testing(unittest.TestCase):
    def test_append_to_empty(self):
        list_ = MyList()
        list_.append(1)
        with captured_output() as (out, err):
            list_.print()
        output = out.getvalue().strip()
        self.assertEqual(output, '1') 
       
    def test_append_another_node(self):
        list_ = MyList(1)
        list_.append(2)
        with captured_output() as (out, err):
            list_.print()
        output = out.getvalue().strip()
        self.assertEqual(output, '1 2')

    def test_append_one_node_list(self):
        list1 = MyList(1)
        list2 = MyList(2)
        list3 = list1 + list2 
        with captured_output() as (out, err):
            list3.print()
        output = out.getvalue().strip()
        self.assertEqual(output, '1 2')

    def test_append_two_node_list(self):
        list1 = MyList(1,2)
        list2 = MyList(3,4)
        list3 = list1 + list2 
        with captured_output() as (out, err):
            list3.print()
        output = out.getvalue().strip()
        self.assertEqual(output, '1 2 3 4')

    def test_print_reversed(self):
        list1 = MyList(1,2,3,4)
        with captured_output() as (out, err):
            list1.print_reversed()
        output = out.getvalue().strip()
        self.assertEqual(output, '4 3 2 1')

if __name__ == '__main__':
    unittest.main()

