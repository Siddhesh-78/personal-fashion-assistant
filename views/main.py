"""import os
import cvzone
import cv2
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture("Resources/Videos/1.mp4")
detector = PoseDetector(staticMode=False,
                        modelComplexity=1,
                        smoothLandmarks=True,
                        enableSegmentation=False,
                        smoothSegmentation=True,
                        detectionCon=0.5,
                        trackCon=0.5)

shirtFolderPath = "Resources/Shirts"
listshirts = os.listdir(shirtFolderPath)
print(listshirts)
fixedRatio = 262/190  #width of shirt/width of paint11 and 12
shirtRatioWeightWidth = 581/440
imageNumber = 0
imgbuttonRight = cv2.imread("Resources/button.png",cv2.IMREAD_UNCHANGED)
imgbuttonleft = cv2.flip(imgbuttonRight,1)
counterRight = 0
counterLeft = 0
selectionspeed =10

while True:
    success, img = cap.read()
    #img = cv2.flip(img,1)
    
    if not success:
        break
    
    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img, draw=True, bboxWithHands=False)

    if lmList:
    # center = bboxInfo["center"]
    lm11 = lmList[11][0:3]
    lm12 = lmList[12][0:3]
    imgShirt = cv2.imread(os.path.join(shirtFolderPath,listshirts[imageNumber]),cv2.IMREAD_UNCHANGED)
    

    widthOfShirt = int((lm11[0]-lm12[0])*fixedRatio)
    print(widthOfShirt)
    imgShirt = cv2.resize(imgShirt,(widthOfShirt, int(widthOfShirt * shirtRatioWeightWidth)))
    currentScale = (lm11[0]-lm12[0])/100
    offset = int(44 * currentScale),int(48 * currentScale)
   
   
   
   
    try:
        img = cvzone.overlayPNG(img,imgShirt,lm12[0]+offset[0],lm12[1]+offset[1])
        #img = cvzone.overlayPNG(img, imgShirt,lm12)
    except:
        pass

    img = cvzone.overlayPNG(img,imgbuttonRight,(1074,293))
    img = cvzone.overlayPNG(img,imgbuttonleft,(72,293))


    if lmList[16][1] <300:
        counterRight += 1
        cv2.ellipse(img,(139,360),(66,66),0,0,
                    counterRight*selectionspeed,(0,255,0),20)
        if counterRight*selectionspeed > 360:
            counterRight = 0
        if imageNumber < len(listshirts)-1:
            imageNumber += 1

    elif lmList[15][1] > 900:
         counterLeft += 1
         cv2.ellipse(img,(1138,360),(66,66),0,0,
                    counterLeft*selectionspeed,(0,255,0),20)
         if counterLeft*selectionspeed > 360:
            counterLeft = 0
         if imageNumber > 0:
            imageNumber -= 1

        
    else:
        counterRight = 0
        counterLeft = 0
        

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()"""

# import os
# import cvzone
# import cv2
# from cvzone.PoseModule import PoseDetector
# import mediapipe

# # Load the video and initialize the pose detector
# cap = cv2.VideoCapture(0)
# detector = PoseDetector(staticMode=False,
#                         modelComplexity=1,
#                         smoothLandmarks=True,
#                         enableSegmentation=False,
#                         smoothSegmentation=True,
#                         detectionCon=0.5,
#                         trackCon=0.5)

# # Load the shirt images from the directory
# shirtFolderPath = "Resources/Shirts"
# listshirts = os.listdir(shirtFolderPath)
# print(listshirts)

# # Constants for shirt sizing
# fixedRatio = 262 / 190  # Adjust this to fit your model
# shirtRatioHeightWidth = 581 / 440  # This seems correct
# imageNumber = 0

# # Load the buttons for interaction
# imgbuttonRight = cv2.imread("Resources/button.png", cv2.IMREAD_UNCHANGED)
# imgbuttonLeft = cv2.flip(imgbuttonRight, 1)

# counterRight = 0
# counterLeft = 0
# selectionspeed = 10

# while True:
#     success, img = cap.read()
#     if not success:
#         break

#     # Detect pose in the image
#     img = detector.findPose(img)
#     lmList, bboxInfo = detector.findPosition(img, draw=True, bboxWithHands=False)

#     if lmList:
#         # Get the positions of landmarks 11 and 12
#         lm11 = lmList[11][:2]  # Take only x, y coordinates
#         lm12 = lmList[12][:2]  # Take only x, y coordinates

#         # Calculate the width of the shirt based on the distance between landmarks 11 and 12
#         widthOfShirt = int((lm11[0] - lm12[0]) * fixedRatio)
#         heightOfShirt = int(widthOfShirt * shirtRatioHeightWidth)

#         # Resize the shirt image to fit the detected pose
#         imgShirt = cv2.imread(os.path.join(shirtFolderPath, listshirts[imageNumber]), cv2.IMREAD_UNCHANGED)
#         imgShirt = cv2.resize(imgShirt, (widthOfShirt, heightOfShirt))

#         # Calculate the offset for positioning the shirt
#         offset = int(44 * (lm11[0] - lm12[0]) / 100), int(48 * (lm11[0] - lm12[0]) / 100)

#         # Overlay the shirt image on the video frame
#         img = cvzone.overlayPNG(img, imgShirt, (lm12[0] + offset[0], lm12[1] - heightOfShirt // 2))

