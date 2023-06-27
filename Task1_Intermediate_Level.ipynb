import cv2

def image_to_pencil_sketch(image_path):
    # Read the image in RGB format
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted_image = cv2.bitwise_not(gray_image)

    # Blur the inverted image
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)

    # Create the pencil sketch by dividing the grayscale image by the inverted blurry image
    pencil_sketch = cv2.divide(gray_image, blurred_image, scale=256.0)

    return pencil_sketch

# Provide the path to your image
image_path = 'path/to/your/image.jpg'

# Convert the image to a pencil sketch
sketch = image_to_pencil_sketch(image_path)

# Display the original image and the pencil sketch
cv2.imshow('Original Image', cv2.imread(image_path))
cv2.imshow('Pencil Sketch', sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()
