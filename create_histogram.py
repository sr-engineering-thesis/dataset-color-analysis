import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def load_dataset_colors (name):
    colors = pd.read_csv(name)
    all_red = colors['red'].to_numpy()
    all_red = all_red / np.sum(all_red)
    all_blue = colors['blue'].to_numpy()
    all_blue = all_blue / np.sum(all_blue)
    all_green = colors['green'].to_numpy()
    all_green = all_green / np.sum(all_green)
    return all_red, all_green, all_blue


fig = plt.figure(constrained_layout = True )

subfigs = fig.subfigures(nrows=3, ncols=1)
subfigs = [s for s in subfigs]
def visualize_dataset(dataset, loc, title):
    color_values = np.array(range(256))
    subfig = subfigs[loc]
    subfig.suptitle(title, fontsize=22)
    axs = subfig.subplots(1, 3, sharex=True, sharey=True)
    for ax, y, color in zip(axs, load_dataset_colors(dataset), ["red", "green", "blue"]):
        ax.bar(color_values, y, width=1.00, color=color, edgecolor = color)
        ax.set_ylim(0.0000001,0.1)
        ax.set_xticks([0, 127, 255])
        ax.set_yticks([0, 0.05, 0.1])
        ax.tick_params(axis="both", labelsize=16)

visualize_dataset("./q2rtx.csv", 0, "Quake2RTX")
visualize_dataset("./div2k.csv", 1, "RealSR")
visualize_dataset("./realsr.csv", 2, "Div2K")


plt.rcParams.update({
    "font.size": 20
})
fig.supxlabel("Intensity", fontsize=20)
fig.supylabel("Frequency", fontsize=20)
fig.set_size_inches(12, 9)
plt.savefig("final.pdf")
