from PIL import Image

# Load the screenshot image
image = Image.open('screenshot-1725840799671.png')

# Get pixel color at specific coordinates (x, y)
x, y = 1, 120  # Replace with your coordinates
pixel_color = image.getpixel((x, y))

print(f"Color at ({x}, {y}): {pixel_color}")
