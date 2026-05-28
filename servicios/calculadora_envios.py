def calcular_costo(transportadora, orden):
    
    costo = (
        transportadora.costo_base +
        (transportadora.costo_por_kg * int(orden.peso))
    )
    
    return costo