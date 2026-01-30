def solution(finish, scooters):
    """
    Calculate total distance traveled on scooters.
    
    Algorithm:
    1. From current position, walk to nearest scooter to the right (or at current position)
    2. Ride scooter up to 10 points toward finish
    3. Repeat until reaching finish or no more scooters available
    
    Args:
        finish: End point of the street (integer)
        scooters: Array of scooter positions
    
    Returns:
        Total distance traveled on scooters
    """
    total_scooter_distance = 0
    current_position = 0
    
    # Use a set for efficient lookup and removal
    available_scooters = set(scooters)
    
    while current_position < finish:
        # Find nearest scooter at or to the right of current position
        nearest_scooter = None
        for pos in available_scooters:
            if pos >= current_position:
                if nearest_scooter is None or pos < nearest_scooter:
                    nearest_scooter = pos
        
        if nearest_scooter is None:
            # No scooters available, walk to finish
            break
        
        # Walk to the scooter and pick it up
        current_position = nearest_scooter
        available_scooters.remove(nearest_scooter)
        
        # Ride the scooter up to 10 points or until finish
        ride_distance = min(10, finish - current_position)
        current_position += ride_distance
        total_scooter_distance += ride_distance
    
    return total_scooter_distance
