import cv2
import matplotlib.pyplot as plt

def main():
    # Load an image
    image = cv2.imread('image.jpg')

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Could not load image.")
    # Display the image in a window
    cv2.imshow('Image', image)
    # Wait for a key press indefinitely
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Prepare a binary image for contour detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    (x,y),radius = cv2.minEnclosingCircle(contours[0])
    center = (int(x),int(y))
    radius = int(radius)

    # Prepare an RGB copy for plotting
    image_rgb_copy2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cv2.circle(image_rgb_copy2, center, radius, (0,255,0), 2)
    (x,y),radius = cv2.minEnclosingCircle(contours[0])
    center = (int(x),int(y))
    radius = int(radius)

    cv2.circle(image_rgb_copy2,center,radius,(0,255,0),2);

    # draw circle to original image
    plt.imshow(image_rgb_copy2)
    plt.axis('off')
    plt.show()
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur to the grayscale image
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    # Apply Canny edge detection
    edges = cv2.Canny(blurred_image, 100, 200)
    # Find contours in the edge-detected image
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Draw contours on the original image
    cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
    # Display the image with contours
    cv2.imshow('Contours', image)
    # Wait for a key press indefinitely
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
# This code loads an image, processes it to find contours, and displays the results.