# This test file uses the test fixture function of input_value from the conftest file. 

def func_retval():
    some_int = 10
    return some_int

def test_func_retval(input_value):
    assert func_retval() == input_value
