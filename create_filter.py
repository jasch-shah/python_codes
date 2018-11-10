from PIL import Image
from PIL import ImageFilter
img = Image.open("6.jpg")
img = img.convert("L")
new_img = img.filter(ImageFilter.Kernel((3,3),[1,0,-1,5,0,-5,1,0,1]))
new_img.save("cr6.jpg")
new_img.show()