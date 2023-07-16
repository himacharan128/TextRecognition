import numpy as np
import pandas as pd
import cv2
import os
import tqdm
from scipy.io import loadmat
import matplotlib.pyplot as plt

image_path = 'Data/images/'
gt_path = 'Data/ground_truth/'
train_image_paths = []
train_gt_paths = []


for new_file in tqdm.tqdm(os.listdir(gt_path)):
    
    name_split = new_file.split('.')
    image_name = name_split[0][3:]
    image_name = image_name + '.jpg'
    
    if 'gt' in new_file:
        image_name = name_split[0][3:]
        image_name = image_name + '.jpg'
    
    path_img = os.path.join(image_path , image_name)
    train_image_paths.append(path_img)
    train_gt_paths.append(os.path.join(gt_path , new_file))



X_final = []
Y_final = []
grid_h = 16
grid_w = 16
img_w = 512
img_h = 512



for z in tqdm.tqdm(range(len(train_image_paths))):
    new_file = train_image_paths[z]
    x = cv2.imread(train_image_paths[z])
    x_sl = 512/x.shape[1]
    y_sl = 512/x.shape[0]
    img = cv2.resize(x,(512,512))
    X_final.append(img)
    #plt.imshow(cv2.imread(new_file))
    #plt.show()
    i = " "
    if 'img' in new_file:
        i = ", "
    Y = np.zeros((grid_h,grid_w,1,5))
    file = train_gt_paths[z]
    name = open(file , 'r')
    data = name.read()
    data = data.split("\n")
    data = data[:-1]
    for li in data:
        temp_list = []
        file_data = li.split(i)
        strr = file_data[4]
        bb = file_data[:4]
        
        xmin = int(bb[0])*x_sl
        xmax = int(bb[2])*x_sl
        ymin = int(bb[1])*y_sl
        ymax = int(bb[3])*y_sl
        #te = cv2.rectangle(img,(int(xmin),int(ymin)),(int(xmax),int(ymax)) , color = (0,255,0))
        w = (xmax - xmin)/img_w
        h = (ymax - ymin)/img_h
        
        x = ((xmax + xmin)/2)/img_w
        y = ((ymax + ymin)/2)/img_h
        x = x * grid_w
        y = y * grid_h

        Y[int(y),int(x),0,0] = 1
        Y[int(y),int(x),0,1] = x - int(x)
        Y[int(y),int(x),0,2] = y - int(y)
        Y[int(y),int(x),0,3] = w
        Y[int(y),int(x),0,4] = h
    #plt.imshow(te)
    #plt.show()
    Y_final.append(Y)
X = np.array(X_final)
X_final = []
Y = np.array(Y_final)
Y_final = []
X = (X - 127.5)/127.5
np.save('Data/X.npy',X)
np.save('Data/Y.npy',Y)
for i in range(5):
    img = (X[i] * 127.5) + 127.5  # Denormalize the image data
    bb_indices = np.where(Y[i][:, :, 0, 0] == 1)

    for y, x in zip(bb_indices[0], bb_indices[1]):
        bbox = Y[i][y, x, 0, 1:]
        x_center = (x + bbox[0]) * (img_w / grid_w)
        y_center = (y + bbox[1]) * (img_h / grid_h)
        width = bbox[2] * img_w
        height = bbox[3] * img_h
        xmin = int(x_center - width / 2)
        ymin = int(y_center - height / 2)
        xmax = int(x_center + width / 2)
        ymax = int(y_center + height / 2)

        cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

    plt.imshow(img.astype(np.uint8))
    plt.title('Processed Image with Bounding Box')
    plt.show()
