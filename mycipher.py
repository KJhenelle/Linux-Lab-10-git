import sys
def complex_cipher():
    correct=0
    strr=str(input('Enter the message you want encoded (numbers will not be encrypted): '))
    try:
        key=int(sys.argv[1])
    except:
        pass
    try:
        keyr+=1
        keyr-=1
    except:
        while correct == 0:
            try:
                key= int(input('enter your encrytion key: '))
                correct=1
            except:
                pass
    cypt=[]
    final=''
    separ =input ('what would you like for non letters to be represented by: ')
    if separ == 'None':
        separ=' '
    for char in strr:
        if ord(char)<65 or (ord(char)>90 and ord(char)<96):
            try: 
                int(char)
                cypt.append(char)
                
            except: 
                cypt.append(separ)
        
        elif char.upper() == char:

            if (ord(char)+key)>90:

                tabs=(ord(char)+key)
                while tabs>90:
                    tabs-=26
                cypt.append(chr(tabs))
                

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



def simple_cipher():
    strrr=str(input('Enter the message you want encoded: '))
    correct=0
    try:
        keyr=int(sys.argv[1])
    except:
        pass
    try:
        keyr+=1
        keyr-=1
    except:
        while correct == 0:
            try:
                keyr= int(input('enter your encrytion key: '))
                correct=1
            except:
                pass
    
    cyptr=[]
    finalr=''
    strrr=strrr.upper()
    five=0
    for char in strrr:
        
        if (ord(char)+keyr)>90:
            tabs=(ord(char)+keyr)
            while tabs>90:
                tabs-=26
            cyptr.append(chr(tabs))
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
"i also made a cipher that is case sensitive"
# print(complex_cipher())