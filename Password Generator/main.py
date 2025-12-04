import random

letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]
numbers = [
    '0','1','2','3','4','5','6','7','8','9'
]
symbols = [
    '!','@','#','$','%','^','&','*','(',')',
    '-','_','=','+',
    '[' ,']','{','}','\\',
    '|',':',';','"',"'",'<','>',',','.','?','/',
    '`','~'
]

print("Welcome to the password generator")

number_letters = int(input("How many letters do you want in your password?\n"))
number_numbers = int(input("How many numbers do you want in you password?\n"))
number_symbols = int(input("How many symbols do you want in you password?\n"))

result = []

for letter in range(0, number_letters):
    result.append(random.choice(letters))

for number in range(0, number_numbers):
    result.append(random.choice(numbers))

for symbol in range(0, number_symbols):
    result.append(random.choice(symbols))

# to change the order of elements in the list
random.shuffle(result)

# to put the list elements in one string
print(f"Your password is: {"".join(result)}")
