import sys
def complex_cipher():
    strr=str(input('Enter the message you want encoded (numbers will not be encrypted): '))
    key= int(input('enter your encrytion key: '))
    cypt=[]
    final=''
    separ =input ('what would you like for non letters to be represented by: ')
    for char in strr:
        if ord(char)<65 or (ord(char)>90 and ord(char)<96):
            try: 
                int(char)
                cypt.append(char)
                
            except: 
                cypt.append(separ)
        
        elif char.upper() == char:

            if (ord(char)+key)>90:

                cypt.append(chr((ord(char))+key-26))

            else:

                cypt.append(chr((ord(char))+key))
        elif char.lower() == char:

            if (ord(char)+key)>122:
                # print (char)
                cypt.append(chr((ord(char))+key-26))

            else:
                # print (char)
                cypt.append(chr((ord(char))+key))
    for i in cypt:
        final+=i
    
    return final

# for nu in range(97,123):
# #     print(chr(nu))
def simple_cipher():
    strrr=str(input('Enter the message you want encoded: '))
    keyr= int(input('enter your encrytion key: '))
    cyptr=[]
    finalr=''
    strrr=strrr.upper()
    five=0
    for char in strrr:
        
        if (ord(char)+keyr)>90:

            cyptr.append(chr((ord(char))+keyr-26))
        elif (ord(char))>90 or (ord(char))<65:
            continue
        else:

            cyptr.append(chr((ord(char))+keyr))
    for x in cyptr:
        if five==5:
                finalr+= ' '
                finalr+=x
                five=0
        else:
                finalr+=x
                five+=1
    return finalr

print(simple_cipher())