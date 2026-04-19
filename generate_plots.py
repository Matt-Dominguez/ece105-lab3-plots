"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""
#impport necessary libraries
# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.

import numpy as np
import matplotlib.pyplot as plt


def generate_data(seed):
    """Generate synthetic sensor temperature and timestamp data.
    
    Creates simulated temperature readings from two sensors and corresponding
    timestamps using NumPy's modern random number generator.
    
    Parameters
    ----------
    seed : int
        Random seed for reproducibility.
    
    Returns
    -------
    sensor_a : ndarray
        (200,) array of temperature readings in Celsius from Sensor A,
        drawn from normal distribution with mean=25°C, std=3°C.
    sensor_b : ndarray
        (200,) array of temperature readings in Celsius from Sensor B,
        drawn from normal distribution with mean=27°C, std=4.5°C.
    timestamps : ndarray
        (200,) array of timestamps in seconds, uniformly distributed from
        0 to 10 seconds and sorted chronologically.
    """
    rng = np.random.default_rng(seed=seed)
    
    sensor_a = rng.normal(loc=25, scale=3, size=200)
    sensor_b = rng.normal(loc=27, scale=4.5, size=200)
    timestamps = np.sort(rng.uniform(low=0, high=10, size=200))
    
    return sensor_a, sensor_b, timestamps

# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Create scatter plot of sensor readings vs time on given Axes.
    
    Draws a scatter plot showing temperature readings from two sensors
    over time, with distinct colors and transparency to show overlap.
    Modifies the Axes object in place.
    
    Parameters
    ----------
    sensor_a : ndarray
        (200,) array of temperature readings in Celsius from Sensor A.
    sensor_b : ndarray
        (200,) array of temperature readings in Celsius from Sensor B.
    timestamps : ndarray
        (200,) array of timestamps in seconds.
    ax : matplotlib.axes.Axes
        Axes object to draw on. Modified in place.
    
    Returns
    -------
    None
    """
    ax.scatter(timestamps, sensor_a, color='blue', label='Sensor A', alpha=0.6, s=50)
    ax.scatter(timestamps, sensor_b, color='orange', label='Sensor B', alpha=0.6, s=50)
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Sensor Temperature Readings Over Time')
    ax.legend()
    ax.grid(True, alpha=0.3)

# Overlaid histogram of Sensor A and Sensor B temperature distributions.
# Use 30 bins, alpha=0.5 for transparency so both distributions are visible.
# Add vertical dashed lines at each sensor's mean.
# Include a legend labeling each sensor.

def plot_histogram(sensor_a, sensor_b, ax):
    """Create overlaid histogram of sensor temperature distributions on given Axes.
    
    Draws overlaid histograms showing the temperature distributions from two
    sensors, with vertical dashed lines indicating each sensor's mean.
    Modifies the Axes object in place.
    
    Parameters
    ----------
    sensor_a : ndarray
        (200,) array of temperature readings in Celsius from Sensor A.
    sensor_b : ndarray
        (200,) array of temperature readings in Celsius from Sensor B.
    ax : matplotlib.axes.Axes
        Axes object to draw on. Modified in place.
    
    Returns
    -------
    None
    """
    ax.hist(sensor_a, bins=30, alpha=0.5, label='Sensor A')
    ax.hist(sensor_b, bins=30, alpha=0.5, label='Sensor B')
    ax.axvline(sensor_a.mean(), linestyle='--', linewidth=2, 
               label=f'Sensor A Mean: {sensor_a.mean():.2f}°C')
    ax.axvline(sensor_b.mean(), linestyle='--', linewidth=2,
               label=f'Sensor B Mean: {sensor_b.mean():.2f}°C')
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Frequency')
    ax.set_title('Temperature Distribution Comparison')
    ax.legend()
    ax.grid(True, alpha=0.3)

# Side-by-side box plot comparing Sensor A and Sensor B distributions.
# Label x-axis with sensor names, y-axis with "Temperature (deg C)".
# Add a horizontal dashed line at the overall mean of both sensors combined.

def plot_boxplot(sensor_a, sensor_b, ax):
    """Create side-by-side box plot comparing sensor temperature distributions.
    
    Draws box plots for both sensors showing distribution statistics
    (median, quartiles, outliers). Includes a horizontal reference line
    at the overall mean. Modifies the Axes object in place.
    
    Parameters
    ----------
    sensor_a : ndarray
        (200,) array of temperature readings in Celsius from Sensor A.
    sensor_b : ndarray
        (200,) array of temperature readings in Celsius from Sensor B.
    ax : matplotlib.axes.Axes
        Axes object to draw on. Modified in place.
    
    Returns
    -------
    None
    """
    ax.boxplot([sensor_a, sensor_b], labels=['Sensor A', 'Sensor B'])
    overall_mean = np.mean(np.concatenate([sensor_a, sensor_b]))
    ax.axhline(overall_mean, linestyle='--', linewidth=2, 
               label=f'Overall Mean: {overall_mean:.2f}°C')
    ax.set_xlabel('Sensor')
    ax.set_ylabel('Temperature (deg C)')
    ax.set_title('Temperature Distribution Comparison')
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')

# Create main() that generates data, creates a 1x3 subplot figure,
# calls each plot function, adjusts layout, and saves as sensor_analysis.png
# at 150 DPI with tight bounding box.

def main():
    """Generate synthetic sensor data and create publication-quality visualizations.
    
    Creates three synchronized plots (scatter, histogram, box plot) showing
    temperature sensor data distributions, plus a summary statistics panel.
    Saves the figure as a PNG file.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    """
    # Generate synthetic sensor data with seed 6063
    sensor_a, sensor_b, timestamps = generate_data(seed=6063)
    
    # Create figure with 2x2 subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Create each plot
    plot_scatter(sensor_a, sensor_b, timestamps, axes[0, 0])
    plot_histogram(sensor_a, sensor_b, axes[0, 1])
    plot_boxplot(sensor_a, sensor_b, axes[1, 0])
    
    # Add summary statistics in the fourth subplot
    ax_stats = axes[1, 1]
    ax_stats.axis('off')
    
    stats_text = f"""
Summary Statistics

Sensor A:
  Mean:     {sensor_a.mean():.2f}°C
  Std Dev:  {sensor_a.std():.2f}°C
  Min:      {sensor_a.min():.2f}°C
  Max:      {sensor_a.max():.2f}°C

Sensor B:
  Mean:     {sensor_b.mean():.2f}°C
  Std Dev:  {sensor_b.std():.2f}°C
  Min:      {sensor_b.min():.2f}°C
  Max:      {sensor_b.max():.2f}°C

Overall:
  Combined Mean: {np.mean(np.concatenate([sensor_a, sensor_b])):.2f}°C
  Sample Size:   {len(sensor_a)} readings per sensor
"""
    
    ax_stats.text(0.1, 0.5, stats_text, fontfamily='monospace', fontsize=10,
                  verticalalignment='center', bbox=dict(boxstyle='round', 
                  facecolor='wheat', alpha=0.5))
    
    # Adjust layout for readability
    plt.tight_layout()
    
    # Save figure
    plt.savefig('sensor_analysis.png', dpi=150, bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    main()