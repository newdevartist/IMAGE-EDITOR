python
from PIL import Image

# Open an image file
img = Image.open('example.jpg')
# Save the image in a different format
img.save('example.png')
python
# Resize the image
resized_img = img.resize((100, 100))

# Crop the image
cropped_img = img.crop((100, 100, 200, 200))

# Rotate the image
rotated_img = img.rotate(45)
python
from PIL import ImageFilter

# Convert the image to grayscale
grayscale_img = img.convert('L')

# Apply a blur filter
blurred_img = img.filter(ImageFilter.BLUR)
# We Implement a Simple User Interface: we can use Tkinter or PyQt to create a simple user interface for the image editor. Tkinter is the standard GUI toolkit for Python, while PyQt is a more advanced and feature-rich option. Here are some resources for creating a UI with Tkinter and PyQt: