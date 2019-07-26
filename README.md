# Air-Drawing



This is  simple computer vision based code snippet which tracks a target and uses the said target to draw on air.
This project make use of a web cam to track the motion of the target.

The lines of code below are used to set the range of the color of your tracker. Here  the target is of orange and
the values in brackets specifies a range for the desired color.

l_orange=np.array([10,180,180])
h_orange=np.array([30,255,255])


These lines below are used to calculate the centroid of your target to get a finer pointing tip to draw with.

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
	    
	    
Each frame in the video is blurred using Gaussian blur to get a smooth image. The blurred image is then analysed to get the loaction of pointing target.
The image is then masked and centroid of target is found. Then a line i drawn from current frame to the previous frame.




