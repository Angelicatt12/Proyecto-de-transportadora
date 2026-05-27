from servicios.lector_word import leer_documento
from modelos.orden import Orden

datos = leer_documento()

orden = Orden(
    numero=datos["numero"],
    fecha=datos["fecha"],
    cliente=datos["cliente"],
    origen=datos["ciudad_origen"],
    destino=datos["ciudad_destino"],
    peso=datos["peso_total"],
    paquetes=datos["cantidad_paquetes"],
    tiempo_entrega=datos["tiempo_entrega"],
    observaciones=""
)

print(orden.cliente)
print(orden.origen)
print(orden.destino)
