
import os
import zipfile
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from simulation import Simulation

def save_and_zip_plots(simulation_number, gamma_values, init_freqs, a, b, c, d, time_steps, s_value, population_size, sample_size, plot_dir):
    zip_filename = f"{plot_dir}/plots_simulation_{simulation_number}.zip"
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for game_type in range(3):
            avg_final_freq = np.zeros((len(gamma_values), len(init_freqs)))
            for j, gamma in enumerate(gamma_values):
                for k, init_freq in enumerate(init_freqs):
                    sim = Simulation(gamma, game_type, a, b, c, d, time_steps, s_value, population_size, sample_size, init_freq)
                    sim.run()
                    avg_final_freq[j, k] = np.mean(sim.freq[-100000:])

                    plot_filename = f"plot_g{game_type}_gamma{gamma}_init{init_freq}.png"
                    plot_path = os.path.join(plot_dir, plot_filename)
                    plt.plot(sim.freq, color='r')
                    plt.axhline(y=avg_final_freq[j, k], color='b', linestyle='--')
                    plt.savefig(plot_path)
                    plt.close()

                    zipf.write(plot_path, os.path.basename(plot_path))
                    os.remove(plot_path)

            df = pd.DataFrame(avg_final_freq, columns=init_freqs, index=gamma_values)
            excel_filename = f"{plot_dir}/avg_freq_game_type_{game_type}_simulation_{simulation_number}.xlsx"
            df.to_excel(excel_filename, index=True)
