import pythonpy
import tensorflow as tf
from keras.layers import Input, Dense, Flatten
from keras.models import Sequential
import matplotlib.pyplot as plt
from keras.datasets import mnist
import numpy as np

print("Tensorflow version: ", tf.__version__)

(x_train, y_train), (x_test, y_test) = mnist.load_data()
print("x_train: "+str(x_train.shape))
print("y_train: "+str(y_train.shape))
print("x_test: "+str(x_test.shape))
print("y_test: "+str(y_test.shape))

# x_train: (60000, 28, 28)
#             ^      ^
#             |     dimensiunile imaginilor (28px*28px)
#           dimensiunea (60000 de imagini)
# y_train: (60000,) > output???? (zice ca y reprezinta etichetele pt imagini)
# x_test: (10000, 28, 28)
# y_test: (10000,)


# for i in range(9):
#     plt.subplot(330+1+i)
#     plt.imshow(x_train[i],cmap=plt.get_cmap('gray'))
# plt.show()


model = Sequential(
    [
        Input((28,28)),
        Flatten(),
        Dense(16, activation='relu',name='hidden_layer1'),
        Dense(16, activation='relu',name='hidden_layer2'),
        Dense(10, activation='softmax'),
    ]
)

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.summary()
epoci=10
def learnStupid(epoci):
    model.fit(x=x_train, y=y_train,epochs=10,validation_split=0.2)
    print(np.argmax(model.predict(np.array([x_test[10]]))))
    plt.imshow(x_test[10],cmap=plt.get_cmap('gray'))
    plt.show()
    isRight=input("E corect?")
    if isRight=="nu":
        epoci+=10
        learnStupid(epoci)
    else:
        print("Bravo Patratel")

learnStupid(epoci)


