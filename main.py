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
    
    contour,f=cv2.findContours(edges_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) # finding the contours of the image
    if contour is None:
        raise ValueError("No contours found in the image")
        return
    else:
        print(f"Number of contours found: {len(contour)}")
    # to display the result at this point
    
    # to compare contours with the area of the coins in the original image
    img_copy=img.copy()
    coin_cnt=0
    
    #filtering the contours based on area
    for i ,c in enumerate(contour):
        area=cv2.contourArea(c)
        perm=cv2.arcLength(c,True)
        #apox for a poligon
        approx=cv2.approxPolyDP(c,0.02*perm,True)
        
        min,max=1000,10000 #might need adjustment based on the image size
        circule=0 # to check if the contour is a circle but this   is for taking the value... please remember future me...
        if perm>0:
            circule=4*3.14*area/(perm*perm)
        #flag the detected contour as a coin...ig
        coin=True
        if not (min<area<max):
            coin=False
        if circule<0.66 or circule>1.3:
            coin=False
        if len(approx)<6:# this might need to change depending on the accuracy..
            coin=False
        if coin:
            cv2.drawContours(img_copy, [c], -1, (0, 255, 0), 2)  #detection on the image(green :3)
            coin_cnt+=1
    #display the result at this point
    print("\n Starting to display the result...")
    cv2.imshow("detected coins",img_copy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()  # press any key to close the display window
    print(f"Total number of coins detected: {coin_cnt}")
    
if __name__ == "__main__":
    img_path = "/home/backlog/Downloads/s-l1600-1014332594.jpg"
    # Provide the path to your image here
    coin_cnt(img_path)  # Call the function with the image path
    # Example: coin_cnt("path/to/your/image.jpg")
        
    
    