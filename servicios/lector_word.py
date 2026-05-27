from docx import Document

def leer_documento():
    
    documento = Document("documentos/orden_001.docx")
    
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
            
        if "Ciudad destino:" in texto:
            datos["ciudad_destino"] = texto.split(":")[1].strip()
            
        if "Peso total (kg):" in texto:
            datos["peso_total"] = texto.split(":")[1].strip()
            
        if "Cantidad de paquetes:" in texto:
            datos["cantidad_paquetes"] = texto.split(":")[1].strip()
            
        if "Tiempo máximo de entrega (días):" in texto:
            datos["tiempo_entrega"] = texto.split(":")[1].strip()
            
    return datos