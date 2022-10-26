#Password Generator Project
from operator import concat, contains
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

f_letters = []
for number in range(1, nr_letters + 1):
    f_letters.append(letters[random.randint(0, len(letters) - 1)])

f_symbols = []
for number in range(1, nr_symbols + 1):
    f_symbols.append(symbols[random.randint(0, len(symbols) - 1)])

f_numbers = []
for number in range(1, nr_numbers + 1):
    f_numbers.append(numbers[random.randint(0, len(numbers) - 1)])

f_pass = [*f_letters, *f_symbols, *f_numbers]
random.shuffle(f_pass)

ran_pass = "".join(f_pass)
print(f"Your password is {ran_pass}")