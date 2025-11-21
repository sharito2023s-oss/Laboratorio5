# 🎮 Algoritmo para Piedra, Papel o Tijera - Equilibrio de Nash

## 📋 Descripción del Proyecto

Este proyecto implementa un algoritmo óptimo para el juego clásico de Piedra, Papel o Tijera, demostrando el concepto de equilibrio de Nash en teoría de juegos. El algoritmo adopta una estrategia mixta donde todas las jugadas tienen igual probabilidad.

## 🎯 Planteamiento del Problema

- Juego: Piedra, Papel o Tijera

- Jugadores: 2 (nuestro algoritmo vs oponente racional)

- Objetivo: Maximizar las ganancias a largo plazo

- Supuesto: Ambos jugadores son racionales y buscan optimizar su estrategia

## ⚙️ Algoritmo Voraz Implementado

### 🔄 Función Principal

```python
import random

opciones = ["Piedra", "Papel", "Tijera"]

def estrategia_optima():
    # En equilibrio racional, las tres tienen igual probabilidad
    jugada = random.choice(opciones)
    return jugada
```
## 🎯 Mecánica del Juego

```python

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

```

## 📊 Matriz de Pagos

### 🎲 Reglas del Juego

```python
Piedra 🪨 vs Tijera ✂️  → 🪨 Gana
Papel 📄 vs Piedra 🪨  → 📄 Gana  
Tijera ✂️ vs Papel 📄  → ✂️ Gana
Misma jugada → Empate 🤝

```

## 📈 Representación Matricial

```text
          Op: Piedra  Op: Papel  Op: Tijera
Yo: Piedra    Empate     Pierde      Gana
Yo: Papel      Gana      Empate     Pierde
Yo: Tijera    Pierde      Gana      Empate
```


## 🧠 Teoría de Juegos Aplicada

### ⚖️ Equilibrio de Nash

- Estrategia pura: No existe equilibrio (siempre hay contramedida)

- Estrategia mixta: Distribución uniforme 1/3 para cada opción

- Valor esperado: 0 (empate a largo plazo contra oponente racional)

## 📐 Fundamentos Matemáticos


```python
# Probabilidades óptimas
prob_piedra = 1/3
prob_papel = 1/3  
prob_tijera = 1/3

# Valor esperado del juego
valor_esperado = 0  # Juego justo
```

## 🎯 Estrategia del Algoritmo

### 🔀 Selección Aleatoria Uniforme

```python
def estrategia_optima():
    return random.choice(["Piedra", "Papel", "Tijera"])
    # Equivalente a: random.choices(opciones, weights=[1/3, 1/3, 1/3])
```

## ✅ Por qué es Óptima

- Impredecibilidad: El oponente no puede anticipar la jugada

- Explotación resistente: No hay patrones que el oponente pueda explotar

- Máximo mínimo: Maximiza el peor caso posible (principio minimax)


## 📊 Resultados Esperados

```python

Tú: Piedra  |  Oponente: Papel
❌ Perdiste

Tú: Tijera  |  Oponente: Papel  
🏆 Ganaste

Tú: Papel  |  Oponente: Papel
🤝 Empate

Tú: Papel  |  Oponente: Papel
🤝 Empate

Tú: Tijera  |  Oponente: Papel
🏆 Ganaste

```

## ⚡ Análisis Estadístico
### 📊 Distribución a Largo Plazo

- Ganancias: ≈ 33.3%

- Pérdidas: ≈ 33.3%

- Empates: ≈ 33.3%

- Valor esperado: 0 puntos por ronda

### 🎲 Ley de los Grandes Números

```python

# Después de muchas rondas:
ganancias ≈ 1/3
perdidas ≈ 1/3
empates ≈ 1/3
```

## 👥 Autores

#### 🧑‍💻 Contribuidores Principales

- **Carlos Andrés Suárez Torres** → [Carlos23Andres](https://github.com/Carlos23Andres)  

- **Saira Sharid Sanabria Muñoz** → [sharito202](https://github.com/sharito202)
