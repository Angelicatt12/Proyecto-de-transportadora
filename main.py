from servicios.lector_word import leer_documento
from modelos.orden import Orden
from modelos.transportadora import Transportadora
from servicios.comparador import obtener_mejor_opcion
from servicios.calculadora_envios import calcular_costo

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
    18000,
    3500,
    2
)

coordinadora = Transportadora(
    "Coordinadora",
    15000,
    3000,
    3
)

interrapidisimo = Transportadora(
    "Interrapidisimo",
    12000,
    2800,
    5
)

costos = {
    
    servientrega.nombre: {
        "costo": calcular_costo(
            servientrega,
            orden
        ),
        "dias": servientrega.dias_entrega
    },
    
    coordinadora.nombre: {
        "costo": calcular_costo(
            coordinadora,
            orden
        ),
        "dias": coordinadora.dias_entrega
    },
    
    interrapidisimo.nombre: {
        "costo": calcular_costo(
            interrapidisimo,
            orden
        ),
        "dias": interrapidisimo.dias_entrega
    }
}

nombre, costos, dias = obtener_mejor_opcion(
    costos,
    int(orden.tiempo_entrega)
)

print("\nTransportadora sugerida:")
print(nombre)

print("Costo:")
print(f"${costos:,} COP")

print("Tiempo estimado:")
print(dias, "días")

print(orden.cliente)
print(orden.origen)
print(orden.destino)
