def obtener_mejor_opcion(resultados, tiempo_maximo):
    
    opciones_validas = {}
    
    for nombre, datos in resultados.items():
        
        if datos["dias"] <= tiempo_maximo:
            opciones_validas[nombre] = datos
            
    mejor_transportadora = None
    menor_costo = float("inf")
    
    for nombre, datos in opciones_validas.items():
        
        costos = datos["costo"]
        
        if costos < menor_costo:
            
            menor_costo = costos
            
            mejor_transportadora = (
                nombre,
                costos,
                datos["dias"]
            )

    return mejor_transportadora
