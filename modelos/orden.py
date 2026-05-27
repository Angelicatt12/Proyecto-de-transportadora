class Orden:
    
    def __init__(
        self,
        numero,
        fecha,
        cliente,
        origen,
        direccion_origen,
        destino,
        direccion_destino,
        peso,
        paquetes,
        tiempo_entrega,
        observaciones
    ):
        self.numero = numero
        self.fecha = fecha
        self.cliente = cliente
        self.origen = origen
        self.direccion_origen = direccion_origen
        self.destino = destino
        self.direccion_destino = direccion_destino
        self.peso = peso
        self.paquetes = paquetes
        self.tiempo_entrega = tiempo_entrega
        self.observaciones = observaciones
        