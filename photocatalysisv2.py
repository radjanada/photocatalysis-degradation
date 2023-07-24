import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def main():
    print("Welcome to the Photocatalysis Experiment Data Analysis App (V2)!")
    
    plot_title = input("Enter the title of the plot: ")
    time_values_str = input("Enter time values (comma separated): ")
    time_values = np.array([float(x) for x in time_values_str.split(",")])

    time_unit = input("Enter the unit of time: ")

    num_plots = int(input("How many plots do you have? Enter a number: "))

    plot_data = []

    for i in range(num_plots):
        plot_name = input(f"Enter the name of Plot {i + 1}: ")
        color = input(f"Enter the color for Plot {i + 1} (e.g., 'red', 'blue', '#FF0000'): ")

        absorbance_str = input(f"Enter absorbance values for {plot_name} (comma separated): ")
        absorbance_values = np.array([float(x) for x in absorbance_str.split(",")])

        # Mask the points where the absorbance is zero
        mask = absorbance_values != 0
        time_values_plot = time_values[mask]
        absorbance_values_plot = absorbance_values[mask]

        # Interpolate absorbance values only up to the maximum time value
        time_max = np.max(time_values_plot)
        mask_interp = time_values <= time_max
        absorbance_values_interp = np.interp(time_values[mask_interp], time_values_plot, absorbance_values_plot)

        ln_ratio = np.log(absorbance_values_interp / absorbance_values_interp[0])
        plot_data.append((plot_name, color, time_values[mask_interp], ln_ratio))

    # Print the table with Time, Absorbance, and ln(A_t/A_0) for all plots
    num_cols = 1 + num_plots * 2
    data_table = []

    headers = ["Time (minutes)"]
    for i in range(num_plots):
        headers.extend([f"Absorbance Plot {i + 1} (AU)", f"ln(A_t/A_0) Plot {i + 1}"])
    data_table.append(headers)

    for row_idx in range(max(len(time_values[mask]) for _, _, time_values_plot, _ in plot_data)):
        data_row = ["" for _ in range(num_cols)]
        for i, (plot_name, _, time_values_plot, ln_ratio) in enumerate(plot_data):
            if row_idx < len(time_values_plot):
                data_row[0] = f"{time_values_plot[row_idx]:.3f}"
                data_row[1 + 2 * i] = f"{absorbance_values[mask][row_idx]:.3f}"
                data_row[2 + 2 * i] = f"{ln_ratio[row_idx]:.3f}"
        data_table.append(data_row)

    # Print the table
    print("\nTable of Data:")
    print("===========================================")
    for row in data_table:
        print(" | ".join(row))

    # Plotting the data
    plt.figure(figsize=(10, 6))

    for i, (plot_name, color, time_values, ln_ratio) in enumerate(plot_data):
        plt.plot(time_values, ln_ratio, marker='o', label=f'Degradation {plot_name} (ln(A_t/A_0))', color=color)

    # Adding labels and title
    plt.xlabel(f"Time ({time_unit})")
    plt.ylabel("Degradation (ln(A_t/A_0))")
    plt.title(plot_title)

    # Set both axes to start from 0
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    # Set the limits of the plot
    plt.xlim(0, np.max(time_values))
    plt.ylim(np.nanmin(ln_ratio) - 0.5, np.nanmax(ln_ratio) + 0.5)

    # Add legend in the top right of the plot
    plt.legend(loc='upper right', fontsize='small')

    plt.grid()
    plt.tight_layout()

    # Calculate and display R squared, equation, and slope for each plot
    print("\nResults:")
    print("===========================================")
    for i, (plot_name, _, _, ln_ratio) in enumerate(plot_data):
        slope, intercept, r_value, _, _ = linregress(time_values, ln_ratio)
        equation = f"y = {slope:.4f}x + {intercept:.4f}"
        r_squared = f"R-squared: {r_value**2:.4f}"
        k = f"Slope (k): {slope:.4f} min^-1"

        print(f"\nResults for {plot_name}:")
        print(equation)
        print(r_squared)
        print(k)

    plt.show()

if __name__ == "__main__":
    main()
