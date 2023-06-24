def get_min_number_of_operations(a: list[int]) -> int:
    count = 0
    start = 0
    end = len(a) - 1

    while start <= end:
        while start <= end and a[start] >= 0:
            start += 1
        
        while start <= end and a[end] >= 0:
            end -= 1
        
        if start <= end:
            count += 1
            for i in range(start, end+1):
                a[i] = -a[i]
    
    return count