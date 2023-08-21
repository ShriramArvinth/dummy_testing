from PIL import Image
import os

path_to_main = os.path.expanduser("~/main")
# Open the image file
with Image.open(path_to_main + '/image.jpg') as im:
    # Calculate the new height based on the new width
    basewidth = 300
    wpercent = (basewidth / float(im.size[0]))
    hsize = int((float(im.size[1]) * float(wpercent)))
    
    # Resize the image
    im_resized = im.resize((basewidth, hsize))
    
    # Save the resized image
    im_resized.save(path_to_main + '/image_resized.jpg')
