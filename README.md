# Monte Carlo Simulation of the 2D Ising Model

This repository contains a Python implementation of the 2D Ising model using the Metropolis Monte Carlo method. The simulation evolves a square lattice of spins and reports the total energy at regular intervals.

## Overview

The Ising model is a fundamental model in statistical mechanics used to study ferromagnetism. Each site on a lattice carries a spin that interacts with its four nearest neighbors. The Metropolis algorithm probabilistically accepts or rejects spin flips based on the change in total energy and temperature, allowing the system to explore low-energy configurations over time.

In this implementation:
- Spins take values of **-1** or **+1**
- Each spin interacts with its four nearest neighbors
- Periodic boundary conditions connect edges of the matrix
- The Metropolis criterion is applied to accept or reject spin flips, with a temperature parameter

## Files

- `ising model.py` — main simulation script

## Features

- Random initialization of a square spin matrix
- Local and total energy calculations using coupling constant `J`
- Metropolis Monte Carlo updates with temperature `T`
- Periodic boundary conditions
- Console output of total energy every 50 steps

## How to Run

1. Clone or download the repository.
2. Ensure you have Python 3 installed.
3. Run the simulation:

   ```bash
   python ising\ model.py
   ```

4. When prompted, enter:

   * **length**: size of the square spin matrix (e.g., `10`)
   * **steps**: number of Monte Carlo steps (e.g., `500`)
   * **J**: coupling constant (e.g., `1`)
   * **T**: temperature (e.g., `2.0`)

Example interaction:

```
Enter the length of the array: 10
Enter the number of steps: 500
Enter the value for J: 1
Enter the temperature T: 2.0
Initial total energy: -40
Total energy after step 50: -52
Total energy after step 100: -60
...
Final total energy: -68
```

## Requirements

This script uses only built-in Python libraries:

* `random`
* `math`

No additional installations are required.

## Possible Extensions

* Plot energy vs. simulation steps using `matplotlib`
* Track and plot lattice magnetization over time
* Visualize the spin matrix dynamically (e.g., with `matplotlib` or `pygame`)

## License

This project is open source and provided for educational use. Feel free to modify and distribute under the MIT License.