from .models import Categoria, Servicio

def load_data():
    # Crea categorías hardcodeadas
    CATEGORIAS_HARD_CODED = [
    "Afinación",
    "Frenos",
    "Suspensión",
    "Service",
    "Embrague",
    "Distribución",
    "Circuito Refrigerante",
    "Electricidad",
    "Motor",
    "Otros"
]
    for categoria_nombre in CATEGORIAS_HARD_CODED:
        Categoria.objects.get_or_create(nombre=categoria_nombre)


    SERVICIOS_HARD_CODED = {
    "Afinación": [
        "Puesta a punto",
        "Bujías",
        "Filtro de aire",
        "Filtro de nafta o gasoil",
        "Filtro de habitáculo",
        "Tapa de distribuidor",
        "Rotor",
        "Carburador",
        "Diafragma",
        "Regulación válvulas",
        "Caños de nafta",
        "Limpieza inyectores",
        "Sonda lambda",
        "Emisión de gases",
        "Potenciómetro",
        "Motor paso a paso",
        "M.A.P",
        "Bobina de encendido",
        "Caja electrónica",
        "Sensores",
        "Análisis por escáner"
    ],
    "Frenos": [
        "Pastillas del / Tras",
        "Discos del / Tras",
        "Cintas y Campanas",
        "Líquido",
        "Freno de Mano",
        "Bomba",
        "Cilindros",
        "Válvula Compensadora"
    ],
    "Suspensión": [
        "Alineación del / Tras",
        "Amortiguadores del / Tras",
        "Brazos Suspensión",
        "Rótulas",
        "Extremos Dirección",
        "Caja Dirección",
        "Rulemán Rueda"
    ],
    "Service": [
        "Aceite",
        "Filtro",
        "Aceite Caja",
        "Aceite Hidráulica"
    ],
    "Embrague": [
        "Embrague Completo",
        "Rulemán Empuje",
        "Retenes",
        "Engranajes",
        "Sincronizados",
        "Horquillas",
        "Desplazables"
    ],
    "Distribución": [
        "Correa de Distribución",
        "Correa de Alternador",
        "Correa de Aire Acondicionado",
        "Correa de Bomba de Agua",
        "Rulemán Tensor",
        "Retenes"
    ],
    "Circuito Refrigerante": [
        "Radiador",
        "Líquido Refrigerante",
        "Bomba de Agua",
        "Termostato",
        "Caños de agua",
        "Electroventilador"
    ],
    "Electricidad": [
        "Alternador",
        "Burro Arranque",
        "Batería",
        "Lámparas",
        "Cable Captor / Módulo"
    ],
    "Motor": [
        "Cilindros",
        "Válvulas",
        "Reparación de Tapa",
        "Aros",
        "Juntas",
        "Metales",
        "Bomba Aceite",
        "Árbol de Levas",
        "Pistones"
    ]
}
    for categoria_nombre, servicios in SERVICIOS_HARD_CODED.items():
        categoria, _ = Categoria.objects.get_or_create(nombre=categoria_nombre)
        for servicio_nombre in servicios:
            Servicio.objects.get_or_create(nombre=servicio_nombre, categoria=categoria)