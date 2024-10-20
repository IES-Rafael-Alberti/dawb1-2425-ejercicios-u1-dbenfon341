import pytest
from src.ej02_def import calcular_horas

def test_calcular_horas():
    assert calcular_horas(5, 20) == 100
    assert calcular_horas(20, 10) == 200
    assert calcular_horas(44, 12) == 528

@pytest.mark.parametrize(
    "horas, precio_hora, expected",
    [
        (5, 20, 100),
        (20, 10, 200),
        (44, 12, 528)
    ]
)

def test_calcular_horas_params(horas, precio_hora, expected):
    assert calcular_horas(horas, precio_hora) == expected