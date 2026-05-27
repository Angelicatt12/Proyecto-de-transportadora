def generador_reporte(
    orden,
    transportadora,
    costo,
    dias
):
    with open(
        "reporte_despacho.txt",
        "w",
        encoding="utf-8"
    ) as archivo:
        
        archivo.write(
            "======== REPORTE DE DESPACHO ========\n\n"
        )
        
        archivo.write(
            f"Cliente: {orden.cliente}\n"
        )
        
        archivo.write(
            f"Origen: {orden.origen}\n"
        )
        
        archivo.write(
            f"Destino: {orden.destino}\n"
        )
        
        archivo.write(
            f"Transportadora elegida: {transportadora}\n"
        )
        
        archivo.write(
            f"Costo: ${costo:,} COP\n"
        )
        
        archivo.write(
            f"Tiempo estimado: {dias} días\n"
        )
        
        archivo.write(
            "Estado del despacho: En proceso\n"
        )
        
        archivo.write(
            "\n====================================="
        )
        
    print(
        "\nReporte generado correctamente."
    )    