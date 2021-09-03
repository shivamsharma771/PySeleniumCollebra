from pytesseract import image_to_string
from PIL import Image, ImageEnhance, ImageFilter

im = Image.open(r'C:\Users\hp\Desktop\imagetc.png') 
print(im)

txt = image_to_string(im)
print(txt)