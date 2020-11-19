import os

def cek_palindrome(string):
    string.lower()
    x = 0
    y = len(string) - 1
    kondisi = 1

    while (x < y):
        if(string[x]==string[y]):
            x+=1
            y-=1
        else:
            kondisi = 0
            break
    return int(kondisi)

while True:
    os.system('cls')

    string = input('Masukkan kalimat ? ')

    if cek_palindrome(string) == 0:
        print(f'{string} Bukanlah Palindrome')
    else:
        print(f'{string} Merupakan Palindrome')
    
    while True:
        lanjut = input('Continue [y/n] ? ')
        if lanjut in ('y', 'n'):
            break
    
    if lanjut == 'n':
        break