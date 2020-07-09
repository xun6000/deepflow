import scipy.io
import numpy
import numpy as np
#coding=utf-8

#baab 这是竖着的图
# dataFile = '/Users/gy12/Desktop/notebooks/bioml/training_set/poor/new/P13_p.mat'
# data = scipy.io.loadmat(dataFile)
# #print(len(data['final_tumor']))
#
# #data['final_tumor']
# #a= [[[0,0,0] for i in range(20000)] for j in range(15000)]
# #a=numpy.zeros((15000,20000,3))
# scipy.misc.imsave("p13.jpg", data['final_tumor']*255)
from PIL import Image
import os

def cal(folder):
    #folder="V2007-761_AS"
    numbers=len(os.listdir(folder+"/w"))
    print("number is", numbers)
    for number in range(0,numbers):
        cancer_name= folder+"/w/"+str(number)+".png"
        t_name=folder+"/r/"+str(number)+".png"
        cancer=Image.open(cancer_name)
        cancer = np.array(cancer.convert("RGB"))
        t = Image.open(t_name)
        t = np.array(t.convert("RGB"))
        count_ai_cell=0
        count_t_cell=0
        for ii in range(64):
            for jj in range(64):
                if t[ii][jj][0] > 150:
                    cancer[ii][jj][0]=255
                    cancer[ii][jj][1] = 0
                    cancer[ii][jj][2] = 0
                if int(cancer[ii][jj][0]) > 150 and int(cancer[ii][jj][1]) > 150 and int(cancer[ii][jj][2]) > 150:
                    count_ai_cell+=1
                if int(cancer[ii][jj][0])-int(cancer[ii][jj][1])>150:
                    count_t_cell+=1
        name=folder+"/c/"+str(number)+".png"
        #if count_ai_cell>=900 :#and count_t_cell>0:
        #cancer = scipy.misc.imresize(cancer, (64, 64))
        scipy.misc.imsave(name, cancer)



    # import matplotlib.image as mpimg
    # lena = Image.open("b.png") #20000*15000, the size is correct. So i ONLY NEED TO FIND THE POSITION OF T CELLS
    # # # #
    # # # #
    # # # # #
    # lena2 = np.array(lena.convert("RGB"))
    # a,b,c=lena2.shape #横着的是a,b 竖着的是b，a
    # print("a,b,",a,b) #20000:12000
    # resized=lena2
    # # #
    # # #
    # # #
    # # for k in range(int(len(data['centroids_all']))):
    # #     #print(k)
    # #     if data['centroids_all'][k][1]>=10 and data['centroids_all'][k][0]>=10 and data['centroids_all'][k][1]<a-10 and data['centroids_all'][k][0]<b-10:
    # #
    # #
    # #
    # #         x,y=int(data['centroids_all'][k][1]),int(data['centroids_all'][k][0])
    # #         lena2[x-10:x+11,y-10:y+11,0]=255
    # #         lena2[x - 10:x + 11, y - 10:y + 11, 1] = 0
    # #         lena2[x - 10:x + 11, y - 10:y + 11, 2] = 0
    # #
    # #     else:
    # #         print("i am not here")
    # # #
    # # # # firstpart= lena2[0:int(a/2)]
    # # # # secondpart= lena2[int(a/2):]
    # # # #scipy.misc.imsave("p23s.jpg", firstpart)
    # # # #scipy.misc.imsave("p27bs.jpg", secondpart)
    # # #
    # # scipy.misc.imsave("p13s.jpg", lena2)
    # # print(lena2.shape)
    # # print(lena2.size)
    # from PIL import Image
    # #
    # #
    # #
    #
    # # img = Image.open("p13s.jpg")
    # #
    # height=a
    # width=b
    #
    # #img=Image.fromarray(lena2)
    # #img=lena2.convert("RGB")
    # #resized = lena.resize((width,height))
    # #scipy.misc.imsave("resized2006w.jpg", resized)
    # print("done")
    #  #20000*15000, the size is correct. So i ONLY NEED TO FIND THE POSITION OF T CELLS
    # #
    # #
    # #
    # #resized= np.array(resized.convert("RGB"))
    # #print(type(resized))
    # #print(resized.shape)
    # count = 0
    # for i in range(int(height/64)-2):
    #     for j in range(int(width/64)-2):
    #python
    #         current = resized[64*i:64+64*i,64*j:64+64*j]
    #
    #         print(i)
    #         name = "r/"+str(count)+".jpg"
    #
    #
    #         # count_t_cell = 0
    #         # count_ai_cell = 0
    #         for ii in range(64):
    #             for jj in range(64):
    #                 if current[ii][jj][0]>150:
    #                     current[ii][jj][1]=0
    #                     current[ii][jj][2]=0
    #                 # if int(current[ii][jj][0])>150 and int(current[ii][jj][1])>150 and int(current[ii][jj][2])>150:
    #                 #     count_ai_cell+=1
    #         #         if int(current[ii][jj][0])-int(current[ii][jj][1])>150:
    #         #             count_t_cell+=1
    #         # if count_ai_cell>=900 and count_t_cell>0:
    #         scipy.misc.imsave(name, current)
    #         count+=1
    # #
    #
    #
    # #
    # #
    # #
    # #
    # #
    #
    #
    #
    #
    #
    # #
    # # # print("done")
    # # #
    # # # for i in range(len(data['final_tumor'])):
    # # #     for j in range(len(data['final_tumor'][0])):
    # # #         if data['final_tumor'][i][j]==0:
    # # #             a[i][j][0],a[i][j][1],a[i][j][2]=1,1,1
    # # import math
    # # lena2=lena2[0:6130,0:6130]
    # # scipy.misc.imsave("fefe5.jpg", lena2)
    # # import random
    # # for i in range(10):
    # #     for j in range(10):
    # #         lena2[i][j][0]=255
    #
    #
    # for k in range(len(data['centroids_all'])):
    #     if int(math.floor(data['centroids_all'][k][0]))<6130 and int(math.floor(data['centroids_all'][k][1]))<6130:
    #         print("get one")
    #         lena2[int(math.floor(data['centroids_all'][k][0]))][int(math.floor(data['centroids_all'][k][1]))][0]=255
    #         lena2[int(math.floor(data['centroids_all'][k][0]))][int(math.floor(data['centroids_all'][k][1]))][1] = 0
    #         lena2[int(math.floor(data['centroids_all'][k][0]))][int(math.floor(data['centroids_all'][k][1]))][2] = 0
    #
    #
    # scipy.misc.imsave("fefe6.bmp", lena2)

    # # # print("done")
    # #
    # #
    # #
    # #
    # # import copy
    # #
    # # c=copy.deepcopy(data['final_tumor']*255)
    # # s=c
    # # s1=np.append(s,c)
    # # s2=np.append(s1,c)
    # # s3=np.reshape(s2,(15000,20000,3))
    # # print(len(s3[0][0]))
    # # print(s.shape)
    # # print(s1.shape)
    # # print(s2.shape)
    # # print(s3.shape)
    #
    # #print(s.shape)
    # #scipy.misc.imsave("fefe3.jpg", s3)
    # lena = Image.open("fefe4.jpg")
    # print(lena)
    # #r,g,b=lena.split()
    #
