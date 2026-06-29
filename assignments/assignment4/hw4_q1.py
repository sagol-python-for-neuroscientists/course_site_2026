import numpy as np
import matplotlib.pyplot as plt


def mandel(
    n: int,
    thresh: float = 50.0,
    xlims: np.ndarray = np.array([-2, 1]),
    nx: int = 1500,
    ylims: np.ndarray = np.array([-1.5, 1.5]),
    ny: int = 1500,
) -> np.ndarray:
    """Computes the Mandelbrot fractal on some given set of numbers."""
    
    # Generating the 2D Complex Spatial Coordinates
    x = np.linspace(xlims[0], xlims[1], nx)
    y = np.linspace(ylims[0], ylims[1], ny)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    
    # Initializing Vectorized Math Trackers
    Z = np.zeros_like(C) # Allocates memory arrays to track pixel values
    mask = np.ones(C.shape, dtype=bool) # initializes a Boolean grid of True entries to keep track of which coordinates have not yet escaped past the absolute boundaries

    # Executes the mathematical sequence across the entire landscape simultaneously
    for _ in range(n):
        Z[mask] = Z[mask] ** 2 + C[mask]
        mask &= np.abs(Z) < thresh

    # Transforms the abstract true/false map into a concrete binary image array
    return mask.astype(int)  # Just return the binary image


# # test

# if __name__ == "__main__":
#     img = mandel(n=100)

#     plt.imshow(img, extent=[-2, 1, -1.5, 1.5], cmap="gray")
#     plt.xlabel("Re")
#     plt.ylabel("Im")
#     plt.title("Mandelbrot Set")
#     plt.savefig(
#         "mandelbrot_Gaia.png", dpi=300, bbox_inches="tight"
#     )  # ← customized name
#     plt.show()
