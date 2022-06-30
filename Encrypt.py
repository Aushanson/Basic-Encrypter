plainText = input("""Enter a message:\n""")
shift = int(input("Enter the distance value:"))
cipherText = """"""
textLength = len(plainText)
for ch in range(0, textLength):
    Ascii = ord(plainText[ch])
    Ascii = Ascii + 1
    if Ascii > 90:
        Ascii - 26
    cipherText = cipherText + chr(Ascii)
print(cipherText)
with open('copy.txt', 'w') as wf:
    save_file = open('encrypt.txt', 'w')
    save_file.write(cipherText)
    wf.write(cipherText)
