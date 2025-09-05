"""
line_plot.py

A reusable template for creating a simple line plot with up to three datasets.
This script is designed to be part of a larger figure template repository.
It applies a consistent style and saves a high-quality figure.

Datasets Format:
    datasets (dict): A dictionary where each key is a dataset name (str), and each value is another dict containing:
        - 'x' (list/array): The x-axis data for this dataset.
        - 'y' (list/array): The y-axis data for this dataset.
        - 'label' (str, optional): The legend label for this dataset. Defaults to the key name.
    Example:
        datasets = {
            "Steel": {"x": [0, 1, 2], "y": [0, 1, 4], "label": "Steel"},
            "Aluminium": {"x": [0, 1, 2], "y": [0, 2, 3]},
        }
"""

import matplotlib.pyplot as plt

from styles import three_lines_chart


def create_3line_plot(
    datasets: dict,
    output_path: str,
    x_label: str = "X-axis",
    y_label: str = "Y-axis",
    title: str = "Line Plot",
):
    """
    Generates and saves a high-quality line plot from a dictionary of datasets.

    Args:
        datasets (dict): A dictionary where keys are dataset names (str), and values are dicts with 'x' (list/array), 'y' (list/array), and optionally 'label' (str).
        output_path (str): Path to save the output figure.
        x_label (str): Label for the x-axis.
        y_label (str): Label for the y-axis.
        title (str): The title of the plot.
    """
    # Apply the custom Matplotlib style from _style_config.py
    plt.rcParams.update(three_lines_chart.mpl_style)

    # Create the figure and axes
    fig, ax = plt.subplots()

    # Get colors and line styles from the style configuration
    colors = three_lines_chart.COLORS
    line_styles = three_lines_chart.LINE_STYLES

    # Plot each dataset
    for i, (name, data) in enumerate(datasets.items()):
        x = data["x"]
        y = data["y"]
        label = data.get("label", name)
        ax.plot(
            x,
            y,
            color=colors[i % len(colors)],
            linestyle=line_styles[i % len(line_styles)],
            label=label,
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


def create_5line_plot(
    datasets: dict,
    output_path: str,
    x_label: str = "X-axis",
    y_label: str = "Y-axis",
    title: str = "Line Plot",
):
    """
    Generates and saves a high-quality line plot from a dictionary of datasets.

    Args:
        datasets (dict): A dictionary where keys are dataset names (str), and values are dicts with 'x' (list/array), 'y' (list/array), and optionally 'label' (str).
        output_path (str): Path to save the output figure.
        x_label (str): Label for the x-axis.
        y_label (str): Label for the y-axis.
        title (str): The title of the plot.
    """
    from styles import five_lines_chart

    # Apply the custom Matplotlib style from _style_config.py
    plt.rcParams.update(five_lines_chart.mpl_style)

    # Create the figure and axes
    fig, ax = plt.subplots()

    # Get colors and line styles from the style configuration
    colors = five_lines_chart.COLORS
    line_styles = five_lines_chart.LINE_STYLES

    # Plot each dataset
    for i, (name, data) in enumerate(datasets.items()):
        x = data["x"]
        y = data["y"]
        label = data.get("label", name)
        ax.plot(
            x,
            y,
            color=colors[i % len(colors)],
            linestyle=line_styles[i % len(line_styles)],
            label=label,
            zorder=10 - i,  # Ensure the first line is on top
        )

    # Customize the plot
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.legend(loc="lower right")
    ax.grid(True)

    # Save the figure to the specified path
    plt.savefig(output_path, bbox_inches="tight")
    plt.show()
    # plt.close(fig)  # Close the figure to free up memory
    # print(f"Plot saved to: {output_path}")
