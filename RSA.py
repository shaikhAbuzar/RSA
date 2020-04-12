from math import gcd

# Getting the values of p and q
p = int(input('Enter the value of p: '))
q = int(input('Enter the value of q: '))

# Calculating n
n = p * q
# print('n', n)

# Calculating phi of N
phi_n = (p - 1) * (q - 1)
# print('pn', phi_n)

# Calculating e
e_if = int(input('Would you mannualy like to enter e[y = 1 / n = 0]: '))
if e_if == 0:
    i = 2
    while gcd(i, phi_n) != 1:
        i += 1
    e = i
elif e_if == 1:
    e = int(input('Enter the value of e: '))
    if 1 < e < phi_n and gcd(e, phi_n) == 1:
        print(f'{e} is valid value of e')
    else:
        print(f'{e} is not a valid value for e')
else:
    print('invalid input for e\n finding e mannually')
    i = 2
    while gcd(i, phi_n) != 1:
        i += 1
    e = i

# Calculating d
d = 0
for k in range(1, 10):
    d = (1 + k * phi_n) / e
    if int(str(d - int(d))[2:]) == 0:
        d = int(d)
        break
# print(k)

# Displaying the output
print(f'Public Key: {{{n}, {e}}}')
print(f'Private Key: [{p}, {q}, {d}]')

while True:
    question = int(input('\nDo You wish to \n1. Implement RSA\n2. Implement Digital Signature\n3. Exit\nYour choice: '))
    if question == 2:
        e, d = d, e  # for implementing digital signature we interchange the bits
    elif question != 1:
        break

    # The character space
    character_space = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                       'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                       'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4',
                       '5', '6', '7', '8', '9', ' ', '?', ',', '@', '_', '$', '#', '!']

    # Get the message
    message = input('\n\t[INPUT] Enter the message: ')

    # Encryption
    ciphered_text = []
    for character in message:
        value = character_space.index(character)
        ciphered_text.append((value ** e) % n)

    temp = ''
    for cipher in ciphered_text:
        temp += str(cipher)

    if question == 2: content = 'DIGITAL SIGNATURE'
    else: content = 'CIPHERED'
    print(f'\n\t[{content}]: {temp}')

    # Decryption
    deciphered_text = ''
    for character in ciphered_text:
        deciphered_text += character_space[(character ** d) % n]

    print(f'\n\t[DECIPHERED]: {deciphered_text}')
