# TODO: Build Convolutional Neural Network in Keras Here
# added pooling
# added dropout


# TODO: Build Convolutional Pooling Neural Network with Dropout in Keras Here
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=(32,32,3)))
model.add(MaxPooling2D(pool_size=(2, 2), strides=None, padding='valid', data_format=None))
model.add(Dropout(0.5, noise_shape=None, seed=None))
model.add(Activation('relu'))
model.add(Flatten())
model.add(Dense(128))
model.add(Activation('relu'))
model.add(Dense(5))
model.add(Activation('softmax'))