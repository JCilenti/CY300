from PIL import Image
f = open("COLPIXVALS.txt", "w")
img = Image.open("image2.jpg")
pix_val = list(img.getdata())
pix_val_flat = [x for sets in pix_val for x in sets]
f.write(str(pix_val_flat))