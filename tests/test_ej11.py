import pytest
from src.ej11_def import contar_numeros

def test_contar_numeros():
    assert contar_numeros(15) == "La suma de 1+2+3+4+5+6+7+8+9+10+11+12+13+14+15 es 120."
    assert contar_numeros(5) == "La suma de 1+2+3+4+5 es 15."
    assert contar_numeros(30) ==  "La suma de 1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20+21+22+23+24+25+26+27+28+29+30 es 465."

@pytest.mark.parametrize(
    "num, expected",
    [
        (15, "La suma de 1+2+3+4+5+6+7+8+9+10+11+12+13+14+15 es 120."),
        (5, "La suma de 1+2+3+4+5 es 15."),
        (30, "La suma de 1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20+21+22+23+24+25+26+27+28+29+30 es 465.")
    ]
)

def test_contar_numeros_params(num, expected):
    assert contar_numeros(num) == expected