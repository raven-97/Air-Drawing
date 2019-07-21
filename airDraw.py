import numpy as np
import cv2
cap=cv2.VideoCapture(0)
_,old_frame=cap.read()
mask1 = np.zeros_like(old_frame)
counter=0
while(1) :
    check, frame=cap.read()
    
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  
    blur = cv2.GaussianBlur(hsv, (11,11),0)
    
    l_orange=np.array([10,180,180])
    h_orange=np.array([30,255,255])
    
    mask = cv2.inRange(hsv, l_orange , h_orange)
    mblur = cv2.GaussianBlur(mask,(15,15),0)
    
    ret,thresh = cv2.threshold(mblur,127,255,0)
    image, contours, heirarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    img = cv2.drawContours(frame, contours, -1, (0,255,0), 3)
    if( contours != []):
        cnt = contours[0]
        M = cv2.moments(cnt)
        if M['m00']!=0:
            cx = int (M['m10']/M['m00'])
            cy = int (M['m01']/M['m00'])
            if (counter==0) :
                cx1=cx
                cy1=cy
            if(counter==0):
                counter += 1
            mask1 = cv2.line(mask1, (cx,cy),(cx1,cy1),(0.0,255),2)
            frame = cv2.circle(frame,(cx,cy),8,(0,0,255),-1)
            cx1=cx
            cy1=cy
        img=cv2.add(frame,mask1)
        cv2.imshow("ori",img)
        cv2.imshow("mask",mask1)
        k=cv2.waitKey(1)
        if k==ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
                
