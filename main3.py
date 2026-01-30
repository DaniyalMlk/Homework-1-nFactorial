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
    remaining = centerCapacities[:]  # Current remaining capacity
    package_count = [0] * n  # Packages processed by each center
    closed = [False] * n  # Track closed centers
    current_center = 0  # Current center to check
    
    for log in dailyLog:
        if log == "PACKAGE":
            # Find next available center with capacity
            while closed[current_center] or remaining[current_center] == 0:
                current_center = (current_center + 1) % n
                if current_center == 0:
                    # Completed rotation - reset all capacities
                    for i in range(n):
                        remaining[i] = centerCapacities[i]
            
            # Process package at current center
            remaining[current_center] -= 1
            package_count[current_center] += 1
        else:
            # CLOSURE <j> - close center j
            j = int(log.split()[1])
            closed[j] = True
    
    # Find center with most packages (highest index if tie)
    max_packages = max(package_count)
    result = -1
    for i in range(n):
        if package_count[i] == max_packages:
            result = i  # Keep updating to get highest index
    
    return result
