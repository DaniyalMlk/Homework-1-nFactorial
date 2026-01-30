def solution(centerCapacities, dailyLog):
    n = len(centerCapacities)
    if n == 0:
        return 0
    
    remaining = list(centerCapacities)
    package_count = [0] * n
    closed = [False] * n
    current = 0
    
    for log in dailyLog:
        if log == "PACKAGE":
            for _ in range(n * 3):
                if not closed[current] and remaining[current] > 0:
                    remaining[current] -= 1
                    package_count[current] += 1
                    break
                
                current = (current + 1) % n
                
                if current == 0:
                    for i in range(n):
                        remaining[i] = centerCapacities[i]
        
        else:
            try:
                parts = log.split()
                if len(parts) >= 2:
                    j = int(parts[1])
                    if 0 <= j < n:
                        closed[j] = True
            except:
                pass
    
    max_packages = 0
    result = 0
    for i in range(n):
        if package_count[i] >= max_packages:
            max_packages = package_count[i]
            result = i
    
    return result
