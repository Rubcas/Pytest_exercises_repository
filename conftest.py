#conftest file used to define fixtures, can be used for other files. 

import pytest

@pytest.fixture
def input_value():
    input = 10
    return input


