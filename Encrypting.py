import math

word = input('Phrase to be encrypted: ')
word = word.lower()
wl = []
space = 32
period = 27
comma = 28
question = 29
exclamation = 30
for letter in word:
    if letter == ' ':
        wl.append(space)
    elif letter == '.':
        wl.append(period)
    elif letter == ',':
        wl.append(comma)
    elif letter == '?':
        wl.append(question)
    elif letter == '!':
        wl.append(exclamation)
    else:
        wl.append(ord(letter) - 96)
print('Phrase input to numbers: ', *wl)

encrypt_list_short = []
encrypt_list_long = []

p = 3
q = 11
e = 3

n = p * q


def encrypt(me):
    global encrypt_list_long
    en = math.pow(me, e)
    c = en % n
    c = int(c)
    encrypt_list_short.append("%02d" % c)
    encrypt_list_long = [' '.join(encrypt_list_short)]
    return c


# run function on int list
for item in wl:
    c = encrypt(item)


print('Encrypted phrase: ', *encrypt_list_long)

