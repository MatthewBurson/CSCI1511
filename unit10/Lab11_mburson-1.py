import pytest

def normalize_rotation(degrees):
    """
    Normalizes a rotation angle to be within the range [0, 360).

    Args:
        degrees: The rotation angle in degrees.

    Returns:
        The normalized rotation angle in degrees.
    """
    if not isinstance(degrees, (int, float)):
        raise TypeError("Input must be a numeric value.")
    
    return degrees % 360

def test_normalize_rotation_100():
    assert normalize_rotation(100) == 100

def test_normalize_rotation_460():
    assert normalize_rotation(460) == 100

def test_normalize_rotation_negative_100():
    assert normalize_rotation(-100) == 260

def test_normalize_rotation_non_numeric():
    with pytest.raises(TypeError):
        normalize_rotation("abc")

def test_normalize_rotation_float():
    assert normalize_rotation(720.5) == 0.5
    assert normalize_rotation(360.0) == 0.0
    assert normalize_rotation(-10.5) == 349.5