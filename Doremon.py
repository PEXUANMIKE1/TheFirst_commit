from PIL import Image

# Load the image
img = Image.open('doremon.png')

# Get the size of the image
width, height = img.size

# Create a new image with the same size
new_img = Image.new('RGB', (width, height), 'white')

# Loop through each pixel and set the color of the corresponding pixel in the new image
for x in range(width):
    for y in range(height):
        # Get the color of the pixel
        color = img.getpixel((x, y))
        # Set the color of the corresponding pixel in the new image
        new_img.putpixel((x, y), color)

# Save the new image
new_img.save('doremon_pixel.png')
