import cv2 as cv;
import numpy as np;

print("Welcome to PicFi")

#take image path as input
path = input("Enter Image Path\n")

#read + resize image
img = cv.resize(cv.imread(path,1),(750,600))


#greyimage function
def greyImage(image):
    #convert color img to grey and return it
    return cv.cvtColor(image,cv.COLOR_BGR2GRAY)

#display output of 1 & 2
def display(input,output):
    cv.imshow("Input Image",input)
    cv.imshow("Output Image",output)
    cv.waitKey(0)
    cv.destroyAllWindows()

flag = True;
while flag:
    #take filter input from user
    filter = int(input("Choose the Filter \n 1.Grey  2.Thresholding  3.Histogram Processing   4.Exit\n"));
    
    
    #Grey
    if filter == 1:
        grey = greyImage(img)
        display(img,grey)
        

    #Thresholding
    elif filter == 2:
        grey = greyImage(img)
        threshVal = int(input("Enter Threshold Value: "))

        #ret is boolean value that returns true if the frame is available
        ret, threshImg = cv.threshold(grey, threshVal, 255, cv.THRESH_BINARY)

        display(grey,threshImg)

    #Histogram Equalization
    elif filter == 3:
        grey = greyImage(img)
        histEqu = cv.equalizeHist(grey)
        output = np.hstack((grey,histEqu));
        cv.imshow("Histogram Equalization (Input Left, Output Right)",output)
        cv.waitKey(0);
        cv.destroyAllWindows();

    #exit app
    elif filter == 4:
        flag=False;
        
    else:
        print("Wrong Input")

