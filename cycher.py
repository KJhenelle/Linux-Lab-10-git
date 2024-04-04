import sys
def cipher():
    strr=str(input('Enter the message you want encoded: '))
    key= int(input('enter your encrytion key: '))
    cypt=[]
    final=''
    for char in strr:
        if char.upper == char:
            if (ord(char)+key)>90:
                print (char)
                cypt.append(chr((ord(char))+key-26))

            else:
                print (char)
                cypt.append(chr((ord(char))+key))
        elif char.lower == char:
            if (ord(char)+key)>122:
                print (char)
                cypt.append(chr((ord(char))+key-26))

            else:
                print (char)
                cypt.append(chr((ord(char))+key))
    for i in cypt:
        final+=i
    print (final)
    return cypt

for nu in range(97,123):
    print(chr(nu))
# print(cipher())