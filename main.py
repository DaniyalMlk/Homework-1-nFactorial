def solution(diffs):
    """
    Calculate the highest rating ever and current rating.
    
    Starting rating is 1500.
    Apply each change from diffs array and track:
    - The maximum rating achieved at any point
    - The final (current) rating
    
    Args:
        diffs: Array of rating changes (positive or negative integers)
    
    Returns:
        Array with two values: [highest_rating_ever, current_rating]
    """
    initial_rating = 1500
    current_rating = initial_rating
    max_rating = initial_rating
    
    for diff in diffs:
        current_rating += diff
        max_rating = max(max_rating, current_rating)
    
    return [max_rating, current_rating]