#     # Display the selection buttons
#     img = cvzone.overlayPNG(img, imgbuttonRight, (1074, 293))
#     img = cvzone.overlayPNG(img, imgbuttonLeft, (72, 293))

#     # Handle right button selection
#     if lmList[16][1] < 300:
#         counterRight += 1
#         cv2.ellipse(img, (139, 360), (66, 66), 0, 0, counterRight * selectionspeed, (0, 255, 0), 20)
#         if counterRight * selectionspeed > 360:
#             counterRight = 0
#             if imageNumber < len(listshirts) - 1:
#                 imageNumber += 1

#     # Handle left button selection
#     elif lmList[15][1] > 900:
#         counterLeft += 1
#         cv2.ellipse(img, (1138, 360), (66, 66), 0, 0, counterLeft * selectionspeed, (0, 255, 0), 20)
#         if counterLeft * selectionspeed > 360:
#             counterLeft = 0
#             if imageNumber > 0:
#                 imageNumber -= 1

#     # Reset counters if neither button is pressed
#     else:
#         counterRight = 0
#         counterLeft = 0

#     # Display the final image
#     cv2.imshow("Image", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Clean up
# cap.release()
# cv2.destroyAllWindows()

import os
import cvzone
import cv2
from cvzone.PoseModule import PoseDetector

# Initialize webcam feed
cap = cv2.VideoCapture(0)

# Set the resolution for the webcam (optional)
cap.set(3, 1280)  # Width
cap.set(4, 720)   # Height

detector = PoseDetector(staticMode=False,
                        modelComplexity=1,
                        smoothLandmarks=True,
                        enableSegmentation=False,
                        smoothSegmentation=True,
                        detectionCon=0.5,
                        trackCon=0.5)

# Load the shirt images from the directory
shirtFolderPath = "Resources/Shirts"
listshirts = os.listdir(shirtFolderPath)
print(listshirts)

# Constants for shirt sizing
fixedRatio = 262 / 190  # Adjust this to fit your model
shirtRatioHeightWidth = 581 / 440  # Shirt height-to-width ratio
imageNumber = 0

# Load the buttons for interaction
imgbuttonRight = cv2.imread("Resources/button.png", cv2.IMREAD_UNCHANGED)
imgbuttonLeft = cv2.flip(imgbuttonRight, 1)

counterRight = 0
counterLeft = 0
selectionspeed = 10

while True:
    success, img = cap.read()
    if not success:
        break

    # Detect pose in the image
    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img, draw=True, bboxWithHands=False)

    if lmList:
        # Ensure there are enough landmarks to avoid index errors
        if len(lmList) > 16:  # Check if landmarks 16 (right hand) and 15 (left hand) exist
            # Get the positions of landmarks 11 and 12 (shoulders)
            lm11 = lmList[11][:2]  # Left shoulder (x, y)
            lm12 = lmList[12][:2]  # Right shoulder (x, y)

            # Calculate the width and height of the shirt
            shoulderDistance = int((lm11[0] - lm12[0]) * fixedRatio)
            shirtHeight = int(shoulderDistance * shirtRatioHeightWidth)

            # Increase the size by a small percentage for better fit
            shoulderDistance = int(shoulderDistance * 1.2)
            shirtHeight = int(shirtHeight * 1.2)

            # Ensure the dimensions are positive and reasonable
            if shoulderDistance > 0 and shirtHeight > 0:
                # Resize the shirt image
                imgShirt = cv2.imread(os.path.join(shirtFolderPath, listshirts[imageNumber]), cv2.IMREAD_UNCHANGED)
                imgShirt = cv2.resize(imgShirt, (shoulderDistance, shirtHeight))

                # Calculate midpoint between shoulders for alignment
                midPointX = (lm11[0] + lm12[0]) // 2
                shoulderY = (lm11[1] + lm12[1]) // 2

                # Increased vertical adjustment to place the shirt further down the torso
                verticalOffset = int(0.1 * shirtHeight)  # Increase this value to move the shirt lower

                # Overlay the shirt on the video frame, positioning it below the shoulders
                img = cvzone.overlayPNG(img, imgShirt, (midPointX - shoulderDistance // 2, shoulderY - verticalOffset))

            # Display the selection buttons
            img = cvzone.overlayPNG(img, imgbuttonRight, (1074, 293))
            img = cvzone.overlayPNG(img, imgbuttonLeft, (72, 293))

            # Handle right button selection (checking right hand position)
            if lmList[16][1] < 300:  # Check y-coordinate of right hand
                counterRight += 1
                cv2.ellipse(img, (139, 360), (66, 66), 0, 0, counterRight * selectionspeed, (0, 255, 0), 20)
                if counterRight * selectionspeed > 360:
                    counterRight = 0
                    if imageNumber < len(listshirts) - 1:
                        imageNumber += 1

            # Handle left button selection (checking left hand position)
            elif lmList[15][1] > 900:  # Check y-coordinate of left hand
                counterLeft += 1
                cv2.ellipse(img, (1138, 360), (66, 66), 0, 0, counterLeft * selectionspeed, (0, 255, 0), 20)
                if counterLeft * selectionspeed > 360:
                    counterLeft = 0
                    if imageNumber > 0:
                        imageNumber -= 1

            # Reset counters if neither button is pressed
            else:
                counterRight = 0
                counterLeft = 0

    # Display the final image
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()

