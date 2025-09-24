def generate_series(a: int):
    series = []
    length = (a + 1) // 2
    for i in range(length):
        series.append(2 * i + 1)
    return series

print(generate_series(1))  
print(generate_series(2)) 
print(generate_series(3))  
print(generate_series(4))  
print(generate_series(5))  
print(generate_series(6))  
