
import os
from config import *
from utils import save_and_zip_plots

def main():
    # Create directory to save plots
    os.makedirs(plot_dir, exist_ok=True)

    # Run multiple simulations and save results
    for sim_num in range(1, num_simulations + 1):
        save_and_zip_plots(sim_num, gamma_values, init_freqs, a, b, c, d, time_steps, s_value, population_size, sample_size, plot_dir)

if __name__ == "__main__":
    main()
