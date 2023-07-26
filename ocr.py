from PIL import Image
import pytesseract
im_file = "image-2.webp"
im = Image.open(im_file)
ocr_result = pytesseract.image_to_string(im)
print(ocr_result)



