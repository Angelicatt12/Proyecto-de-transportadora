
Sistema desarrollado en Python para automatizar el proceso de selección de transportadoras mediante lectura de órdenes de venta, cálculo de costos y generación de reportes logísticos.

---

# Descripción del proyecto

El sistema permite leer automáticamente una orden de venta en formato Word, extraer la información del envío y calcular la mejor opción de transportadora según:

- Costos de envío
- Tiempo máximo de entrega
- Acuerdos comerciales locales

Además, el usuario puede aceptar la sugerencia automática o seleccionar manualmente otra transportadora.

Finalmente, el sistema genera un reporte del despacho y almacena un historial de reportes generados.

---

# Flujo del sistema

<img width="2708" height="1814" alt="image" src="https://github.com/user-attachments/assets/9fe2a8c9-6f68-4ab4-a7de-ba4fdff3b8db" />

# Funcionalidades implementadas

- Lectura automática de órdenes desde Word
- Extracción de datos logísticos
- Creación de objetos mediante Programación Orientada a Objetos
- Cálculo automático de costos de envío
- Comparación inteligente de transportadoras
- Restricción por tiempo máximo de entrega
- Selección automática y manual de transportadora
- Generación automática de reportes
- Historial persistente de despachos

---

# Estructura del proyecto

```text
Proyecto-de-transportadora/
│
├── documentos/
│
├── modelos/
│   ├── orden.py
│   └── transportadora.py
│
├── servicios/
│   ├── lector_word.py
│   ├── calculadora_envios.py
│   ├── comparador.py
│   ├── seleccion_usuario.py
│   └── generador_reporte.py
│
├── reportes/
│
├── main.py
│
└── README.md
```

---

# Tecnologías utilizadas

- Python
- Programación Orientada a Objetos (POO)
- Archivos TXT
- python-docx
- Git y GitHub

---

# Ejemplo de funcionamiento

```text
Transportadora sugerida:
Coordinadora

Costo:
$51,000 COP

Tiempo estimado:
3 días
```

---

# Historial de reportes

El sistema almacena automáticamente los reportes generados dentro de la carpeta:

```text
reportes/
```

Cada despacho queda registrado como:

```text
reporte_001.txt
reporte_002.txt
reporte_003.txt
```

Esto permite mantener un historial persistente de operaciones, simulando una base de datos básica mediante archivos.

---

# Posibles mejoras futuras

- Integración con APIs reales de transportadoras
- Dashboard logístico
- Predicción de tiempos de entrega
- Análisis de datos históricos
- Implementación de Machine Learning
- Base de datos SQL

---

# Autor

Proyecto desarrollado por:

**Angelica Torres**

---

# Estado del proyecto

- Proyecto funcional
- Flujo completo implementado
- Persistencia de reportes
- Mejoras futuras en análisis y visualización
