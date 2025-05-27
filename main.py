import cv2 
def main():
    # Load an image
    image = cv2.imread('image.jpg')

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Could not load image.")
        return
    #take multiple images all at once and on demand
    # Display the image in a window
    cv2.imshow('Image', image)
    # Wait for a key press indefinitely
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)