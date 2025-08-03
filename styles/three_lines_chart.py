"""
_style_config.py

This file defines all the stylistic parameters for the figure templates.
It can be imported into any plotting script to ensure a consistent look and feel.
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
# A minimalist palette with shades of black and gray.
# The order corresponds to the order in which data is plotted.
COLORS = [
    "#000000",  # Black
    "#555555",  # Dark Gray
    "#999999",  # Medium Gray
    # Add more colors for more datasets if needed
]

# Line styles to differentiate between datasets without relying solely on color.
LINE_STYLES = [
    "-",  # Solid line
    "--",  # Dashed line
    ":",  # Dotted line
    "-.",  # Dash-dotted line
]

# Marker styles, for use in scatter plots or line plots with markers.
MARKERS = [
    "o",  # Circle
    "s",  # Square
    "^",  # Triangle up
    "v",  # Triangle down
    "D",  # Diamond
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
    # Grid properties
    "axes.grid": True,
    "grid.color": "#D3D3D3",
    "grid.linestyle": "--",
    "grid.linewidth": 0.5,
    "grid.alpha": 0.8,
    # Legend properties
    "legend.fontsize": LEGEND_SIZE,
    "legend.frameon": False,  # No box around the legend
    "legend.handlelength": 2,
    # Line properties
    "lines.linewidth": 1.5,
    "lines.markersize": 5,
    # Saving properties
    "savefig.dpi": DPI,
    "savefig.transparent": False,  # Set to False to disable transparency
    "savefig.facecolor": "white",  # Explicitly set the background to white
}
