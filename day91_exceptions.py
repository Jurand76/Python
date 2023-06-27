class NegativeNumberException(Exception):
    pass

def check_number(number):
    if number < 0:
        raise NegativeNumberException('Jeden z parametrów jest liczbą mniejszą od 0')

def divide(a, b):
    
    result = None
    try:
        self_a = int(a)
        self_b = int(b)
    except TypeError as e:
        print(f"Jeden z parametrów nie jest liczbą. Błąd: {e}")
        return result
        
    try:
        check_number(a)
        check_number(b)
    except NegativeNumberException as e:
        print(f'Blad: {e}')
        return result

    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Próba dzielenia przez zero") 

    return result

print(divide(-8,3))



