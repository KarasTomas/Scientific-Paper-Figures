"""
_style_config.py

This file defines all the stylistic parameters for the figure templates.
It can be imported into any plotting script to ensure a consistent look and feel.
Based on best practices from 'Python Scientific Figure Template Design_.md':
- Use colorblind-safe, distinct colors for accessibility.
- Employ serif fonts (e.g., Times New Roman) for professional, publication-ready figures.
- Ensure minimalism: no chartjunk, clear grids, and redundant differentiation (e.g., line styles).
- Support up to 5+ datasets with qualitative palettes and varied line styles/markers.
"""

# --- Figure and Font Settings ---
# Recommended figure size for single-column publication figures in inches.
FIG_WIDTH = 3.5  # Width in inches = 8.9 cm
FIG_HEIGHT = 2.5  # Height in inches = 6.35 cm
DPI = 300  # Dots per inch for high-quality raster exports

# Font settings for a clean, professional look. Times New Roman is a classic
# choice for scientific publications.
FONT_FAMILY = "serif"
FONT_SERIF = ["Times New Roman", "DejaVu Serif", "Computer Modern Roman"]
FONT_SIZE = 10
FONT_WEIGHT = "normal"

TITLE_SIZE = FONT_SIZE + 2
LABEL_SIZE = FONT_SIZE
TICK_SIZE = FONT_SIZE - 2
LEGEND_SIZE = FONT_SIZE - 2


# --- Color and Line Style Palettes ---
# Based on Matplotlib's tab10 for accessibility; use line styles/markers for redundancy.
COLORS = [
    "#1f77b4",  # Blue
    "#ff7f0e",  # Orange
    "#2ca02c",  # Green
    "#d62728",  # Red
    "#9467bd",  # Purple
    "#8c564b",  # Brown
    # Limit to ≤10 for clarity; add more if needed, but test for distinction.
]

# Line styles to differentiate datasets without relying solely on color (essential for accessibility).
LINE_STYLES = [
    "-",  # Solid line
    "--",  # Dashed line
    ":",  # Dotted line
    "-.",  # Dash-dotted line
    "-",  # Solid
    "--",  # Dashed
]

# Marker styles for scatter plots or added redundancy in line plots.
MARKERS = [
    "o",  # Circle
    "s",  # Square
    "^",  # Triangle up
    "v",  # Triangle down
    "D",  # Diamond
    "*",  # Star
]

# --- Matplotlib RCParams for a Consistent Style ---
# This dictionary contains all the default settings for Matplotlib plots.
# We will use this to override the default Matplotlib style.
mpl_style = {
    # Figure properties
    "figure.figsize": (FIG_WIDTH, FIG_HEIGHT),
    "figure.dpi": DPI,
    "figure.autolayout": True,  # Adjusts subplot params for tight layout
    # Font properties
    "font.family": FONT_FAMILY,
    "font.serif": FONT_SERIF,
    "font.size": FONT_SIZE,
    "font.weight": FONT_WEIGHT,
    "text.usetex": False,  # Set to True if you have a LaTeX distribution
    "mathtext.fontset": "cm",  # Computer Modern fonts for math text
    # Axes properties
    "axes.labelsize": LABEL_SIZE,
    "axes.titlesize": TITLE_SIZE,
    "axes.labelweight": FONT_WEIGHT,
    "axes.titleweight": FONT_WEIGHT,
    "axes.linewidth": 0.8,
    "axes.edgecolor": "#333333",  # Darker axes for better visibility
    "axes.facecolor": "white",
    # Tick properties
    "xtick.labelsize": TICK_SIZE,
    "ytick.labelsize": TICK_SIZE,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "xtick.major.size": 4,
    "ytick.major.size": 4,
    "xtick.major.width": 0.8,
    "ytick.major.width": 0.8,
    "xtick.minor.size": 2,
    "ytick.minor.size": 2,
    "xtick.minor.width": 0.6,
    "ytick.minor.width": 0.6,
    "xtick.top": True,
    "ytick.right": True,
    # Grid properties (minimal and light for clarity, per guidelines)
    "axes.grid": True,
    "grid.color": "#D3D3D3",
    "grid.linestyle": "--",
    "grid.linewidth": 0.5,
    "grid.alpha": 0.8,
    # Legend properties
    "legend.fontsize": LEGEND_SIZE,
    "legend.frameon": True,  # Enable frame for background
    "legend.facecolor": "white",  # White background to avoid grid interference
    "legend.edgecolor": "grey",  # Optional: add a subtle border
    "legend.handlelength": 2,
    # Line properties
    "lines.linewidth": 1.5,
    "lines.markersize": 5,
    # Saving properties
    "savefig.dpi": DPI,
    "savefig.transparent": False,  # Set to False to disable transparency
    "savefig.facecolor": "white",  # Explicitly set the background to white
}
