import sys
def complex_cipher():
    strr=str(input('Enter the message you want encoded: '))
    key= int(input('enter your encrytion key: '))
    cypt=[]
    final=''
    for char in strr:
        if ord(char)<65 or (ord(char)>90 and ord(char)<96):
            try: 
                int(char)
                cypt.append(char)
                
            except: 
                cypt.append('/')
        
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
# def simple_cipher():
#     strrr=str(input('Enter the message you want encoded: '))
#     keyr= int(input('enter your encrytion key: '))
#     cyptr=[]
#     finalr=''
#     strrr.upper()
#     for char in strrr:
#         cyptr.append(char)


print(complex_cipher())