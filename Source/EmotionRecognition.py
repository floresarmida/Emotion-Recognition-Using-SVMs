"""
======================================================
Emotion recognition using SVMs (Scikit-learn & OpenCV
======================================================

Author: Izhar Shaikh
License: MIT
Dependencies: Python 2.7, Scikit-Learn, OpenCV 3.0.0,
              Numpy, Scipy, Matplotlib
Instructions: Please checkout Readme.txt & Instructions.txt

The dataset used in this example is Olivetti Faces:
 http://cs.nyu.edu/~roweis/data/olivettifaces.mat

"""

import matplotlib.pyplot as plt
from sklearn import datasets

faces = datasets.fetch_olivetti_faces()
print faces.keys()

for i in range(10):
    face = faces.images[i]
    plt.subplot(1, 10, i + 1)
    plt.imshow(face.reshape((64, 64)), cmap='gray')
    plt.axis('off')
plt.show()

