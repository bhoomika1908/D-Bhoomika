def count_multiples(numbers: list):
    result = {}
    for i in range(1, 10): 
        count = 0
        for num in numbers:
            if num % i == 0:
                count += 1
        result[i] = count
    return result


numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
print(count_multiples(numbers))

