# ising_model.py

import random
import math

def create_matrix(length):
    # Generate a random matrix of spins +1 and -1
    return [[random.choice([-1, 1]) for _ in range(length)] for _ in range(length)]

def calculate_energy(matrix, i, j, J):
    # Calculate local energy at position (i, j) with periodic boundaries
    length = len(matrix)
    spin = matrix[i][j]
    neighbors = (
        matrix[i][(j - 1) % length] +
        matrix[i][(j + 1) % length] +
        matrix[(i - 1) % length][j] +
        matrix[(i + 1) % length][j]
    )
    # Standard Ising energy term: -J * s_i * sum(neighbors)
    return -J * spin * neighbors

def calculate_total_energy(matrix, J):
    # Sum over all spins (divide by 2 to correct double counting)
    length = len(matrix)
    total = 0
    for i in range(length):
        for j in range(length):
            total += calculate_energy(matrix, i, j, J)
    return total / 2

def accept_change(delta_energy, T=1.0):
    # Metropolis acceptance criterion at temperature T
    return random.random() < min(1, math.exp(-delta_energy / T))

def perform_simulation(length, steps, J, T=1.0):
    matrix = create_matrix(length)
    energy = calculate_total_energy(matrix, J)
    print("Initial total energy:", energy)

    for step in range(1, steps + 1):
        i = random.randrange(length)
        j = random.randrange(length)
        # If we flip spin s -> -s, energy change is ΔE = -2 * E_local
        delta_energy = -2 * calculate_energy(matrix, i, j, J)

        if accept_change(delta_energy, T):
            matrix[i][j] *= -1
            energy += delta_energy

        if step % 50 == 0:
            print(f"Total energy after step {step}: {energy}")

    return energy

def main():
    length = int(input("Enter the matrix size: "))
    steps  = int(input("Enter the number of steps: "))
    J      = float(input("Enter the coupling constant J: "))
    T_input = input("Enter temperature T [default 1.0]: ").strip()
    T      = float(T_input) if T_input else 1.0

    final_energy = perform_simulation(length, steps, J, T)
    print("Final total energy:", final_energy)

if __name__ == "__main__":
    main()
