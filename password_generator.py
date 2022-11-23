import random
import json

# chars = "~!@#$%^&*()_+№?*./*<>qwertyuiop[]asdfghjkl;'zxcvbnm,./`"

# def pass_generator(len_):
#     chars = "~!@#$%^&*()_+№?*./*<>qwertyuiop[]asdfghjkl;'zxcvbnm,./`"
#     # num = int(input("enter num"))
#     password = ''
#     while True:
#         for i in chars:
#             password += random.choice(chars)
#             if len(password) == len_:
#                 yield password
#                 password = ''
#
# p_1 = pass_generator(6)
#
# print(next(p_1))
# print(next(p_1))
# print(next(p_1))
# print(next(p_1))
# print(next(p_1))
# print(next(p_1))
# print(next(p_1))
# print(next(p_1))
# print(next(p_1))
# print(next(p_1))
# print(next(p_1))
# print(next(p_1))


#ex2
# class Generator:
#     def __init__(self, file):
#         self.file = file
#
#     def download_citation(self):
#         with open(self.file) as f:
#             data = json.load(f)
#             for i in data:
#                  return data
#
#     def generator_citation(self):
#         for i in data:
#             cit = random.choice(data)
#             yield cit
#             cit = ''
#
# c_1 = Generator("new.json")
# print(c_1.generator_citation())
# print(c_1.download_citation())

def generator_citation(file):
    with open(file) as f:
        data = json.load(f)
        for i in data.values():
            cit = i
            yield cit
            cit = ''

c_1 = generator_citation("new.json")
# print(next(c_1))

for i in c_1:
    print(i)

try:
    print(next(c_1))
except StopIteration:
    print("you've got all the possible options")

# print(next(c_1))
