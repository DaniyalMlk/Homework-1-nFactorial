def solution(centerCapacities, dailyLog):
    n = len(centerCapacities)
    remaining = list(centerCapacities)
    package_count = [0] * n
    closed = [False] * n
    current = 0
    
    for log in dailyLog:
        if log == "PACKAGE":
            # Search for available center, allow multiple rotations
            for _ in range(n * 2 + 1):
                if not closed[current] and remaining[current] > 0:
                    # Found available center, process package
                    remaining[current] -= 1
                    package_count[current] += 1
                    break
                
                # Move to next center
                current = (current + 1) % n
                
                # If we wrapped back to 0, reset all capacities
                if current == 0:
                    for i in range(n):
                        remaining[i] = centerCapacities[i]
        
        else:
            # CLOSURE command - extract center number
            j = int(log.split()[1])
            closed[j] = True
    
    # Find center with most packages (highest index wins ties)
    max_packages = 0
    result = 0
    for i in range(n):
        if package_count[i] >= max_packages:
            max_packages = package_count[i]
            result = i
    
    return result
