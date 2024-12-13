from tensorflow import keras
import numpy as np
import warnings
import os
from PIL import Image, ImageOps
warnings.filterwarnings('ignore')
import m4_ast01_file

ast_01 = m4_ast01_file.m4_ast_01_seq()
UPLOAD_FOLDER = 'static/img/m4/user123/'

def test_display_results():
    display_results = ast_01.get_display_data()
    for result in zip(display_results[1], display_results[2], display_results[3]):
        print(result)


def test_display_predictions_default():
    X_pred, y_raw, y_pred, y_labels = ast_01.get_display_predictions()
    print(y_raw[0], y_pred[0], y_labels[0])

def test_display_predictions():
    for i in range (1, 31):
        im1 = Image.open(os.path.join(UPLOAD_FOLDER, "img_" + str(i) + ".png"))
        image = np.array(im1)
        image = np.reshape(image, (1, 28, 28))
        X_pred, y_raw, y_pred, y_labels = ast_01.get_display_predictions(X_pred=image)
        print(y_raw[0], y_pred[0], y_labels[0])

#test_display_results()
#test_display_predictions_default()
test_display_predictions()
