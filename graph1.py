import json
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

with open("npm_top_500.json") as f:
    npm = json.load(f)
with open("pypi_top_500.json") as f:
    pypi = json.load(f)
with open("rust_top_500.json") as f:
    cargo = json.load(f)

npm_downloads = sorted([p["downloads"] for p in npm], reverse=True)
pypi_downloads = sorted([p["downloads"] for p in pypi], reverse=True)
cargo_downloads = sorted([p["downloads"] for p in cargo], reverse=True)

pink = "#FF00AA"  # HSL(311, 100%, 50%)

fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor("black")
ax.set_facecolor("black")

x_npm = range(1, len(npm_downloads) + 1)
x_pypi = range(1, len(pypi_downloads) + 1)
x_cargo = range(1, len(cargo_downloads) + 1)

ax.plot(x_npm, npm_downloads, color=pink, linewidth=1.7)
ax.plot(x_pypi, pypi_downloads, color=pink, linewidth=1.7, linestyle="--")
ax.plot(x_cargo, cargo_downloads, color=pink, linewidth=1.7, linestyle=":")

label_x = 500
ax.text(label_x, npm_downloads[label_x - 1] * 0.9, "npm",
        color="white", fontsize=11, fontweight="bold", va="bottom")
ax.text(label_x, pypi_downloads[label_x - 1] * 0.9, "PyPI",
        color="white", fontsize=11, fontweight="bold", va="bottom")
ax.text(label_x, cargo_downloads[label_x - 1] * 0.9, "Cargo",
        color="white", fontsize=11, fontweight="bold", va="bottom")

ax.set_xlabel("Packages", color="white", fontsize=13)
ax.set_ylabel("Downloads", color="white", fontsize=13)

ax.yaxis.set_major_locator(ticker.MultipleLocator(250_000_000))
ax.yaxis.set_major_formatter(ticker.FuncFormatter(
    lambda x, _: f"{x / 1e9:.2f}B" if x >= 1e9 else f"{x / 1e6:.0f}M"))
ax.set_ylim(bottom=0)

ax.set_xticks([1, 500])
ax.tick_params(axis="x", which="both", bottom=True, colors="white")

ax.tick_params(colors="white", which="major")
ax.spines["bottom"].set_color("white")
ax.spines["left"].set_color("white")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.grid(axis="y", which="major", color="white", alpha=0.15, linewidth=0.5)

plt.tight_layout()
plt.savefig("downloads_plot.png", dpi=150, facecolor="black")
plt.show()
