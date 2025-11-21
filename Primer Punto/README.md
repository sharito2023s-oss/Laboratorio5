# 🪑 Optimización de Disposición de Sillas con Hill Climbing

## 📋 Descripción del Proyecto

Este proyecto implementa un algoritmo de Hill Climbing para resolver el problema de organizar 6 sillas con 6 personas, maximizando la satisfacción total basada en las preferencias de cada persona por sentarse junto a otras.

## 🎯 Planteamiento del Problema

- 6 personas y 6 sillas en disposición circular

- Cada persona tiene niveles de satisfacción específicos por sentarse junto a otras

- Objetivo: Encontrar la disposición que maximice la satisfacción total

- Restricción: Las sillas están organizadas en círculo (cada persona tiene 2 vecinos)

## 📊 Matriz de Satisfacción

```python

satisfaction = [[0, 5, -2, 3, 1, 4],
                [5, 0, 3, -1, 2, 2],
                [-2, 3, 0, 4, -3, 5],
                [3, -1, 4, 0, 2, 1],
                [1, 2, -3, 2, 0, 4],
                [4, 2, 5, 1, 4, 0]]

```

Interpretación: satisfaction[i][j] representa cuánto le gusta a la persona i sentarse junto a la persona j.


## ⚙️ Algoritmo Hill Climbing Implementado

### 🔄 Función de Evaluación


```text

def total_satisfaction(arrangement):
    total = 0
    n = len(arrangement)
    for i in range(n):
        left = arrangement[i - 1]  # Persona a la izquierda
        right = arrangement[(i + 1) % n]  # Persona a la derecha (circular)
        person = arrangement[i]
        total += satisfaction[person][left] + satisfaction[person][right]
    return total

```

Características:

- Considera la disposición circular de las sillas

- Calcula la satisfacción de cada persona con sus dos vecinos

- Suma todas las satisfacciones individuales


## 🧭 Algoritmo de Búsqueda

```text

def hill_climbing():
    current = list(range(6))
    random.shuffle(current)  # Solución inicial aleatoria
    current_value = total_satisfaction(current)

    for _ in range(1000):  # 1000 iteraciones máximas
        i, j = random.sample(range(6), 2)  # Selecciona 2 personas aleatorias
        neighbor = current[:]  # Crea vecino intercambiando 2 personas
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
        neighbor_value = total_satisfaction(neighbor)
        
        # Criterio de aceptación: solo mejora
        if neighbor_value > current_value:
            current, current_value = neighbor, neighbor_value
            
    return current, current_value

```

## 🎯 Estrategia de Optimización

### 🔍 Generación de Vecinos

- Operador: Intercambio de dos personas aleatorias

- Espacio de búsqueda: 6! = 720 disposiciones posibles

- Movimiento: Pequeñas modificaciones locales

### 📈 Criterio de Aceptación

- Hill Climbing Simple: Solo acepta mejoras

- Sin reinicios: Búsqueda desde un punto inicial aleatorio

- Máximo local: Puede quedar atrapado en óptimos locales

## 💡 Resultados Esperados

### 🎯 Salida del Programa

```python

best_arrangement, best_score = hill_climbing()
print("🪑 Mejor disposición:", best_arrangement)
print("😄 Satisfacción total:", best_score)

```

Ejemplo de salida:


```text

🪑 Mejor disposición: [2, 4, 1, 5, 0, 3]
😄 Satisfacción total: 42

```

## ⚡ Características Técnicas


### 🔧 Parámetros del Algoritmo

- Iteraciones: 1000 como límite máximo

- Vecindario: Intercambios de 2 elementos

- Inicialización: Aleatoria

- Condición de parada: Máximo de iteraciones


```python

def find_flower_for_scout(self, drone):
    # Explora todas las áreas del invernadero
    # Busca flores listas en cualquier zona
    # Movimiento aleatorio cuando no hay objetivos

```

## 🎨 Representación Visual

- Disposición circular: Cada persona tiene exactamente 2 vecinos

- Satisfacción asimétrica: A puede gustarle B diferente a como B gusta de A

- Valores negativos: Indican disgusto por sentarse junto a alguien


## 👥 Autores

#### 🧑‍💻 Contribuidores Principales

- **Carlos Andrés Suárez Torres** → [Carlos23Andres](https://github.com/Carlos23Andres)  

- **Saira Sharid Sanabria Muñoz** → [sharito202](https://github.com/sharito202)
