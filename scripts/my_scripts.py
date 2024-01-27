import os.path
import matplotlib.pyplot as plt
import numpy as np


def hello_world():
    return "Hello, world from you library!"


def transform_path_crossplatform(path):
    """
    Replaces backslashes ("\") with forward slashes ("/") in the given path string.

    :param path: The string representing a file path.
    :type path: str
    :return: The transformed path string with backslashes replaced by forward slashes.
    :rtype: str
    :raises ValueError: If the path parameter is not a string.
    """
    if not isinstance(path, str):
        raise ValueError("The path parameter must be a string")

    return path.replace("\\", "/")


def create_path_for_notebook(path):
    """
    Create a path for a notebook file.

    :param path: The relative path to the notebook file.
    :type path: str
    :return: The transformed cross-platform path for the notebook file.
    :rtype: str
    :raises ValueError: If the path parameter is not a string.
    """
    if not isinstance(path, str):
        raise ValueError("The path parameter must be a string")

    return transform_path_crossplatform(os.path.join('..', path))


def read_image_and_convert_to_np_array(path):
    """
    Read an image file and convert it to a NumPy array.

    :param path: The relative path to the image file.
    :type path: str
    :return: The NumPy array representing the image.
    :rtype: numpy.ndarray
    :raises ValueError: If the path parameter is not a string.
    """
    if not isinstance(path, str):
        raise ValueError("The path parameter must be a string")

    return plt.imread(path)


def convert_np_array_and_show_image_to_plt(np_array):
    """
    Convert a NumPy array representing an image and show it using Matplotlib.

    :param np_array: The NumPy array representing the image.
    :type np_array: numpy.ndarray
    :return: None
    :rtype: None
    :raises ValueError: If the np_array parameter is not a NumPy array.
    """
    if not isinstance(np_array, np.ndarray):
        raise ValueError("The np_array parameter must be a NumPy array")

    image = plt.imshow(np_array)
    plt.show(image)


def grid_with_flips(image, matrix):
    """
    Create a grid of images with different flips.

    :param image: The NumPy array representing the image.
    :type image: numpy.ndarray
    :param matrix: The matrix containing the type of flips that you do with your image.
    :type matrix: list
    :return: None
    :rtype: None
    :raises ValueError: If the image parameter is not a NumPy array.
    :raises ValueError: If the matrix parameter is not a list.
    """
    if not isinstance(image, np.ndarray):
        raise ValueError("The image parameter must be a NumPy array")
    if not isinstance(matrix, list):
        raise ValueError("The matrix parameter must be a list")

    # Create a new figure with a grid of subplots
    fig, axs = plt.subplots(len(matrix), len(matrix[0]))

    # Iterate through the given matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            # Apply the flips according to the matrix values
            if matrix[i][j] == 0:    # no flip
                img = image
            elif matrix[i][j] == 1:  # flip left-right
                img = np.fliplr(image)
            elif matrix[i][j] == 2:  # flip up-down
                img = np.flipud(image)
            elif matrix[i][j] == 3:  # flip both directions
                img = np.flipud(np.fliplr(image))

            # Display the flipped image in the subplot
            axs[i, j].imshow(img)
            axs[i, j].axis('off')

    plt.show()
