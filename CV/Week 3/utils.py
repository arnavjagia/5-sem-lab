import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def _parse_image_title_pairs(L):
    """Extract (image, title) pairs from flattened list L."""
    pairs = []

    for item in L:
        if type(item) == str:
            pairs[-1][-1] = item
        else:
            pairs.append([item, ''])
    
    return pairs


def plot_images(*args):
    """
    Plot images side-by-side using matplotlib.

    Parameters:
        *args: images and titles

    Example usage:
    >>> plot_images(image1, "title 1", image2, image3, image4, "title 4")
    """
    pairs = _parse_image_title_pairs(args)

    fig, axes = plt.subplots(ncols=len(pairs))
    
    for i, (image, title) in enumerate(pairs):
        ax = axes[i] if len(pairs) > 1 else axes
        ax.axis('off')

        ax.imshow(image, cmap='grey')
        ax.set_title(title)
        
    plt.show()


def display_image(title, image):
    cv.imshow(title, image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    cv.waitKey(1)
    
def get_cdf(img):
    """Return a list representing the cdf function of `img`."""
    hist, _ = np.histogram(img.flatten(), 256, (0, 256))
    cdf = hist.cumsum()
    cdf = cdf / cdf[-1] 
    return cdf

def plot_with_histogram(*args):
    pairs = _parse_image_title_pairs(args)

    fig, axes = plt.subplots(nrows=2, ncols=len(pairs))
    
    for ax in axes.flat:
        ax.axis('off')

    for i, (image, title) in enumerate(pairs):
        col = axes[:, i] if len(pairs) > 1 else axes

        col[0].set_title(title)
        col[0].imshow(image, cmap='grey')

        hist, _ = np.histogram(image, 256, (0, 256))
        cdf = get_cdf(image)
        cdf = cdf * max(hist) / max(cdf)
        
        col[1].plot(cdf, 'b--')
        col[1].hist(image.flatten(), 256, [0,256], color='r')
    
    plt.show()