This repository contains scripts used to analyze color distribution of SR datasets.

Before running any of these scripts, install dependencies:
```
pip install opencv-python numpy pandas matplotlib tqdm
```

To analyze a dataset, first you need to create `*.csv` files contain pixel color counts using:
```
python aggregate_color_data.py DATASET_DIRECTORY OUTPUT_CSV
```
Analysis scripts expect three input files:
- `q2rtx.csv`
- `div2k.csv`
- `realsr.csv`
created using `aggregate_color_data.py` from corresponding datasets.

`create_histogram.py` is used to create color histogram.

`calculate_average_intensity.py` is used to create average color intensity values.
