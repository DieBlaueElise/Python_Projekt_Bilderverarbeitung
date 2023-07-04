from PIL import Image
from numpy import asarray
# load the image

#image = Image.open('hs_bw_512.png')
#print(image.mode)
#(image.size)
# convert image to numpy array
#data = asarray(image)
#print(type(data))
# summarize shape
#print(data.shape)

# create Pillow image
#image2 = Image.fromarray(data)
#print(type(image2))

# summarize image details
#print(image2.mode)
#print(image2.size)

def imagetonparray(myimage):
    image = Image.open(myimage)
    mydata = asarray(image)
    return mydata

mydatapng = imagetonparray('hs_bw_512.png')
print(mydatapng)
mydatajpg = imagetonparray('jpeg2000-home.jpg')
print(mydatajpg)
mydatabmp = imagetonparray('Felis_silvestris_silvestris_small_gradual_decrease_of_quality.bmp')
print(mydatabmp)
    