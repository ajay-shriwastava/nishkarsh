from tensorflow import keras
import numpy as np
import warnings
import os
from PIL import Image, ImageOps
warnings.filterwarnings('ignore')


class m4_ast_01_seq:

    def load_test_data(self):
        fashion_mnist = keras.datasets.fashion_mnist
        (X_train_full, y_train_full), (X_test, y_test) = fashion_mnist.load_data()
        return X_test, y_test

    def load_model(self, dirName, fileName):
        model_file = os.path.join(dirName, fileName)
        return keras.models.load_model(model_file)

    def __init__(self, dirName = 'static/models/m4', fileName='m4_ast01_ANN_img_classifier.keras'):
        self.model = self.load_model(dirName, fileName)
        self.X_test, self.y_test = self.load_test_data()
        print('Finished loading model')

    def get_model(self):
        return self.model

    def get_class_names(self):
        class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]
        return class_names

    def get_test_data(self):
        return self.X_test

    def get_default_data(self, noOfElements = 10):
        return self.X_test[:noOfElements]

    def get_display_data(self, noOfElements = 10):
        X_test = self.get_default_data(noOfElements)
        X_pred = X_test / 255
        y_raw = self.model.predict(X_pred)
        y_pred = np.argmax(y_raw, axis=-1)
        y_labels = np.array(self.get_class_names())[y_pred]
        return (X_test, y_raw, y_pred, y_labels)

    def get_display_predictions(self, X_pred = None):
        if (X_pred is None) or (not X_pred.any()):
            X_pred = self.get_default_data(1) / 255
        else:
            X_pred = X_pred / 255
        y_raw = self.model.predict(X_pred)
        y_pred = np.argmax(y_raw, axis=-1)
        y_labels = np.array(self.get_class_names())[y_pred]
        return (X_pred, y_raw, y_pred, y_labels)

    def get_class_probabilities(self, X_pred = None):
        if not X_pred:
            X_pred = self.get_default_data() / 255
        y_proba = self.model.predict(X_pred)
        y_proba.round(2)
        return y_proba


