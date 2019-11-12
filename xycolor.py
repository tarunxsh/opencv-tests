import numpy as np
import cv2
img=cv2.imread('img3.png',1)
#img= np.array([[[1, 2, 3],[4, 5, 6],[7, 8, 9]],[[2, 3, 4],[1, 3, 5],[6, 5, 7]]])
#row=0
#col=0
found=0
cord = []
color=[[0,0,255],[0,255,0]]
for k in color:
	col=0
	row=0
	for i in img:
		row+=1
		#col=0
		for j in i:
			col+=1
			if np.array_equal(j,k):       #BGR value is given
				#print(row,col)
				print('coordinates x,y for {} is {},{}'.format(k,col-1,row-1))
				cord.append((col-1,row-1))	
				found+=1
				#col=0
				#break
			elif col==1024:                             #col==last db_column=''
				col=0
		#if found:break																																																																																																																																																																																																																																																																										
	
if not found:print('not found')
print(cord)
print('total {} coordinates are found'.format(found))
