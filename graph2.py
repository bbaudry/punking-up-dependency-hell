import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import colorsys

def hsl_to_hex(h, s, l):
    r, g, b = colorsys.hls_to_rgb(h / 360, l / 100, s / 100)
    return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"

pink = hsl_to_hex(311, 100, 50)
green = hsl_to_hex(126, 100, 41)
white = "#ffffff"

categories = ["Direct", "Transitive"]
bloated =  [29.9, 78.3]
used =     [64.3, 12.8]
others =   [5.8,  8.9]

fig, ax = plt.subplots(figsize=(10, 4))
fig.patch.set_facecolor("black")
ax.set_facecolor("black")

bar_height = 0.5
y_pos = [1, 0]

for i, cat in enumerate(categories):
    y = y_pos[i]
    left = 0

    ax.barh(y, bloated[i], height=bar_height, left=left, color=pink,
            edgecolor=white, linewidth=0.8)
    if bloated[i] > 4:
        ax.text(left + bloated[i] / 2, y, f"{bloated[i]}%",
                ha="center", va="center", color="white", fontsize=10, fontweight="bold")
    left += bloated[i]

    ax.barh(y, used[i], height=bar_height, left=left, color=green,
            edgecolor=white, linewidth=0.8)
    if used[i] > 4:
        ax.text(left + used[i] / 2, y, f"{used[i]}%",
                ha="center", va="center", color="white", fontsize=10, fontweight="bold")
    left += used[i]

    ax.barh(y, others[i], height=bar_height, left=left, color=white,
            edgecolor=white, linewidth=0.8)
    if others[i] > 4:
        ax.text(left + others[i] / 2, y, f"{others[i]}%",
                ha="center", va="center", color="black", fontsize=10, fontweight="bold")
    else:
        ax.text(left + others[i] / 2, y, f"{others[i]}%",
                ha="center", va="center", color="white", fontsize=8, fontweight="bold")

ax.set_yticks(y_pos)
ax.set_yticklabels(categories, color="white", fontsize=12)
ax.set_xlim(0, 100)
ax.set_xticks([0, 25, 50, 75, 100])
ax.set_xticklabels(["0%", "25%", "50%", "75%", "100%"], color="white", fontsize=11)

# ax.set_xlabel("Percentage of occurrence", color="white", fontsize=13)
ax.set_ylabel("Dependency type", color="white", fontsize=13)

ax.tick_params(colors="white", which="both")
ax.spines["bottom"].set_color("white")
ax.spines["left"].set_color("white")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

patch_bloated = mpatches.Patch(facecolor=pink, edgecolor=white, linewidth=0.8,
                               label="□ bloated")
patch_used = mpatches.Patch(facecolor=green, edgecolor=white, linewidth=0.8,
                            label="□ used")
patch_others = mpatches.Patch(facecolor=white, edgecolor=white, linewidth=0.8,
                              label="others")

legend = ax.legend(handles=[patch_bloated, patch_used, patch_others],
                   loc="upper center", bbox_to_anchor=(0.5, 1.25),
                   ncol=3, facecolor="black", edgecolor="white", fontsize=11)
legend.get_title().set_color("white")
for text in legend.get_texts():
    text.set_color("white")

plt.tight_layout()
plt.savefig("graph_new.png", dpi=150, facecolor="black", bbox_inches="tight")
plt.show()
