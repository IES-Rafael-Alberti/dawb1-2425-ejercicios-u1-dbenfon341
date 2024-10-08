import pytest
from src.prueba1 import num_mayor

def test_num_mayor():
    assert num_mayor(1, 1) == 0
    assert num_mayor(4, 2) == 4
    assert num_mayor(2, 30) == 30

@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        (1, 1, 0),
        (4, 2, 4),
        (2, 30, 30)
    ]
)

def test_num_mayor_params(input_x, input_y, expected):
    assert num_mayor(input_x, input_y) == expected