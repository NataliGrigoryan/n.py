import random

# chars = "~!@#$%^&*()_+№?*./*<>qwertyuiop[]asdfghjkl;'zxcvbnm,./`"

def pass_generator(len_):
    chars = "~!@#$%^&*()_+№?*./*<>qwertyuiop[]asdfghjkl;'zxcvbnm,./`"
    # num = int(input("enter num"))
    password = ''
    while True:
        for i in chars:
            password += random.choice(chars)
            if len(password) == len_:
                yield password
                password = ''

p_1 = pass_generator(6)

print(next(p_1))
print(next(p_1))
print(next(p_1))
print(next(p_1))
print(next(p_1))
print(next(p_1))
