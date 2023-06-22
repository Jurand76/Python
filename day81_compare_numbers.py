def compare_numbers(a, b):
    epsilon = 1e-9
    if(abs(a-b)<epsilon):
        return True
    else:
        return False
    
first = 0.3
second = 0.2
print(compare_numbers(first, second))