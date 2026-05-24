import random
import string
digits = string.digits
print("".join(random.choice(digits) for _ in range(6)))

# def Generate_otp():
#     otp = random.randint(100000,99999)
#     return otp
# result = Generate_otp()
# print("6 Digit otp is:",result)
# print(type(result))
# print(Generate_otp())