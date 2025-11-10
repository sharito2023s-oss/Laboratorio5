import random

opciones = ["Piedra", "Papel", "Tijera"]

def estrategia_optima():
    # En equilibrio racional, las tres tienen igual probabilidad
    jugada = random.choice(opciones)
    return jugada

def jugar_ronda():
    jugador = estrategia_optima()
    oponente = estrategia_optima()  # El oponente también es racional
    print(f"Tú: {jugador}  |  Oponente: {oponente}")

    if jugador == oponente:
        print("🤝 Empate\n")
    elif (jugador == "Piedra" and oponente == "Tijera") or \
         (jugador == "Papel" and oponente == "Piedra") or \
         (jugador == "Tijera" and oponente == "Papel"):
        print("🏆 Ganaste\n")
    else:
        print("❌ Perdiste\n")

# Simulamos 5 rondas
for _ in range(5):
    jugar_ronda()
