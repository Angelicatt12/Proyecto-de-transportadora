class Transportadora:
    
    def __init__(
        self,
        nombre,
        costo_base,
        costo_por_kg,
        dias_entrega
    ):
        self.nombre = nombre
        self.costo_base = costo_base
        self.costo_por_kg = costo_por_kg
        self.dias_entrega = dias_entrega