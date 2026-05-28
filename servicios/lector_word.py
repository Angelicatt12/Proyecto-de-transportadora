from docx import Document

def leer_documento():
    
    nombre_archivo = input(
        "Ingrese el nombre del archivo Word (con extensión .docx): "
    )
    documento = Document(
        f"documentos/{nombre_archivo}"
    )
        
    datos = {}
    
    for parrafo in documento.paragraphs:
        
        texto = parrafo.text
        
        if "Número de orden:" in texto:
            datos["numero"] = texto.split(":")[1].strip()
        
        if "Fecha:" in texto:
            datos["fecha"] = texto.split(":")[1].strip()
        
        if "Cliente:" in texto:
            datos["cliente"] = texto.split(":")[1].strip()
            
        if "Ciudad de origen:" in texto:
            datos["ciudad_origen"] = texto.split(":")[1].strip()
            
        if "Dirección de origen:" in texto:
            datos["direccion_origen"] = texto.split(":")[1].strip()
            
        if "Ciudad destino:" in texto:
            datos["ciudad_destino"] = texto.split(":")[1].strip()
            
        if "Dirección de destino:" in texto:
            datos["direccion_destino"] = texto.split(":")[1].strip()
            
        if "Peso total (kg):" in texto:
            datos["peso_total"] = texto.split(":")[1].strip()
            
        if "Cantidad de paquetes:" in texto:
            datos["cantidad_paquetes"] = texto.split(":")[1].strip()
            
        if "Tiempo máximo de entrega (días):" in texto:
            datos["tiempo_entrega"] = texto.split(":")[1].strip()
            
    return datos