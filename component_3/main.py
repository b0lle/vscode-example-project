from typing import Any
import numpy as np

def calculate_mean(array: np.ndarray) -> np.floating[Any]:
    """Calculate the mean of a numpy array."""
    return np.mean(array)

if __name__ == '__main__':
    mean = calculate_mean(np.array([1, 2, 3]))
    print(mean)
