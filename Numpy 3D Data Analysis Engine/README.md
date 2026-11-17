# NumPy 3D Multidimensional Data Analysis Engine

## Project Overview

The **NumPy 3D Multidimensional Data Analysis Engine** is a Python-based data analysis project that uses NumPy to process, analyze, and visualize multidimensional environmental sensor data.

The project simulates readings from multiple monitoring stations over 30 days and performs statistical analysis, advanced array operations, matrix computations, and data visualization.

## Dataset Information

The dataset contains simulated environmental readings from 5 monitoring stations over 30 days.

| Attribute | Details |
|---|---|
| Monitoring Stations | 5 |
| Duration | 30 Days |
| Measurements | 4 |
| Total Readings | 600 |
| NumPy Array Shape | `(5, 30, 4)` |

### Measurements

1. Temperature (°C)
2. Humidity (%)
3. Pressure (hPa)
4. Wind Speed

## Features

### 1. Dataset Generation
- Generate synthetic environmental sensor data.
- Combine multiple measurement arrays using `np.stack()`.
- Save and load datasets using NumPy.

### 2. Multidimensional Array Operations
- Work with 3D NumPy arrays.
- Understand array dimensions and shapes.
- Perform indexing and slicing operations.

### 3. Advanced Indexing
- Fancy indexing.
- Boolean indexing.
- Conditional filtering.
- Identify temperature readings above specified thresholds.

### 4. Broadcasting and Vectorization
- Perform broadcasting operations.
- Convert Celsius temperatures to Fahrenheit.
- Normalize and standardize temperature data.
- Apply vectorized calculations.

### 5. Statistical Analysis
- Calculate mean, median, standard deviation, variance, minimum, and maximum.
- Calculate percentiles and interquartile range (IQR).
- Analyze temperature and humidity correlation.
- Identify hottest and coldest stations and days.
- Detect statistical outliers.

### 6. Linear Algebra
- Matrix transposition.
- Matrix multiplication.
- Determinants and inverse matrices.
- Eigenvalues and eigenvectors.

### 7. Data Visualization
- Line charts.
- Bar charts.
- Scatter plots.
- Histograms.
- 3D scatter plots.

### 8. Integration and Testing
- Create reusable analysis functions.
- Test analysis functions.
- Integrate functions into a main execution script.
- Generate a consolidated analysis report.

## Project Structure

```text
NumPy-3D-Data-Analysis-Engine/
│
├── datasets/
│   └── sensor_data.npy
│
├── src/
│   └── analysis.py
│
├── visualizations/
│   ├── temperature_by_day.png
│   ├── average_temperature_by_station.png
│   ├── temperature_vs_humidity.png
│   ├── temperature_histogram.png
│   └── 3d_temperature_distribution.png
│
├── 01_Dataset_Generation.py
├── 02_Multidimensional_Arrays.py
├── 03_Advanced_Indexing.py
├── 04_Broadcasting_Vectorization.py
├── 05_Statistical_Analysis.py
├── 06_Linear_Algebra.py
├── 07_3D_Visualization.py
├── 08_Test_Analysis.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Technologies Used

- Python
- NumPy
- Matplotlib
- VS Code
- Git and GitHub

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/NumPy-3D-Data-Analysis-Engine.git
```

Navigate to the project directory:

```bash
cd NumPy-3D-Data-Analysis-Engine
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## How to Run

Run the scripts in the following order:

**1. Generate the dataset**

```bash
python 01_Dataset_Generation.py
```

**2. Explore and analyze the dataset**

Run the numbered scripts from `02` through `07` to explore the NumPy operations, statistical analysis, linear algebra, and visualizations.

**3. Test the analysis functions**

```bash
python 08_Test_Analysis.py
```

**4. Run the integrated analysis engine**

```bash
python main.py
```

## Visualizations

The project generates the following visualizations:

- Temperature trends across 30 days.
- Average temperature by monitoring station.
- Temperature versus humidity relationship.
- Temperature distribution histogram.
- 3D temperature distribution across stations and days.

The generated charts are stored in the `visualizations/` directory.

## Learning Outcomes

Through this project, I gained practical experience in:

- Working with 3D NumPy arrays.
- Multidimensional indexing and slicing.
- Broadcasting and vectorization.
- Statistical analysis using NumPy.
- Matrix operations and linear algebra.
- Data visualization using Matplotlib.
- Building reusable Python functions.
- Testing and integrating a data analysis project.

## Author

**Jiss Philip**

GitHub: https://github.com/jiss123-abc

