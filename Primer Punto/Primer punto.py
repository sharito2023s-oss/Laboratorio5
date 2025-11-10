import random

# Simulamos niveles de satisfacción entre las personas (6 personas)
# satisfaction[i][j] = cuánto le gusta a la persona i sentarse junto a j
satisfaction = [[0, 5, -2, 3, 1, 4],
                [5, 0, 3, -1, 2, 2],
                [-2, 3, 0, 4, -3, 5],
                [3, -1, 4, 0, 2, 1],
                [1, 2, -3, 2, 0, 4],
                [4, 2, 5, 1, 4, 0]]

# Función para calcular satisfacción total de una disposición
def total_satisfaction(arrangement):
    total = 0
    n = len(arrangement)
    for i in range(n):
        left = arrangement[i - 1]  # Persona a la izquierda
        right = arrangement[(i + 1) % n]  # Persona a la derecha (circular)
        person = arrangement[i]
        total += satisfaction[person][left] + satisfaction[person][right]
    return total

# Hill Climbing
def hill_climbing():
    current = list(range(6))
    random.shuffle(current)
    current_value = total_satisfaction(current)

    for _ in range(1000):  # número de iteraciones
        i, j = random.sample(range(6), 2)
        neighbor = current[:]
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
        neighbor_value = total_satisfaction(neighbor)
        if neighbor_value > current_value:
            current, current_value = neighbor, neighbor_value
    return current, current_value

best_arrangement, best_score = hill_climbing()
print("🪑 Mejor disposición:", best_arrangement)
print("😄 Satisfacción total:", best_score)
