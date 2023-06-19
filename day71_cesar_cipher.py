import requests
url = 'https://zerotojunior.dev/cezar.txt' # url do odczytu treści

# funkcja zwracająca przesunięty znak - wejście: znak, wzorzec dekodowania, przesunięcie
def move_char(input_char, decode_pattern, iteration):
    pos = decode_pattern.index(input_char)
    length = len(decode_pattern)
    new_position = pos + iteration
    if new_position >= length:
        new_position = new_position - length
    return decode_pattern[new_position]

# odczyt zawartości url
response = requests.get(url)

# sprawdzenie poprawności odczytu - jesli nie pobrano zawartości - zatrzymanie programu
if response.status_code == 200:
    text = response.content.decode('utf-8', errors='ignore')
    print("Zawartosc odczytana przed dekodowaniem:")
    print(text)
else:
    print("Blad odczytu URL!")
    exit()

print("Zawartość po dekodowaniu:")

text_decoded = ''
text_final = ''
count_e_max = 0
text_length = len(text)

small = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
large = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ"

for i in range(1, len(small)):
  for char in text:
    if char in text:
      if char in small:
        text_decoded = text_decoded + move_char(char, small, i)    # dekodowanie małych liter
      elif char in large:
        text_decoded = text_decoded + move_char(char, large, i)    # dekorowanie dużych liter
      else:
        text_decoded = text_decoded + char                         # jeśli znak nie jest literą - zostaw jak jest
  
  count_e = text_decoded.count('e')                                # liczenie wystąpień litery e
  
  if count_e > count_e_max:
     text_final = text_decoded
     count_e_max = count_e
  text_decoded = ''

print(text_final)

