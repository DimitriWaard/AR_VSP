#!/usr/bin/env python
import roslib
#roslib.load_manifest('my_package')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_converter:
    def __init__(self):
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("usb_cam/image_raw", Image, self.callback)

    def callback(self,data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data,"bgr8")
        except CvBridgeError as e:
            print(e)
        
        (rows,cols,channels) = cv_image.shape
        if cols > 60 and rows > 60 :
            cv2.circle(cv_image, (350,250), 200, 255)        
        
        cv2.imshow("yellow_ball",cv_image)
        cv2.waitKey(3)
        
 

def main (args):
    rospy.init_node("yellow_ball", anonymous = True)
    image_converter()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("shut down")
    cv2.destoyAllWindows()

if __name__ == '__main__':
    main(sys.argv)