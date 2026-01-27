import cv2
import glob
import numpy as np
import tqdm
import matplotlib.pyplot as plt
import pandas as pd
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input", nargs="+", help="directories containing input images")
parser.add_argument("output", help="output csv filename")
args = parser.parse_args()
all_red = np.zeros((256,))
all_blue = np.zeros((256,))
all_green = np.zeros((256,))

all_files = []
for dirname in args.input:
    all_files += [name for name in glob.glob(f"{dirname}/*")]


for filename in tqdm.tqdm(all_files):
    # images are BGR
    image = cv2.imread(filename)
    if image is None:
        print("Failed to read the file")
        exit(1)
    blue, green, red = cv2.split(image)


    index, counts = np.unique(red.flatten(), return_counts=True)
    for i, c in zip(index, counts):
        all_red[i] += c
    index, counts = np.unique(green.flatten(), return_counts=True)

    for i, c in zip(index, counts):
        all_green[i] += c
    index, counts = np.unique(blue.flatten(), return_counts=True)

    for i, c in zip(index, counts):
        all_blue[i] += c

colors =  {
        "red": all_red,
        "blue": all_blue,
        "green": all_green,
        }
df = pd.DataFrame(colors)
df.to_csv(args.output)
print(f"Saved metrics to {args.output}")
