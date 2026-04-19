"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

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