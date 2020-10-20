import hopfield
from skimage.transform import resize
from skimage.filters import threshold_mean
from skimage.color import rgb2gray
import skimage.data
from matplotlib import pyplot as plt
import numpy as np
import cv2
np.random.seed(1)

# Utils


def get_corrupted_input(input, corruption_level):
    corrupted = np.copy(input)
    inv = np.random.binomial(n=1, p=corruption_level, size=len(input))
    for i, v in enumerate(input):
        if inv[i]:
            corrupted[i] = -1 * v
    return corrupted


def reshape(data):
    dim = int(np.sqrt(len(data)))
    data = np.reshape(data, (dim, dim))
    print('data', data)
    return data


def plot(data, test, predicted, figsize=(6, 6)):
    data = [reshape(d) for d in data]
    test = [reshape(d) for d in test]
    predicted = [reshape(d) for d in predicted]

    print('data reshaped', data)

    fig, axarr = plt.subplots(len(data), 3, figsize=figsize)
    for i in range(len(data)):
        if i == 0:
            axarr[i, 0].set_title('Train data')
            axarr[i, 1].set_title("Input data")
            axarr[i, 2].set_title('Output data')

        axarr[i, 0].imshow(data[i], cmap='plasma_r')
        axarr[i, 0].axis('off')
        axarr[i, 1].imshow(test[i], cmap='plasma_r')
        axarr[i, 1].axis('off')
        axarr[i, 2].imshow(predicted[i], cmap='plasma_r')
        axarr[i, 2].axis('off')

    plt.tight_layout()
    plt.show()


def preprocessing(img, w=128, h=128):
    # Resize image
    img = resize(img, (w, h), mode='reflect')

    # Thresholding
    thresh = threshold_mean(img)
    binary = img > thresh
    shift = 2*(binary*1)-1  # Boolian to int

    # Reshape
    flatten = np.reshape(shift, (w*h))
    return flatten


def main():
    # Load data
    # camera = np.array([[1, 1, 1, 1, 1], [-1, -1, -1, 1, -1], [-1, -1, -1,
    #                                                           1, -1], [-1, -1, -1, 1, -1], [1, 1, 1, -1, -1]], dtype=float)
    # astronaut = np.array([[1, 1, 1, 1, 1], [-1, -1, 1, -1, -1], [-1, -1,
    #                                                              1, -1, -1], [-1, -1, 1, -1, -1], [-1, -1, 1, -1, -1]], dtype=float)
    # horse = np.array([[1, 1, 1, 1, 1], [1, -1, -1, -1, -1], [1, 1,
    #                                                          1, 1, 1], [1, -1, -1, -1, -1], [1, 1, 1, 1, 1]], dtype=float)
    # coffee = np.array([[-1, 1, 1, 1, -1], [1, -1, -1, -1, 1], [1, -
    #                                                            1, -1, -1, 1], [1, -1, -1, -1, 1], [-1, 1, 1, 1, -1]], dtype=float)

    # Marge data
    data = np.array([[1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, 1, 1, 1, -1, -1],
                     [1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -
                      1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1],
                     [1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1,
                      1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1],
                     [-1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, -1]])

    # print('data', data)

    # Preprocessing
    # print("Start to data preprocessing...")
    # data = [preprocessing(d) for d in data]

    # Create Hopfield hopfield Model
    model = hopfield.HopfieldNetwork()
    model.train_weights(data)

    # Generate testset
    test = np.array([[1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1],
                     [1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -
                      1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1],
                     [1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1,
                      1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1],
                     # [1, -1, -1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1],
                     [-1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, -1]])

    predicted = model.predict(test, threshold=0, asyn=False)
    print("Show prediction results...")
    plot(data, test, predicted)
    print("Show hopfield weights matrix...")
    model.plot_weights()


if __name__ == '__main__':
    main()
