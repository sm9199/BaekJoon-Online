# 다이얼

alphabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
num_word = input()
time = 0

for i in range(len(num_word)):
    for j in alphabet:
        if num_word[i] in j:
            time += alphabet.index(j) + 3
print(time)