import cv2 as cv;
import numpy as np;

print("Welcome to PicFi")
path = input("Enter Image Path\n")

img = cv.resize(cv.imread(path,1),(450,600))

flag = True;

while flag:
    filter = int(input("Choose the Filter \n 1.Grey  2.Thresholding  3.Histogram Processing   4.Exit\n"));

    #Grey
    if filter == 1:
        grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        # stack = np.hstack((img,grey))
        cv.imshow("Input Image",img)
        cv.imshow("Output Image",grey)
        cv.waitKey(0)
        cv.destroyAllWindows()

    #Thresholding
    elif filter == 2:
        grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        threshVal = int(input("Enter Threshold Value: "))

        #ret is boolean value that returns true if the frame is available
        ret, threshImg = cv.threshold(grey, threshVal, 255, cv.THRESH_BINARY)

        cv.imshow("Input Image",grey)
        cv.imshow("Output Image",threshImg)
        cv.waitKey(0)
        cv.destroyAllWindows()

    #Histogram Equalization
    elif filter == 3:
        grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        histEqu = cv.equalizeHist(grey)
        output = np.hstack((grey,histEqu));
        cv.imshow("Histogram Equalization (Input Left, Output Right)",output)
        cv.waitKey(0);
        cv.destroyAllWindows();

    elif filter == 4:
        flag=False;
    else:
        print("Wrong Input")