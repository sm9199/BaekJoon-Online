# 크로아티아 알파벳

cro_alphabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cro_alpha = input()

for i in range(len(cro_alphabet)):
    cro_alpha = cro_alpha.replace(cro_alphabet[i], chr(65+i))


print(len(cro_alpha))
