# test_descuentos.py
from descuentos import aplicar_descuento

def test_descuento_basico():
    assert aplicar_descuento(100, 10) == 90

def test_descuento_cero():
    assert aplicar_descuento(50, 0) == 50

def test_descuento_total():
    assert aplicar_descuento(200, 100) == 0

def test_valores_invalidos():
    import pytest
    with pytest.raises(ValueError):
        aplicar_descuento(-10, 100)
    with pytest.raises(TypeError):
        aplicar_descuento("LOLE", )    
