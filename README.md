# slcc

Simulation code for the paper "[Social learning with complex contagion](https://arxiv.org/abs/2406.14922)" by Chiba-Okabe, H. and Plotkin, J. See the paper for the details of the model.

## Instruction

Run the `main.py` to execute the simulations. Other files are:

- `config.py`: Configuration file for setting parameters.
- `simulation.py`: Contains the simulation code for the stochastic model.
- `utils.py`: Utility functions for producing plots.

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
