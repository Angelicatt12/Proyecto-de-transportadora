class Orden:
    
    def __init__(
        self,
        numero,
        fecha,
        cliente,
        origen,
        destino,
        peso,
        paquetes,
        tiempo_entrega,
        observaciones
    ):
        self.numero = numero
        self.fecha = fecha
        self.cliente = cliente
        self.origen = origen
        self.destino = destino
        self.peso = peso
        self.paquetes = paquetes
        self.tiempo_entrega = tiempo_entrega
        self.observaciones = observaciones
        