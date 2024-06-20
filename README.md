# slcc

Simulation code for the paper "Behavioral evolution under social learning with complex contagion" by Chiba-Okabe, H. and Plotkin, J. See the paper for the details of the model.

## Instruction

Run the `main.py` to execute the simulations. Other files are:

- `config.py`: Configuration file for setting parameters.
- `simulation.py`: Contains the simulation model.
- `utils.py`: Utility functions for saving and zipping plots.

## Games

The code runs simulations for three game types:
- 0: Donation game
- 1: Snowdrift game
- 2: Coordination game

### Donation Game

$$
\begin{pmatrix}
b - c & -c \\
b & 0 
\end{pmatrix}
$$

### Snowdrift Game

$$
\begin{pmatrix}
b - \frac{c}{2} & b - c \\
b & 0 
\end{pmatrix}
$$

### Coordination Game

$$
\begin{pmatrix}
a & 0 \\
0 & b 
\end{pmatrix}
$$
