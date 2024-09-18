# finding key
#key code given
total=0
for i in range(5):
    for j in range(3):
        if i + j == 5:
            total += i + j
        else:
            total -= i - j

counter=0
while counter < 5:
    if total < 13:
        total += 1
    elif total > 13:
        total -= 1
    else:
        counter += 2
print("Key:",total)
# counter can only increase if total = 13 meaning 13 must be our total and our key, running code agrees with this logic

# creating 'decrypt' function based off given 'encrypt' function (also shown below)

def encrypt(text,key):
    encrypted_text=""
    for char in text:
        if char.isalpha():
            shifted=ord(char)+key
            if char.islower():
                if shifted>ord('z'):
                    shifted-=26
                elif shifted<ord('a'):
                    shifted+=26
            elif char.isupper():
                if shifted>ord('Z'):
                    shifted-=26
                elif shifted<ord('A'):
                    shifted+=26
            encrypted_text+=chr(shifted)
        else:
            encrypted_text+=char
    return encrypted_text

def decrypt(text,key):
    decrypted_text=""
    for char in text:
        if char.isalpha():
            shifted=ord(char)-key # subtracting the key rather than adding it should return the ASCII value to what it was before encryption
            if char.islower():
                if shifted>ord('z'):
                    shifted-=26
                elif shifted<ord('a'):
                    shifted+=26
            elif char.isupper():
                if shifted>ord('Z'):
                    shifted-=26
                elif shifted<ord('A'):
                    shifted+=26
            decrypted_text+=chr(shifted)
        else:
            decrypted_text+=char
    return decrypted_text

#initialise key as 13 (shown above) and the encrypted code as text (given)
key=13 
encrypted_code='''
tybony_inevnoyr = 100
zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}

qrs cebprff_ahzoref():
    tybony tybony_inevnoyr 
    ybpny_inevnoyr = 5
    ahzoref= [1, 2, 3, 4, 5]
    
    juvyr ybpny_inevnoyr > 0:
        vs ybpny_inevnoyr % 2 == 0: 
            ahzoref.erzbir(ybpny_inevnoyr)
        ybpny_inevnoyr -= 1
        
    erghea ahzoref

zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg = cebprff_ahzoref(ahzoref=zl_frg)

qrs zbqvsl_qvpg():
    ybpny_inevnoyr = 10
    zl_qvpg['xrl4'] = ybpny_inevnoyr

zbqvsl_qvpg(5)

qrs hcqngr_tybony():
    tybony tybony_inevnoyr
    tybony_inevnoyr += 10

sbe v va enatr(5):
    cevag(v)
    v += 1

vs zl_frg vf abg Abar naq zl_qvpg['xrl4'] == 10:
    cevag("Pbaqvgvba zrg!")

vs 5 abg va zl_qvpg:
    cevag("5 abg sbhaq va gur qvpgvbanel!")

cevag(tybony_inevnoyr)
cevag(zl_qvpg)
cevag(zl_frg)'''
#decrypt and print the code
decrypted_code=decrypt(encrypted_code,key)
print(decrypted_code)

# decryption returns a block of code with errors, seen below with the errors fixed and marked by comments

global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers(numbers): #'numbers' was being defined in the function when it should have been a parameter
    global global_variable #'global_variable' is defined in the function but never used
    local_variable = 5

    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.remove(local_variable)
        local_variable -= 1

    return numbers

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1} # sets are unable to have duplicate values meaning many of these values are lost immediately
result = process_numbers(numbers=my_set)

def modify_dict(local_variable): #'local variable' was being defined in the function when it should have been a parameter
    my_dict['key4'] = local_variable

modify_dict(5)

def update_global(): # this function is never called meaning 'global_variable' is never altered or used
    global global_variable
    global_variable += 10

for i in range(5):
    print(i)
    i += 1 # incrementing i here does not affect anything, these two lines may be in the incorrect order

if my_set is not None and my_dict['key4'] == 10: # the condition is not met however this may be intentional
    print("Condition met!")

if 5 not in my_dict.values(): # if statement was searching the keys in 'my_dict' when 5 would be a value, not a key
    print("5 not found in the dictionary!")

print(global_variable)
print(my_dict)
print(my_set)