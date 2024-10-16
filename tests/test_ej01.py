import pytest
from src.ej01_def import saludo

def test_saludo():
    assert saludo("david") == "Hola, david."
    assert saludo("diego") == "Hola, diego."
    assert saludo("lucia") == "Hola, lucia."

@pytest.mark.parametrize(
    "input, expected",
    [
        ("david", "Hola, david."),
        ("diego", "Hola, diego."),
        ("lucia", "Hola, lucia.")
    ]
)

def test_saludo_params(input, expected):
    assert saludo(input) == expected