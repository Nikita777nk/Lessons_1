import numpy as np
from PIL import Image
from math import floor
img_mat = np.zeros((2000,2000,3), dtype=np.uint8)

x0,y0,x1,y1 = 12.34, 43.21,123.45,987.65
def line(img_mat,x0,y0,x1,y1):
    x0 = x0*15000+1700
    y0 = y0*15000+1000
    x1 = x1*15000+1700
    y1 = y1*15000+1000
    dmax = max(abs(floor(x0)-floor(x1)), abs(floor(y0)-floor(y1)))
    L = dmax+1
    if L==1:
       img_mat[int(floor(x0)),int(floor(y0))] = 255
       return
    dx = (x1-x0) / (L-1)
    dy = (y1-y0) / (L-1)
    for i in range(int(L)):
        x0 = x0 + dx
        y0 = y0 + dy
        img_mat[int(floor(x0)),int(floor(y0))] = 255
#line(img_mat,x0,y0,x1,y1)
pf = []
v = []
file = open("model.obj")
for s in file:
    spl = s.split()
    if spl[0] == "v":
        v.append(spl[1:])


        
# for i in range(len(v)):
#     for j in range(3):
#         v[i][j] = float(v[i][j])
#     img_mat[-floor((v[i][1]+0.06)*5000),floor((v[i][0]+0.1)*5000)] = [180,255,255]

file.close()
file = open("model.obj")
for s in file:
    spl = s.split()
    
    if spl[0] == "f":
        arr = []
        arr.clear()
        arr.append(int(spl[1].split('/')[0])-1)
        arr.append(int(spl[2].split('/')[0])-1)
        arr.append(int(spl[3].split('/')[0])-1)
        pf.append(arr)
for i in range(len(pf)):
    line(img_mat,
         -v[pf[i][0]][1],
         v[pf[i][0]][0],
         -v[pf[i][1]][1],
         v[pf[i][1]][0],
         )
    line(img_mat,
         -v[pf[i][1]][1],
         v[pf[i][1]][0],
         -v[pf[i][2]][1],
         v[pf[i][2]][0],
         )
    line(img_mat,
         -v[pf[i][0]][1],
         v[pf[i][0]][0],
         -v[pf[i][2]][1],
         v[pf[i][2]][0],
         )



img = Image.fromarray(img_mat)
img.save('img.png')