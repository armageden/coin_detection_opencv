import cv2 
import numpy as np
def coin_cnt(img_path):
    img= cv2.imread(img_path)
    if img is None:
        raise ValueError(f"Image not found in {img_path} or unable to read")
        return
    gry_scl=cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY) #gray scaling hope fully works...
    
    blur_img=cv2.GaussianBlur(gry_scl,(11,11),0) #blurring the image
    # increased the values for added clarity for the detection as from test runs I saw the coins need more room to work neatly...
    
    # to display the result at this point
    cv2.imshow("blurred image",blur_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()# press any key to close the display window
    
    edges_img=cv2.Canny(blur_img,50,156) # might need to change to detect more edges for a better result
    # to display the result at this point
    cv2.imshow("edges image",edges_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()# press any key to close the display window
    
    
    