import random
import math

def create_matrix(length):
    return [[random.randint(0, 1) for _ in range(length)] for _ in range(length)]

def calculate_energy(matrix, i, j, J):
    length = len(matrix)
    current = matrix[i][j]
    energy = 0

    energy += J * (current - matrix[i][(j - 1) % length])  
    energy += J * (current - matrix[i][(j + 1) % length])  
    energy += J * (current - matrix[(i - 1) % length][j])  
    energy += J * (current - matrix[(i + 1) % length][j]) 

    return energy

def calculate_total_energy(matrix, J):
    length = len(matrix)
    total = 0
    for i in range(length):
        for j in range(length):
            total += calculate_energy(matrix, i, j, J)
    return total

def accept_change(delta_energy):
    # Metropolis criterion
    return random.random() < min(1, math.exp(-delta_energy))

def perform_simulation(length, steps, J):
    matrix = create_matrix(length)
    energy = calculate_total_energy(matrix, J)
    print("Initial total energy:", energy)

    for step in range(steps):
        i = random.randint(0, length - 1)
        j = random.randint(0, length - 1)
        delta_energy = -2 * calculate_energy(matrix, i, j, J)

        if accept_change(delta_energy):
            matrix[i][j] = 1 - matrix[i][j]  # Flip spin
            energy += delta_energy

        if (step + 1) % 50 == 0:
            print(f"Total energy after step {step + 1}: {energy}")

    return energy

def main():
    length = int(input("Enter the length of the array: "))
    steps = int(input("Enter the number of steps: "))
    J = int(input("Enter the value for J: "))

    final_energy = perform_simulation(length, steps, J)
    print("Final total energy:", final_energy)

if __name__ == '__main__':
    main()
