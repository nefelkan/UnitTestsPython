from unittest import result, runner
from funtotest import find_nb , get_sum, remove_element , capitalize_string_with_a_twist , Car
import unittest

class TestCubeMethods(unittest.TestCase):

    def test_case_find_nb1(self):
        self.assertEqual(find_nb(4183059834009) , 2022)

    def test_case_find_nb2(self):
        self.assertEqual(find_nb(24723578342962) , -1)

class TestSumMethods(unittest.TestCase):

    def test_case_get_sum1(self):
        self.assertEqual(get_sum(-1,2) , 2)

    def test_case_get_sum2(self):
        self.assertEqual(get_sum(4,-1) , 9)

class TestRemoveElementMethods(unittest.TestCase):

    def test_case_remove_element1(self):
        input = [4,2,3]
        expected_result2 = [4,2,3]
        result1 = remove_element(input)
        result2 = input        
        self.assertFalse(result1)
        self.assertEqual(expected_result2 , result2)

    def test_case_remove_element2(self):
        input = [5,2,3]
        expected_result2 = [2,3]
        result1 = remove_element(input)
        result2 = input
        self.assertTrue(result1)
        self.assertEqual(expected_result2 , result2)

class capitalize_string(unittest.TestCase):
    
    def capitalize_test_case1(self):
        input = "kamilopardali"
        expected_result1 = 13
        expected_result2 = "KAMILOPARDALI"
        result1 , result2= capitalize_string_with_a_twist(input)
        self.assertEqual(expected_result1 , result1)
        self.assertEqual(expected_result2 , result2)

    def capitalize_test_case2(self):
        input = "dog"
        expected_result1 = 3
        expected_result2 = "Dog"
        result1 , result2 = capitalize_string_with_a_twist(input)
        self.assertEqual(expected_result1 , result1)
        self.assertEqual(expected_result2 , result2)

    def capitalize_test_case3(self):
        input = "LAMPA"
        expected_result2 = "lampa"
        result1 , result2 = capitalize_string_with_a_twist(input)
        self.assertFalse(result1)
        self.assertEqual(expected_result2 , result2)

class CarConstructor(unittest.TestCase):

    def constructor_test_case1(self):
        input1 = 260
        input2 = 3000
        input3 = 4
        expected_result1 = 260
        expected_result2 = 3000
        expected_result3 = 4
        result = Car(input1,input2,input3)
        self.assertEqual(expected_result1 , result.top_speed)
        self.assertEqual(expected_result2 , result.weight)
        self.assertEqual(expected_result3 , result.num_wheels)

    def apply_breaks_test_case2(self):
        input1 = 540
        input2 = 2
        expected_result1 = 3
        expected_result2 = 86.6
        Toyota = Car(260,3000,4)
        Toyota.apply_breaks(input1 , input2)
        self.assertEqual(expected_result1 , Toyota.num_wheels)
        self.assertAlmostEqual(expected_result2 , Toyota.top_speed,0)


def cube_test_suite():
    cube_suite = unittest.TestSuite()
    cube_suite.addTest(TestCubeMethods('test_case_find_nb1'))
    cube_suite.addTest(TestCubeMethods('test_case_find_nb2'))
    return cube_suite

def sum_test_suite():
    sum_suite = unittest.TestSuite()
    sum_suite.addTest(TestSumMethods('test_case_get_sum1'))
    sum_suite.addTest(TestSumMethods('test_case_get_sum2'))
    return sum_suite

def remove_test_suite():
    remove_suite = unittest.TestSuite()
    remove_suite.addTest(TestRemoveElementMethods('test_case_remove_element1'))
    remove_suite.addTest(TestRemoveElementMethods('test_case_remove_element2'))
    return remove_suite

def capitalize_test_suite():
    capitalize_suite = unittest.TestSuite()
    capitalize_suite.addTest(capitalize_string('capitalize_test_case1'))
    capitalize_suite.addTest(capitalize_string('capitalize_test_case2'))
    capitalize_suite.addTest(capitalize_string('capitalize_test_case3'))
    return capitalize_suite

def car_test_suite():
    car_suite = unittest.TestSuite()
    car_suite.addTest(CarConstructor('constructor_test_case1'))
    car_suite.addTest(CarConstructor('apply_breaks_test_case2'))
    return car_suite


if __name__ == '__main__' :
    runner = unittest.TextTestRunner()
    runner.run(cube_test_suite())
    runner.run(sum_test_suite())
    runner.run(remove_test_suite())
    runner.run(capitalize_test_suite())
    runner.run(car_test_suite())