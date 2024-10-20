import pytest
from src.ej04_def2 import grados_celsius

def test_num_mayor():
    assert grados_celsius(20.00) == 68.00
    assert grados_celsius(20.50) == 68.90
    assert grados_celsius(14.50) == 58.10

@pytest.mark.parametrize(
    "fahrenheit, expected",
    [
        (20.00, 68.00),
        (20.50, 68.90),
        (14.50, 58.10)
    ]
)

def test_grados_celsius_params(fahrenheit, expected):
    assert grados_celsius(fahrenheit) == expected