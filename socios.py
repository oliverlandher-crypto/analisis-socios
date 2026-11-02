socios = [
    {"nombre": "  ana ", "edad": 34, "ahorro": 5000, "municipio": "jalpan"},
    {"nombre": "LUIS", "edad": 52, "ahorro": 12000, "municipio": " Landa "},
    {"nombre": "rosa", "edad": 28, "ahorro": 3000, "municipio": "JALPAN"},
    {"nombre": " pedro", "edad": 45, "ahorro": 8000, "municipio": "arroyo seco"},
    {"nombre": "Marta  ", "edad": 61, "ahorro": 15000, "municipio": "jalpan"},
]

def limpiar(texto):
    return texto.strip().title()

def ahorro_promedio(socios):
    total = 0 
    for socio in socios:
        total = total + socio["ahorro"]
    return total / len(socios)

def contar_altos(socios, limite):
    contador = 0 
    for socio in socios:
        if socio["ahorro"] > limite:
            contador = contador + 1
    return contador

print("Socios:")
for socio in socios:
    print(limpiar(socio["nombre"]), "-", limpiar(socio["municipio"]))
print("Ahorro promedio:", ahorro_promedio(socios))
print("Socios con más de 5000:", contar_altos(socios, 5000))
