def longest_positive_streak(nums: list[int]) -> int:
    """
    Return the length of the longest run of consecutive values strictly greater than 0.
    
    Args:
        nums: List of integers
        
    Returns:
        int: Length of the longest consecutive positive streak
    """
    if not nums:
        return 0
    
    max_streak = 0
    current_streak = 0
    
    for num in nums:
        if num > 0:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0
    
    return max_streak
