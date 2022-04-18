import cv2 as cv;
print("Welcome to PicFi")
path = input("Enter Image Path\n")


flag = True;

while flag:
    filter = int(input("Choose the Filter \n 1.Grey  2.Histogram Processing  3.Thresholding 4.Exit\n"));
    if filter == 1:
        img = cv.imread(path,0)
        cv.imshow("Grey Output",cv.resize(img,(450,550)))
        cv.waitKey(0)
        cv.destroyAllWindows()
    elif filter == 4:
        flag=False;


# cv.imshow("Output",inpImg)
# cv.waitKey(0)