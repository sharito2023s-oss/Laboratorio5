# 💰 Algoritmo Voraz para el Problema del Cambio de Monedas

## 📋 Descripción del Proyecto

Este proyecto implementa un algoritmo voraz (greedy) para resolver el problema clásico de dar cambio utilizando la menor cantidad de monedas posibles. El algoritmo selecciona sistemáticamente la moneda de mayor denominación disponible en cada paso.

## 🎯 Planteamiento del Problema

- Cantidad a cambiar: $63

- Denominaciones disponibles: [50, 20, 10, 5, 1]

- Objetivo: Encontrar la combinación de monedas que sume exactamente $63

- Restricción: Minimizar la cantidad total de monedas utilizadas

## ⚙️ Algoritmo Voraz Implementado

### 🔄 Función Principal

```python

def cambio_voraz(cantidad, monedas):
    resultado = {}
    for moneda in monedas:
        if cantidad >= moneda:
            num = cantidad // moneda
            cantidad -= num * moneda
            resultado[moneda] = num
    return resultado
```



## 📦 Conjunto de Monedas


```text
monedas = [50, 20, 10, 5, 1]

```

## 🎯 Estrategia del Algoritmo

### 🔍 Proceso Paso a Paso para $63


```text
1. Paso 1: $63 ≥ $50 → 1 moneda de $50

        Restante: $63 - $50 = $13

2. Paso 2: $13 ≥ $20? ❌ No → Saltar

        $13 < $20, no se puede usar

3. Paso 3: $13 ≥ $10 → 1 moneda de $10

        Restante: $13 - $10 = $3

4. Paso 4: $3 ≥ $5? ❌ No → Saltar

        $3 < $5, no se puede usar

5 .Paso 5: $3 ≥ $1 → 3 monedas de $1

        Restante: $3 - $3 = $0 ✅
```

## 📊 Resultado Final

```text

cambio = cambio_voraz(63, monedas)
print("💰 Cambio voraz para $63:")
for moneda, cantidad in cambio.items():
    print(f"  {cantidad} moneda(s) de ${moneda}")


```

Salida esperada:

```text

💰 Cambio voraz para $63:
  1 moneda(s) de $50
  1 moneda(s) de $10
  3 moneda(s) de $1

```

## ⚡ Características del Algoritmo

### ✅ Propiedades del Enfoque Voraz

- Selección local óptima: En cada paso elige la moneda más grande posible

- Eficiencia: Complejidad O(n) donde n es el número de denominaciones

- Simplicidad: Fácil de implementar y entender

- Determinismo: Siempre produce el mismo resultado para la misma entrada

### 🔢 Métricas de Rendimiento

- Total de monedas: 1 + 1 + 3 = 5 monedas

- Eficiencia: Utiliza las monedas más grandes primero

- Completitud: Siempre encuentra una solución si las monedas incluyen denominación 1

## 💡 Análisis de Optimalidad

###✅ Casos donde es Óptimo

El algoritmo voraz es óptimo para sistemas de monedas como:

- Sistema decimal: [100, 50, 20, 10, 5, 1]

- Sistema canónico donde cada moneda es múltiplo de la siguiente

## ⚠️ Casos donde NO es Óptimo

Ejemplo contra-intuitivo:

- Cantidad: $30

- Monedas: [25, 10, 1]

- Voraz: 25 + 1 + 1 + 1 + 1 + 1 = 6 monedas

- Óptimo: 10 + 10 + 10 = 3 monedas

## 🎓 Conceptos Algorítmicos Clave

1. Elección Voraz (Greedy Choice)
python

```python

# Siempre selecciona la moneda más grande posible
if cantidad >= moneda:
    num = cantidad // moneda  # Máxima cantidad de esta denominación
```

2. Subestructura Óptima

- El problema se reduce después de cada selección

- La solución del subproblema contribuye a la solución global

3. Propiedad de Monedas Canónicas
python

```python
# Para que el algoritmo voraz sea óptimo:
monedas = [50, 20, 10, 5, 1]  # Sistema canónico
```

## 👥 Autores

#### 🧑‍💻 Contribuidores Principales

- **Carlos Andrés Suárez Torres** → [Carlos23Andres](https://github.com/Carlos23Andres)  

- **Saira Sharid Sanabria Muñoz** → [sharito202](https://github.com/sharito202)
