import cv2
import pytesseract

# Read image
img = cv2.imread('quote.png')

# Set configurations
config = ('-l eng --oem 1 --psm 3')

# Convert the image to grayscale 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

# OTSU threshold performing
ret, threshimg = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

# Specifying kernel size and structure shape
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

# Applying dilation on the threshold image 
dilation = cv2.dilate(threshimg, rect_kernel, iterations=1)

# Getting contours 
img_contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Loop over contours and crop and extract the text file
with open("recognized.txt", "a") as file:
    for cnt in img_contours:
        x, y, w, h = cv2.boundingRect(cnt)

        # Drawing a rectangle
        rect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Cropping the text block  
        cropped_img = img[y:y + h, x:x + w]

        # Applying tesseract OCR on the cropped image 
        text = pytesseract.image_to_string(cropped_img, config=config)

        # Appending the text into file 
        if text.strip():  # Only write non-empty text to the file
            print(text)
            file.write(text + "\n")

# Close the file (with 'with' statement, no need to explicitly close)
