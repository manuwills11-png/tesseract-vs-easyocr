import pytesseract
import cv2
from easyocr import Reader
import re


image_path = "photo/stay_badass.jpg"
def read_text_tesseract():
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    text = pytesseract.image_to_string(thresh, lang='eng')
    return text


reader=Reader(['en'])
def read_text_easyocr():
    text=""
    results=reader.readtext(image_path)
    for result in results:
        text+=result[1]+" "

    
    return text.strip()




def jaccard_similarity(text1, text2):

    text1 = re.sub(r'[^\w\s]', '', text1.lower())
    text2 = re.sub(r'[^\w\s]', '', text2.lower())

    set1 = set(text1.split())
    set2 = set(text2.split())

    intersection = set1 & set2
    union = set1 | set2

    if not union:
        return 0

    return len(intersection) / len(union)

if __name__ == "__main__":   
    t1 = read_text_tesseract()
    t2 = read_text_easyocr()
    print("Tesseract:", t1)
    print("EasyOCR:", t2)
    score = jaccard_similarity(t1, t2)
    print(f"Jaccard Similarity: {score:.4f}")