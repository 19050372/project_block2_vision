import cv2
import numpy as np
font= cv2.FONT_HERSHEY_PLAIN
picture = "triangles2.jpg"
image = cv2.imread(picture)
output = image.copy()

#dictionary met kleuren en mask lower and upper range
colormasks = {
  "blue": [[114,64,17],[169,255,67]],
  "red": [[33,22,112],[123,120,255]],
  "green": [[43,81,13],[115,187,120]],
#  "white": [[169,174,171],[220,208,215]],
  "orange": [[6,125,193],[101,203,236]],
  "purple": [[96,30,58],[136,68,97]]
  }

for color in colormasks:
    #set range for one color from colormasks
    lower_range = np.array(colormasks[color][0])  # Set the Lower range value of color in BGR
    upper_range = np.array(colormasks[color][1])  # Set the Upper range value of color in BGR
    #mask color
    mask = cv2.inRange(image, lower_range, upper_range)  # Create a mask with range
    result = cv2.bitwise_and(image, image, mask=mask)  # Performing bitwise and operation with mask in img variable
    pregray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY) #convert mask to gray image
    (thresh, grayImage) = cv2.threshold(pregray, 50, 200, cv2.THRESH_BINARY) #perform treshold

    contours, _ = cv2.findContours(grayImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #find all countours

    # cv2.namedWindow(color, cv2.WINDOW_NORMAL)
    # cv2.resizeWindow(color, 700, 700)
    # cv2.imshow(color, grayImage)

    if contours is not None:     # ensure at least some contours were found
        for cnt in contours:    #use one contour every loop

            #approximate cnt
            epsilon = 0.07 * cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, epsilon, True)
            # cv2.drawContours(output, [approx], 0, ((800, 800, 800)), 30)
            if len(approx)==3:  #if cnt has 3 sides
                if( cv2.contourArea(cnt)>10000):  #if cnt is bigger then 10000
                    #calculate center of triangle
                    xcenter = int((approx.ravel()[0]+approx.ravel()[2]+approx.ravel()[4])/3)
                    ycenter = int((approx.ravel()[1]+approx.ravel()[3]+approx.ravel()[5])/3)

                    trianglename = "driehoek " + color
                    print("driehoek", color, approx.ravel(), "opp:",cv2.contourArea(cnt), "middelpunt: (", xcenter, ",",  ycenter, ")")
                    #draw around triangle + place center and name
                    cv2.drawContours(output, [approx], 0, ((800, 800, 800)), 30)
                    output = cv2.circle(output, (xcenter, ycenter), 20, ((800, 800, 800)), 5)
                    cv2.putText(output, trianglename, (xcenter+50, ycenter), font, 8, (0, 255, 255), 5)



            if len(approx)==4:  #if cnt has 4 sides
                if( cv2.contourArea(cnt)>10000):  #if cnt is bigger then 10000
                    #calculate center of square
                    xcenter = int((approx.ravel()[0]+approx.ravel()[4])/2)
                    ycenter = int((approx.ravel()[1]+approx.ravel()[5])/2)

                    squarename = "vierkant " + color
                    print("vierkant", color, approx.ravel(), "opp:",cv2.contourArea(cnt), "middelpunt: (", xcenter, ",",  ycenter, ")")
                    #draw around triangle + place center and name
                    cv2.drawContours(output, [approx], 0, ((800, 800, 800)), 30)
                    output = cv2.circle(output, (xcenter, ycenter), 20, ((800, 800, 800)), 5)
                    cv2.putText(output, squarename, (xcenter+50, ycenter), font, 8, (0, 255, 255), 5)


# show the output image
cv2.namedWindow('output', cv2.WINDOW_NORMAL)
cv2.resizeWindow('output', 700, 700)
cv2.imshow("output", output)

cv2.waitKey(0)
