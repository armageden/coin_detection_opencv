import cv2 as cv
def main():
    # Load an image
    image = cv.imread('image.jpg')

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Could not load image.")
        return
    #take multiple images all at once and on demand
    # Display the image in a window
    cv.imshow('Image', image)
    # Wait for a key press indefinitely
    cv.waitKey(0)
    