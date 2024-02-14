import random


def make_verification_code():
    verification_code = ''
    for x in range(16):
        verification_code += random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
    return verification_code

