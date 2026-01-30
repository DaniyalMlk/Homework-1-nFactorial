def solution(centerCapacities, dailyLog):
    """
    Find distribution center that processed the most packages.
    
    Args:
        centerCapacities: Array of max capacities for each center
        dailyLog: Array of operations ("PACKAGE" or "CLOSURE <j>")
    
    Returns:
        Index of center with most packages (highest index if tie)
    """
    n = len(centerCapacities)
    remaining = list(centerCapacities)  # Current remaining capacity
    package_count = [0] * n  # Packages processed by each center
    closed = [False] * n  # Track closed centers
    current_center = 0  # Current center to check
    
    for log in dailyLog:
        if log == "PACKAGE":
            # Find next available center with capacity
            # Track if we've done a reset to prevent infinite loop
            has_reset = False
            
            while closed[current_center] or remaining[current_center] == 0:
                current_center = (current_center + 1) % n
                if current_center == 0:
                    if has_reset:
                        # Already reset once, shouldn't happen if at least one center is operational
                        break
                    # Completed rotation - reset all capacities
                    for i in range(n):
                        remaining[i] = centerCapacities[i]
                    has_reset = True
            
            # Process package at current center (if found)
            if not closed[current_center] and remaining[current_center] > 0:
                remaining[current_center] -= 1
                package_count[current_center] += 1
        
        elif log.startswith("CLOSURE"):
            # CLOSURE <j> - close center j
            parts = log.split()
            if len(parts) >= 2:
                j = int(parts[1])
                if 0 <= j < n:
                    closed[j] = True
    
    # Find center with most packages (highest index if tie)
    max_packages = 0
    result = 0
    for i in range(n):
        if package_count[i] >= max_packages:
            max_packages = package_count[i]
            result = i
    
    return result
