# pip install opencv-python
import cv2

# Load the image
img = cv2.imread("Une_jeune_artiste_04.jpg")

# Get the dimensions of the image
height, width, _ = img.shape

# Divide the width of the image by 6
rect_width = int(width / 6)

# Divide the height of the image by 2
rect_height = int(height)

# Create 6 rectangles
for i in range(6):
    x = i * rect_width
    y = 0
    cv2.rectangle(img, (x, y), (x + rect_width, y + rect_height), (0, 0, 255), 2)

# Show the resulting image
cv2.imshow("6 rectangles", img)
cv2.waitKey(0)
cv2.destroyAllWindows()