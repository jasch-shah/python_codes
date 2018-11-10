from keras.models import Sequential		
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
'''
i)
Sequential package initializes our neural network as sequential network
 There are two basic ways of initializing NL and they are :
 1)Using sequence of layers
 2) Using Graphs

ii)
Conv2D:
	This package performs convolutional operation on training sets
	This is first actual step
	In this case as we are working on images it's 2D

iii)
MaxPooling2D:
	This package is imported so as to perform pooling operation in building a CNN
	In this case , we use maxpooling.

iv)
Flatten:
	This one is imported  for using Flattening.
	Flattening is process of converting all resultant  2D arrays into single
	long continous linear vector.

v)
Dense:
	This import statement is used to perform full connection of neural network	 


'''

# Step 1:Convulation Step
classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), 
activation = 'relu'))

'''
Now Let us breakdown above statement like a pro
At the start of are code ,given neural network is sequential
We added Convolutional Layer using Conv2D method
Here,it consist of 4 params
1--> Number of Filters in our case it is 32
2--> Shape of Each Filter which is 3*3
3--> Input Shape and color type of image(RGB or Black and White)
	 here we are taking 64 X 64 resolution and 3 indicates RGB
4-->Activation Function .In our case it is relu i.e rectifier function
Step 2: Perform Pooling Operation:
'''

#Step 2:Perform Pooling operation

classifier.add(MaxPooling2D(pool_size = (2, 2)))

'''
we take are classifier and add pooling layer to it
we take 2X2 matrix

'''


#Step 3:Flatten

classifier.add(Flatten())


#Step 4:Dense
classifier.add(Dense(units = 128, activation = 'relu'))
#units are no of nodes that should be present in this hidden layer
#unit value is always between no of input nodes and output nodes

classifier.add(Dense(units = 1, activation = 'sigmoid'))
#since the final layer contain single node,so we used sigmoid activation 
#function

#Wooo,done with CNN .Lets gets started with compile part

classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', 
metrics = ['accuracy'])

#Optimizer parameter is to choose the stochastic gradient descent 
#algorithm.
#Loss parameter is to choose the loss function.
#Finally, the metrics parameter is to choose the performance metric.

#Now let us train our data sets
train_datagen = ImageDataGenerator(rescale = 1./255,
shear_range = 0.2,
zoom_range = 0.2,
horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('training_set',
target_size = (64, 64),
batch_size = 32,
class_mode = 'binary')

test_set = test_datagen.flow_from_directory('test_set',
target_size = (64, 64),
batch_size = 32,
class_mode = 'binary')

'''
What Just Happened

we are creating synthetic data out of the same images by performing
 different type of operations on these images like flipping, rotating,
  blurring, etc.
'''

# Fit Data ot our Model

classifier.fit_generator(training_set,
steps_per_epoch = 8000,
epochs = 25,
validation_data = test_set,
validation_steps = 2000)
# epoch stands for no of images in train set

# Part 3 - Making new predictions
import numpy as np
from keras.preprocessing import image
test_image = image.load_img('dataset/single_prediction/cat_or_dog_1.jpg', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
training_set.class_indices
if result[0][0] == 1:
prediction = 'dog'
else:
prediction = 'cat'
