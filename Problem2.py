def generate_series(a: int):
    series = []
    for i in range(a):
        series.append(2 * i + 1)  
    return series

print(generate_series(1))  
print(generate_series(2))  
print(generate_series(3))  
print(generate_series(4))  
print(generate_series(5)) 