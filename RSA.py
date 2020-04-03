from math import gcd

# Getting the values of p and q
p = int(input('Enter the value of p: '))
q = int(input('Enter the value of q: '))

# Calculating n
n = p * q

# Calculating phi of N
phi_n = (p - 1) * (q - 1)

# Calculating e
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

# Displaying the output
print(f'Public Key: {{{n}, {e}}}')
print(f'Private Key: [{p}, {q}, {d}]')

while True:
    question = int(input('\nDo You wish to \n1. Implement RSA\n2. Implement Digital Signature\n3. Exit'))
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

    print(f'\n\t[CIPHERED]: {temp}')

    # Decryption
    deciphered_text = ''
    for character in ciphered_text:
        deciphered_text += character_space[(character ** d) % n]

    print(f'\n\t[DECIPHERED]: {deciphered_text}')
