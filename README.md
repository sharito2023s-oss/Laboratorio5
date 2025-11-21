# 🧠 Laboratorio 5: Algoritmos Voraces y Teoría de Juegos

## 📋 Descripción del Proyecto

Este laboratorio explora tres problemas fundamentales en inteligencia artificial y optimización, demostrando diferentes enfoques algorítmicos para resolver problemas de toma de decisiones. Cada punto aborda un escenario específico donde las estrategias "locales" pueden o no conducir a soluciones globalmente óptimas.

## 🎯 Puntos del Laboratorio

#### 1. 🪑 Organización de Sillas con Hill Climbing
#### 2. 💰 Problema del Cambio de Monedas con Algoritmo Voraz
#### 3. 🎮 Piedra, Papel o Tijera con Equilibrio de Nash

## 🪑 Punto 1: Organización de Sillas con Hill Climbing

### 📋 Descripción

Optimización de la disposición de 6 personas en sillas circulares maximizando la satisfacción total mediante el algoritmo Hill Climbing.

#### 🎯 Objetivo

Visualizar cómo pequeñas modificaciones locales pueden mejorar una solución mediante búsqueda iterativa.

### ⚙️ Implementación

```python

import random

# Matriz de satisfacción entre personas
satisfaction = [[0, 5, -2, 3, 1, 4],
                [5, 0, 3, -1, 2, 2],
                [-2, 3, 0, 4, -3, 5],
                [3, -1, 4, 0, 2, 1],
                [1, 2, -3, 2, 0, 4],
                [4, 2, 5, 1, 4, 0]]

def hill_climbing():
    current = list(range(6))
    random.shuffle(current)
    current_value = total_satisfaction(current)
    
    for _ in range(1000):
        i, j = random.sample(range(6), 2)
        neighbor = current[:]
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
        neighbor_value = total_satisfaction(neighbor)
        if neighbor_value > current_value:
            current, current_value = neighbor, neighbor_value
    return current, current_value


```

### 📊 Características

- Enfoque: Búsqueda local con mejoras incrementales

- Espacio de búsqueda: 720 disposiciones posibles

- Vecindario: Intercambio de dos personas

- Limitación: Puede quedar atrapado en óptimos locales

## 💰 Punto 2: Problema del Cambio de Monedas

### 📋 Descripción

Algoritmo voraz para dar cambio de $63 usando monedas de [50, 20, 10, 5, 1], minimizando la cantidad de monedas.

### 🎯 Objetivo

Introducir el concepto de equilibrio y demostrar estrategias de selección local óptima.

### ⚙️ Implementación

```python

def cambio_voraz(cantidad, monedas):
    resultado = {}
    for moneda in monedas:
        if cantidad >= moneda:
            num = cantidad // moneda
            cantidad -= num * moneda
            resultado[moneda] = num
    return resultado

monedas = [50, 20, 10, 5, 1]
cambio = cambio_voraz(63, monedas)

```
### 🔍 Proceso para $63

- $50: 1 moneda → Restante: $13

- $20: ❌ No aplica

- $10: 1 moneda → Restante: $3

- $5: ❌ No aplica

- $1: 3 monedas → Restante: $0

Resultado: 1×$50 + 1×$10 + 3×$1 = 5 monedas

### 📈 Análisis

- Optimalidad: Óptimo para sistemas canónicos de monedas

- Complejidad: O(n) donde n es número de denominaciones

- Limitación: No óptimo para sistemas no canónicos


## 🎮 Punto 3: Piedra, Papel o Tijera


### 📋 Descripción

Implementación del equilibrio de Nash en el juego clásico mediante estrategia mixta uniforme.

### 🎯 Objetivo

Mostrar cómo la estrategia "siempre toma lo mejor ahora" puede o no llevar a la solución óptima en contextos adversariales.

### ⚙️ Implementación

```python

import random

opciones = ["Piedra", "Papel", "Tijera"]

def estrategia_optima():
    return random.choice(opciones)  # Distribución uniforme 1/3

def jugar_ronda():
    jugador = estrategia_optima()
    oponente = estrategia_optima()
    # Lógica de determinación del ganador

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
