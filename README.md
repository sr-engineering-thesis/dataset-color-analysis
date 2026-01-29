# Color Distribution Analysis for Super-Resolution Datasets

This repository provides a set of scripts for analyzing pixel-level color distributions in super-resolution (SR) datasets. The tools are designed to aggregate per-color statistics from image datasets and derive summary metrics such as histograms and average color intensities.

## Overview

The analysis pipeline consists of two stages:

1. **Data aggregation** – Extracting and counting pixel color values from images and storing the results in CSV format.
2. **Analysis and visualization** – Computing statistics and generating visualizations based on the aggregated data.

## Requirements

Before running any scripts, install the required Python dependencies:

```bash
pip install opencv-python numpy pandas matplotlib tqdm
```

## Data Aggregation

To analyze a dataset, you must first generate a CSV file containing pixel color counts. This is done using the `aggregate_color_data.py` script:

```bash
python aggregate_color_data.py <DATASET_DIRECTORY> <OUTPUT_CSV>
```

* `<DATASET_DIRECTORY>`: Path to the directory containing dataset images.
* `<OUTPUT_CSV>`: Path where the generated CSV file will be saved.

Run this command separately for each dataset you wish to analyze.

## Expected Input Files

The analysis scripts assume the presence of the following CSV files, each generated using `aggregate_color_data.py` from the corresponding dataset:

* `q2rtx.csv`
* `div2k.csv`
* `realsr.csv`

Ensure these files are available in the expected location before running the analysis scripts.

## Analysis Scripts

* **`create_histogram.py`**
  Generates color distribution histograms based on the aggregated pixel data.

* **`calculate_average_intensity.py`**
  Computes average color intensity values for each dataset.

## Datasets

* **Q2RTX**: The Quake II RTX dataset is publicly available on Kaggle:
  [https://www.kaggle.com/datasets/maciejjk208/quake-rtx-v0-3/](https://www.kaggle.com/datasets/maciejjk208/quake-rtx-v0-3/)

Other datasets (e.g., DIV2K, RealSR) should be obtained from their respective official sources and processed in the same manner.
