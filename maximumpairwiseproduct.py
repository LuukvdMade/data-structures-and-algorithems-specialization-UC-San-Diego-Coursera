def maxpairwise(numbers):
    n = len(numbers)

    index1 = 1
    for i in range(n):
        if numbers[i] > numbers[index1]:
            index1 = i

    temp = numbers[index1]
    numbers[index1] = numbers[n-1]
    numbers[n-1] = temp
    
    index1 = 1

    for i in range(n - 2):
        if numbers[i] > numbers[index1]:
            index1 = i
    
    temp2 = numbers[index1]
    numbers[index1] = numbers[n-2]
    numbers[n-2] = temp2
    
    return numbers[n-2] * numbers[n-1]
    
inputnums = list(map(int, input().split()))
print(maxpairwise(inputnums))
