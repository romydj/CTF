from PIL import Image

im = Image.open("code1.png")
pix = im.load()
w,h = im.size

black = (0,0,0)
white = (255,255,255)

red = (255,0,0)
purple = (128,0,128)
blue = (0,0,255)
green = (0,128,0)
yellow = (255,255,0)
orange = (255, 165,0)

mid = w/2
code=""
for y in xrange(0,h,12):
	biner =""
	col = pix[0,y]
	if (col == red):
		warna = 0
	elif (col == purple): 
		warna = 1
	elif (col == blue): 
		warna = 2
	elif (col == green): 
		warna = 3
	elif (col == yellow): 
		warna = 4
	elif (col == orange): 
		warna = 5
	for x in xrange(mid,w,12):
		bw = pix[x,y]
		if (bw == black):
			biner+='1'
		else:
			biner+='0'
	code += chr(int(biner,2)-warna)
	
print code
