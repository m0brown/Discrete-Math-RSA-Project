import math

# Takes input and makes list of integers
d_list = [int(item) for item in input("Enter the message to be decrypted: ").split(' ')]

decrypted_list_short = []
decrypted_list_long = []

message = []
space = '32'
period = '27'
comma = '28'
question = '29'
exclamation = '30'

p = 3
q = 11
e = 3
d = 7

n = p * q

# Outputs a string
def decrypt(c):
    global decrypted_list_long
    en = math.pow(c, d)
    m = en % n
    m = int(m)
    decrypted_list_short.append("%02d" % m)
    decrypted_list_long = [' '.join(decrypted_list_short)]
    return m

for item in d_list:
    m = decrypt(item)

for item in decrypted_list_short:
    if item == space:
        message.append(' ')
    elif item == period:
        message.append('.')
    elif item == comma:
        message.append(',')
    elif item == question:
        message.append('?')
    elif item == exclamation:
        message.append('!')
    else:
        letter = chr(int(item) + 96)
        letter = letter.upper()
        message.append(letter)

print("Original Message is: ", *d_list)
print('Decrypted Message numbers: ', *decrypted_list_long)
print('Secret message: ', ''.join(message))
