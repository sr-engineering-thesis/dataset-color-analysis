import pandas as pd
import numpy as np
import math


def calculate_average_colors (name):
    colors = pd.read_csv(name)
    def parse_color(color):
        all_color = colors[color].to_numpy()
        mean_color_sum = 0
        for i in range(256):
            mean_color_sum += all_color[i] * i
        color_mean = mean_color_sum/ np.sum(all_color)
        std_sum = 0
        for i in range(256):
            std_sum += ((color_mean - i) * (color_mean - i)) * all_color[i]
        color_std = math.sqrt(std_sum/ np.sum(all_color))
        return color_mean, color_std
    return parse_color("red"), parse_color("green"), parse_color("blue")

def print_average_colors(red, green, blue):
    
    print(f"red: {red[0]:.3f} ± {red[1]:.3f}")
    print(f"green: {green[0]:.3f} ± {green[1]:.3f}")
    print(f"blue: {blue[0]:.3f} ± {blue[1]:.3f}")

print(f"===Q2RTX===")
print_average_colors(*calculate_average_colors("./q2rtx.csv"))
print(f"===Div2K===")
print_average_colors(*calculate_average_colors("./div2k.csv"))
print(f"===RealSR===")
print_average_colors(*calculate_average_colors("./realsr.csv"))
# according to pytorch
print(f"===ImageNet===")
imagenet_red   = np.array([0.485, 0.229]) * 255
imagenet_green = np.array([0.456, 0.224]) * 255
imagenet_blue  = np.array([0.406, 0.225]) * 255
print_average_colors(imagenet_red, imagenet_green, imagenet_blue)
