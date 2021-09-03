import os
from PIL import Image

# Directory Path
path = r"J:\Saving Ayah\RGBA\Very Hard"

def add_alpha(name:str):
    img = Image.open("{}/{}".format(path, name))
    img_rgba = img.convert("RGBA") # convert RGB format to RGBA
    img_data = img_rgba.getdata()

    new_data = []

    for item in img_data:
        if item[0] == 255 and item[1] == 255 and item[2] == 255: # Checking if the pixel location is a white color rgb(255, 255, 255)
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
    
    img_rgba.putdata(new_data)
    img_rgba.save("{}/{}".format(path, name), "PNG")
    print("Conversion has been successfully executed")
 
with os.scandir(path) as dirs:
    for entry in dirs:
        add_alpha(entry.name)
