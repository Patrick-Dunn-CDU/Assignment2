import time
from PIL import Image
import numpy as np

# Chapter 1
print("\nCHAPTER 1\n")
# number generation code given
current_time = int(time.time())

generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10

print(generated_number)
#open the image
image_in=Image.open('chapter1.jpg')
#apply the generated number to each pixel using the 'eval' function
image_out=Image.eval(image_in,(lambda x: x+generated_number))
#take all pixel values as a numpy array
a=np.asarray(image_out)
#add all of the values from the pixels, which will be the 'r','g', and 'b' values and print the sum of only the 'r' values
sums=np.sum(a,axis=(0,1))
print("Sum of all 'r' values:",sums[0])
#save the altered image as a png
image_out.save('chapter1out.png')

# Chapter 2
print("\n\nCHAPTER 2\n")
#example s value containing upper/lower case letter and numbers
s="1iunhsd91273dhWTBDCFTERB927h3nex4680e"
#create substrings separating numbers and letters
number_substring=""
letter_substring=""
for i in s:
    if i.isdigit():
        number_substring+=i
    else:
        letter_substring+=i
#print the filtered substrings
print("Number Substring:",number_substring)
print("Letter Substring:",letter_substring)
#initialise empty lists
even_ASCII=[]
upper_ASCII=[]
#add all even number ASCII codes to the corresponding list
for i in number_substring:
    if int(i)%2==0:
        even_ASCII.append(ord(i))
#add all uppercase letter ASCII codes to the corresponding list
for i in letter_substring:
    if i.isupper():
        upper_ASCII.append(ord(i))
#print results
print("Even Numbers ASCII Codes:",even_ASCII)
print("Uppercase Letters ASCII Codes:",upper_ASCII)

#coded message given
coded="VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"
#initialise variables, setting the 's' shift key to 13
decoded=""
s=13
#for each character in the message, shift using ASCII values by the shift key except when the value is a space
for i in coded:
    if ord(i)==32:
        decoded+=i
    elif ord(i)-s<65:
        decoded+=chr(ord(i)-s+26)
    else:
        decoded+=chr(ord(i)-s)
print("The decoded message is:\n",decoded,"\nWhere the shift key value 's' is 13")