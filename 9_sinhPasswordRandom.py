#Way 1:
'''
import random

DIGITS = ['0','1','2','3','4','5','6','7','8','9']

LOWER_CHARACTER = ['a','b','c','d','e','f','g','h',
                    'i','j','k','l','m','n','o','p','q',
                    'r','s','t','u','v','w','x','y','z']

UPPER_CHARACTER = ['A','B','C','D','E','F','G','H',
                    'I','J','K','L','M','N','O','P','Q',
                    'R','S','T','U','V','W','X','Y','Z']

SYMBOLS = ['!','@','#','$','%','^','&','*','(',')','-','_',
            '+','=','{','}','[',']',':',';','"',"'",'<','>',
            ',','.','?','/','\\','~','`']

rand_digit = random.choice(DIGITS)
rand_lower = random.choice(LOWER_CHARACTER)
rand_upper = random.choice(UPPER_CHARACTER)
rand_symbol = random.choice(SYMBOLS)
temp_password = [rand_digit,rand_lower,rand_upper,rand_symbol]

MAX_LEN = random.randint(8, 20)
COMBINED_LIST = DIGITS + UPPER_CHARACTER + LOWER_CHARACTER + SYMBOLS
for i in range(MAX_LEN):
    temp_password.append(random.choice(COMBINED_LIST))

random.shuffle(temp_password)
password = ""
for i in temp_password:
        password += i

print("Password generated: "+password)
'''


#Way 2: useful
import string, random

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation

def passwordLength():
    return int(input("Enter password length = "))

def getPassword(length):
    password = f"{LETTERS} {NUMBERS} {PUNCTUATION}"
    password = list(password)
    random.shuffle(password)
    randomPassword = random.choices(password, k=length)
    return ''.join(randomPassword)

def main():
    length = passwordLength()
    print(getPassword(length))

if __name__ == "__main__":
    main()
