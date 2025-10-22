# descuentos.py
def aplicar_descuento(precio, porcentaje):
    """Aplica un descuento al precio indicado."""
    if not isinstance(precio, (int, float)) or not isinstance(porcentaje, (int, float)):
        raise TypeError("Los valores deben ser numéricos")
    if precio < 0 or porcentaje < 0:
        raise ValueError("ingresar valores positivos!!")
    if porcentaje > 100:
        porcentaje = 100      
    return precio - (precio * porcentaje / 100)