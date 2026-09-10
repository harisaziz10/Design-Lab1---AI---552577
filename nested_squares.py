"""
Nested Squares "Tunnel" Illusion.

A big outer square frame, with progressively smaller square outlines
nested inside it, each one scaled down toward a vanishing point that's
offset from the exact center -- which is what gives the illusion of a
square tunnel receding into the distance rather than perfectly
concentric squares.

Run: python nested_squares.py
Output: nested_squares.png
"""

import numpy as np
import matplotlib.pyplot as plt


def square_corners(cx, cy, half_size):
    """Return the 4 corners of an axis-aligned square (closed loop)."""
    return np.array([
        (cx - half_size, cy - half_size),
        (cx + half_size, cy - half_size),
        (cx + half_size, cy + half_size),
        (cx - half_size, cy + half_size),
        (cx - half_size, cy - half_size),
    ])


def draw_nested_squares(
    ax,
    outer_half_size=40,
    n_squares=18,
    shrink_ratio=0.82,
    vanish_offset=(0.06, -0.05),
    color="white",
    lw=2.0,
):
    """
    Draw n_squares square outlines, each shrink_ratio smaller than the
    last, moving from the outer square's center toward a vanishing
    point offset from center by `vanish_offset` (as a fraction of the
    outer half-size). Geometric shrinkage makes the squares bunch up
    closer together near the center, giving the tunnel-perspective look.
    """
    vx = vanish_offset[0] * outer_half_size
    vy = vanish_offset[1] * outer_half_size

    half = outer_half_size
    cx, cy = 0.0, 0.0

    for i in range(n_squares):
        corners = square_corners(cx, cy, half)
        ax.plot(corners[:, 0], corners[:, 1], color=color, linewidth=lw, solid_capstyle="butt")

        # Shrink the square and shift its center a bit toward the vanishing point
        half *= shrink_ratio
        cx = cx + (vx - cx) * (1 - shrink_ratio)
        cy = cy + (vy - cy) * (1 - shrink_ratio)


def plot_illusion(filename="nested_squares.png"):
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_facecolor("black")
    fig.patch.set_facecolor("black")

    draw_nested_squares(ax)

    ax.set_aspect("equal")
    ax.axis("off")
    margin = 45
    ax.set_xlim(-margin, margin)
    ax.set_ylim(-margin, margin)

    plt.tight_layout()
    plt.savefig(filename, dpi=200, facecolor="black")
    plt.close()


if __name__ == "__main__":
    plot_illusion()
    print("Saved nested_squares.png")
