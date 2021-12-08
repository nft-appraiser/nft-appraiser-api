import os
import gc
import time
import imghdr
from io import BytesIO
from typing import List, Optional

import requests
import numpy as np
import pandas as pd
from tqdm.notebook import tqdm  # if you don't use IPython Kernel like jupyter, you should change "tqdm.notebook" to "tqdm"
from cairosvg import svg2png
from PIL import Image
import cv2
import tensorflow as tf
import tensorflow.keras.layers as layers
import tensorflow.keras.models as models
import tensorflow.keras.losses as losses
import tensorflow.keras.optimizers as optim
import tensorflow.keras.activations as activations
from tensorflow.keras.utils import Sequence
import tensorflow.keras.callbacks as callbacks
from tensorflow.keras.wrappers.scikit_learn import KerasRegressor
import cloudpickle

def is_image(url) -> bool:
    """
    Determine if it is an image of png or jpeg.
    Parameters
    ----------
    url : str
        Target url.
    Returns
    -------
    True or False: Return True if this url content is an image of png or jpeg else returns False.
    """
    img = requests.get(url).content
    img_type = imghdr.what(None, h=img)

    if img_type in ['png', 'jpeg']:
        return True
    else:
        return False


def is_svg(url) -> bool:
    """
    Determine if it is an image of svg.
    Parameters
    ----------
    url : str
        Target url.
    Returns
    -------
    True or False: Return True if this url content is an image of svg else returns False.
    """
    if url.endswith(".svg"):
        return True
    else:
        return False


def save_png(url, file_name) -> None:
    """
    Save an image of png or jpeg as a png file. 
    Parameters
    ----------
    url : str
        Target url.
    file_name : str
        The file path of a saved png file.
    Returns
    -------
    None
    """
    img = requests.get(url).content
    img = Image.open(BytesIO(img)).convert("RGBA")
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGBA2BGRA)
    cv2.imwrite(file_name, img, [int(cv2.IMWRITE_PNG_COMPRESSION), 3])


def save_svg(url, file_name) -> None:
    """
    Save an image of svg as an svg file. The content that is svg data of animation can't save. 
    Parameters
    ----------
    url : str
        Target url.
    file_name : str
        The file path of a saved png file.
    Returns
    -------
    None
    """
    img = requests.get(url).content
    img = svg2png(bytestring=img)
    img = Image.open(BytesIO(img)).convert("RGBA")
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGBA2BGRA)
    cv2.imwrite(file_name, img)

def load_model(file_name: str):
    """
    Load the model file of pickle.
    Parameters
    ----------
    file_name : str
        The absolute path of the model file.
    Returns
    -------
    model : tf.keras.models.Model
        Trained model object.
    """
    with open(file_name, mode='rb') as f:
        model = cloudpickle.load(f)

    return model
