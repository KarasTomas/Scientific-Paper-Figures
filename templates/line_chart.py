"""
line_plot.py

A reusable template for creating a simple line plot with up to three datasets.
This script is designed to be part of a larger figure template repository.
It reads data, applies a consistent style, and saves a high-quality figure.
"""

import matplotlib.pyplot as plt
import pandas as pd

from styles import three_lines_chart


def create_line_plot(
    data_path: str,
    output_path: str,
    x_column: str,
    y_columns: list,
    x_label: str = "X-axis",
    y_label: str = "Y-axis",
    title: str = "Line Plot",
    legend_labels: list = None,
):
    """
    Generates and saves a high-quality line plot.

    Args:
        data_path (str): Path to the input data file (e.g., CSV).
        output_path (str): Path to save the output figure.
        x_column (str): The name of the column for the x-axis.
        y_columns (list): A list of column names for the y-axes.
        x_label (str): Label for the x-axis.
        y_label (str): Label for the y-axis.
        title (str): The title of the plot.
        legend_labels (list): A list of labels for the legend.
    """
    try:
        # Load the data using pandas
        data = pd.read_csv(data_path)
    except FileNotFoundError:
        print(f"Error: The file '{data_path}' was not found.")
        return

    # Apply the custom Matplotlib style from _style_config.py
    plt.rcParams.update(three_lines_chart.mpl_style)

    # Create the figure and axes
    fig, ax = plt.subplots()

    # Get colors and line styles from the style configuration
    colors = three_lines_chart.COLORS
    line_styles = three_lines_chart.LINE_STYLES

    # Check for consistency
    if len(y_columns) > len(colors) or len(y_columns) > len(line_styles):
        print("Warning: Not enough colors or line styles defined for all datasets.")

    if legend_labels is None:
        legend_labels = y_columns

    # Plot each dataset
    for i, col in enumerate(y_columns):
        ax.plot(
            data[x_column],
            data[col],
            color=colors[i % len(colors)],
            linestyle=line_styles[i % len(line_styles)],
            label=legend_labels[i],
            zorder=10 - i,  # Ensure the first line is on top
        )

    # Customize the plot
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.legend()
    ax.grid(True)

    # Save the figure to the specified path
    plt.savefig(output_path, bbox_inches="tight")
    plt.show()
    # plt.close(fig)  # Close the figure to free up memory
    # print(f"Plot saved to: {output_path}")
