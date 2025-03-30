import random


def generate_random_password():
    __alpha="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ"
    __nums="0123456789"
    __symbols="!@#$%^&*?|"
    __temp_pass_holder=""
    
    for i in range(3):
        __temp_pass_holder+=__alpha[random.randrange(len(__alpha)-1)]
        __temp_pass_holder+=__nums[random.randrange(len(__nums)-1)]
        __temp_pass_holder+=__symbols[random.randrange(len(__symbols)-1)]
    __temp_list=list(__temp_pass_holder)
    random.shuffle(__temp_list)
    return ''.join(__temp_list)