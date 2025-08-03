from templates import line_chart as lc

if __name__ == "__main__":
    # --- Example Usage for the Stress-Strain Diagram ---
    # Define file paths
    data_file = "data/stress_strain_data.csv"
    output_file = "figures/stress_strain_plot.png"  # You can also use .svg, .pdf, etc.

    # Define plot parameters
    x_axis_col = "Strain"
    y_axis_cols = ["Stress_Steel", "Stress_Aluminium", "Stress_Titanium"]
    legend_labels = ["Steel", "Aluminium Alloy", "Titanium Alloy"]

    # Generate the plot
    lc.create_line_plot(
        data_path=data_file,
        output_path=output_file,
        x_column=x_axis_col,
        y_columns=y_axis_cols,
        x_label="Strain (mm/mm)",
        y_label="Stress (MPa)",
        title="Stress-Strain Diagram for Three Materials",
        legend_labels=legend_labels,
    )
