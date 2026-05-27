from docx import Document

def leer_documento():
    
    documento = Document("documentos/orden_001.docx")
    
    for parrafo in documento.paragraphs:
        print(parrafo.text)