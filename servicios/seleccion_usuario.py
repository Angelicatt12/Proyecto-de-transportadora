def seleccionar_transportadora(costos, sugerida):
    
    print("\n¿Acepta la sugerencia?")
    print("1. Sí")
    print("2. No, quiero ver otras opciones")
    
    opcion = int(
        input("Ingrese una opción: ")
    )
    
    if opcion == 1:
        return sugerida
    
    nombres = list(costos.keys())
    
    for i, nombre in enumerate(nombres, start=1):
        
        costo = costos[nombre]["costo"]
        dias = costos[nombre]["dias"]
        
        print(
            f"{i}. {nombre}")
        print(
            f"   Costo: ${costo:,} COP")
        print(
            f"   Tiempo: {dias} días\n")
        
    seleccion = int(
        input("Ingrese una opción: ")
    )
    
    return nombres[seleccion - 1]    