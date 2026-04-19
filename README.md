# Sensor Data Visualization

A Python script that generates synthetic temperature sensor data and produces publication-quality visualizations comparing two sensors over time.

## Installation

1. Activate the `ece105` conda environment:
   ```bash
   conda activate ece105
   ```

2. Install required dependencies using conda or mamba:
   ```bash
   conda install numpy matplotlib
   ```
   or
   ```bash
   mamba install numpy matplotlib
   ```

## Usage

Run the script with the following command:
```bash
python generate_plots.py
```

The script will generate synthetic sensor data, create visualizations, and save the output.

## Example Output

The script produces a single PNG file (`sensor_analysis.png`) containing three synchronized plots:

1. **Scatter Plot**: Shows individual temperature readings from both sensors over the 0-10 second time window. Blue points represent Sensor A (mean ~25°C) and orange points represent Sensor B (mean ~27°C).

2. **Histogram**: Displays overlaid temperature distributions for both sensors with 30 bins and semi-transparent colors to show overlap. Vertical dashed lines indicate each sensor's mean temperature.

3. **Box Plot**: Side-by-side box plots comparing the distribution statistics (median, quartiles, and outliers) for each sensor. A horizontal dashed line shows the overall mean across both sensors.

## AI Tools Used and Disclosure

[Placeholder: Describe any AI tools, models, or large language models used in developing this script, such as GitHub Copilot or similar AI assistants. Include details about which parts of the code were generated or assisted by AI.]