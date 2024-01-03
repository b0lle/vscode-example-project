from component_3.main import calculate_mean
import numpy as np


def test_calculate_mean():
    array = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    result = calculate_mean(array)
    assert result == 3.0
