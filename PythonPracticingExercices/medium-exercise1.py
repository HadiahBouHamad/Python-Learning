def three_sum(numbers):
    result = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            for k in range(j+1, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == 0:
                    triplet = sorted([numbers[i], numbers[j], numbers[k]])
                    if triplet not in result:
                        result.append(triplet)
    return result


numbers = [-1, 0, 1, 2, -1, -4]
print(three_sum(numbers))
        
    