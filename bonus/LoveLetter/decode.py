from PIL import Image

img1 = Image.open('flag.png')

rgb_image = img1.convert('RGB')

myimage = Image.new("RGB",(838,502))

for x in xrange(0,838) :
	for y in xrange(0,502):
		r, g, b = rgb_image.getpixel((x,y))
		if(r%2 == 0):
			myimage.putpixel((x,y),(255,255,255))
		if(r%2 == 1):
			myimage.putpixel((x,y),(0,0,0))
myimage.save('out.png')