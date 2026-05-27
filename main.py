from servicios.lector_word import leer_documento
from modelos.orden import Orden
from modelos.transportadora import Transportadora

datos = leer_documento()

orden = Orden(
    numero=datos["numero"],
    fecha=datos["fecha"],
    cliente=datos["cliente"],
    origen=datos["ciudad_origen"],
    direccion_origen=datos["direccion_origen"],
    destino=datos["ciudad_destino"],
    direccion_destino=datos["direccion_destino"],
    peso=datos["peso_total"],
    paquetes=datos["cantidad_paquetes"],
    tiempo_entrega=datos["tiempo_entrega"],
    observaciones=""
)

servientrega = Transportadora(
    "Servientrega",
    5000,
    1000
)

coordinadora = Transportadora(
    "Coordinadora",
    4000,
    1200
)

interrapidisimo = Transportadora(
    "Interrapidisimo",
    6000,
    800
)

print(orden.cliente)
print(orden.origen)
print(orden.destino)
