from PIL import Image
import pytesseract
from pytesseract import image_to_string

str = image_to_string(Image.open("captcha.jpg"))
print(str)

num1 = int(str[0:1])
num2 = int(str[2:3])

if '+' in str:
    print(num1+num2)
elif '-' in str:
    print(num1-num2)
elif '*' in str:
    print(num1*num2)
elif '/' in str:
    print(num1/num2)
else:
    print('Unable to process the result')

