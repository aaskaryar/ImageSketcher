import cv2

# Read the image and make sure image is saved in the project under the same directory
image1 = cv2.imread("image1.jpeg")
window_name = 'Orginal Image'

# Display the orginal image
cv2.imshow(window_name, image1)

#Display the image until any key is pressed
grey_image = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_image)

# Apply Gaussian Blur makes the image more smooth
blur = cv2.GaussianBlur(invert, (21, 21), 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_image, invertedblur, scale=256.0)

# Save the image in the project directory
cv2.imwrite("sketch.jpg", sketch)

# Display the sketch image
image = cv2.imread("sketch.jpg")
window_name = 'Sketch Image'

# Display the sketch image
cv2.imshow(window_name, image)

#Display the image until any key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
