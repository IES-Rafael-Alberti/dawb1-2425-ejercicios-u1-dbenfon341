import pytest
from src.ej05_def2 import calcular_precio

def test_calcular_precio():
    assert calcular_precio(20, 10) == "El precio final del artículo con IVA (10) es 22.00 €"
    assert calcular_precio(55, 101) == "El precio final del artículo con IVA (21) es 66.55 €"
    assert calcular_precio(65, -1) == "El precio final del artículo con IVA (21) es 78.65 €"

@pytest.mark.parametrize(
    "importe, iva, expected",
    [
        (20, 10, "El precio final del artículo con IVA (10) es 22.00 €"),
        (55, 101, "El precio final del artículo con IVA (21) es 66.55 €"),
        (65, -1, "El precio final del artículo con IVA (21) es 78.65 €")
    ]
)

def test_calcular_precio_params(importe, iva, expected):
    assert calcular_precio(importe, iva) == expected