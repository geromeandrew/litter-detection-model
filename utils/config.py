import os
import numpy

width = [0.50, 0.75, 1.0, 1.25]
depth = [0.33, 0.67, 1.0, 1.33]

versions = ['s', 'm', 'l', 'x']
data_dir = 'data'

threshold = 0.3
max_boxes = 150
image_dir = 'images'
label_dir = 'labels'

num_epochs = 100
batch_size = 16
image_size = 640

class_dict = {'plastic': 0, 'trash': 1}

version = 's'
anchors = numpy.array([[171.,  196.],    [187.5, 327.5],   [255.,  216.5],
                       [284.,  280.5],  [314.,  336.],  [410.,  381.],
                       [421.5, 273.], [493.,  325.], [503.,  380.]], numpy.float32)
