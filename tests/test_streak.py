import sys
import os

# Add the parent directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from streak import longest_positive_streak

def test_empty_list():
    """Test that empty list returns 0"""
    assert longest_positive_streak([]) == 0

def test_all_positive():
    """Test list with all positive numbers"""
    assert longest_positive_streak([1, 2, 3]) == 3
    assert longest_positive_streak([1, 1, 1]) == 3

def test_with_negatives_and_zeros():
    """Test list with negatives and zeros that break streaks"""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_multiple_streaks():
    """Test list with multiple streaks to ensure longest is returned"""
    assert longest_positive_streak([1, 2, -1, 3, 4, 5, -2, 6, 7]) == 3

def test_no_positive_numbers():
    """Test list with no positive numbers"""
    assert longest_positive_streak([-1, -2, 0, -3]) == 0

def test_single_positive():
    """Test list with single positive number"""
    assert longest_positive_streak([5]) == 1
    assert longest_positive_streak([-5]) == 0

def test_mixed_streaks():
    """Test various streak scenarios"""
    assert longest_positive_streak([1, -1, 2, 3, -1, 4, 5, 6]) == 3
