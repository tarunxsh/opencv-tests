import numpy as np
import cv2
img=cv2.imread('img1.png',1)
#img= np.array([[[1, 2, 3],[4, 5, 6],[7, 8, 9]],[[2, 3, 4],[1, 3, 5],[6, 5, 7]]])
row=0
col=0
found=0
for i in img:
	row+=1
	for j in i:	
		col+=1
		if np.array_equal(j, [25,104,15]):       #BGR value is given
			print(row,col)
			print('coordinates x,y is {},{}'.format(col-1,row-1))	
			found=1
			col=0
			break
		elif col==350:                             #col==last_column
			col=0
																																																																																																																																																																																																																																																																											
	
if not found:print('not found')
