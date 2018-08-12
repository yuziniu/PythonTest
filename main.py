#-*- coding:utf-8 -*-
import imageio
import matplotlib.pyplot as plt
import numpy
print("first print")
print("second print")
pic = imageio.imread('d:/2.png')
plt.figure(figsize=(15,15))
print('value of Only R channel{}'.format(pic[100,50,0]))
print('value of Only G channel{}'.format(pic[100,50,1]))
print('value of Only B channel{}'.format(pic[100,50,2]))
plt.title('R channel')
plt.ylabel('Height{}'.format(pic.shape[0]))
plt.xlabel('Weight{}'.format(pic.shape[1]))
plt.imshow(pic[:,:,2])
plt.show()

