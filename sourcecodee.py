import rospy
import cv2
from clover import srv
from clover.srv import SetLEDEffect
from std_srvs.srv import Trigger
rospy.init_node('flight') # 'flight' is name of your ROS node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)
from mavros_msgs.msg import RCIn

# Called when new data is received from the transmitter
def rc_callback(data):
    # React on toggling the mode of the transmitter
    if data.channels[5] < 1100:
        # ...
        pass
    elif data.channels[5] > 1900:
        # ...
        pass
    else:
        # ...
        pass

# Creating a subscriber for the topic with the data from the transmitter


rospy.spin()
rospy.init_node('computer_vision_sample')
bridge = CvBridge()

def image_callback(data):
    cv_image = bridge.imgmsg_to_cv2(data, 'bgr8')  # OpenCV image
    # Do any image processing with cv2...
navigate(x=0, y=0, z=1.5, speed=0.5, frame_id='aruco_map', auto_arm=True)
rospy.sleep(5)
navigate(x=1, y=0, z=1.5, speed=0.5, frame_id='aruco_map', auto_arm=True)
rospy.sleep(2)
navigate(x=2, y=0, z=1.5, speed=0.5, frame_id='aruco_map', auto_arm=True)
rospy.sleep(2)
navigate(x=3, y=0, z=1.5, speed=0.5, frame_id='aruco_map', auto_arm=True)
rospy.sleep(2)
navigate(x=4, y=0, z=1.5, speed=0.5, frame_id='aruco_map', auto_arm=True)
rospy.sleep(2)
navigate(x=5, y=0, z=1.5, speed=0.5, frame_id='aruco_map', auto_arm=True)
rospy.sleep(2)
navigate(x=6, y=0, z=1.5, speed=0.5, frame_id='aruco_map', auto_arm=True)
rospy.sleep(2)
navigate(x=7, y=0, z=1.5, speed=0.5, frame_id='aruco_map', auto_arm=True)
rospy.sleep(2)
navigate(x=7, y=1, z=1.5, speed=0.5, frame_id='aruco_map', auto_arm=True)
rospy.sleep(2)
navigate(x=6, y=1, z=1.5, speed=0.5, frame_id='aruco_map', auto_arm=True)
rospy.sleep(2)
navigate(x=5, y=1, z=1.5, speed=0.5, frame_id='aruco_map', auto_arm=True)
rospy.sleep(2)
navigate(x=4, y=1, z=1.5, speed=0.5, frame_id='aruco_map', auto_arm=True)
rospy.sleep(2)
navigate(x=3, y=1, z=1.5, speed=0.5, frame_id='aruco_map', auto_arm=True)
rospy.sleep(2)
navigate(x=2, y=1, z=1.5, speed=0.5, frame_id='aruco_map', auto_arm=True)
rospy.sleep(2)
navigate(x=1, y=1, z=1.5, speed=0.5, frame_id='aruco_map', auto_arm=True)
rospy.sleep(2)
navigate(x=0, y=1, z=1.5, speed=0.5, frame_id='aruco_map', auto_arm=True)
rospy.sleep(2)

image_sub = rospy.Subscriber('main_camera/image_raw', Image, image_callback)
set_effect = rospy.ServiceProxy('led/set_effect', SetLEDEffect)  

set_effect(r=255, g=0, b=0)  #Stop the car
rospy.sleep(2)

set_effect(r=0, g=100, b=0)  # Move the car
rospy.sleep(2)

set_effect(effect='flash', r=0, g=0, b=255)  #Take right turn
rospy.sleep(2)

set_effect(effect='flash', r=255, g=0, b=0)  # Tske left turn
rospy.sleep(5)

set_effect(effect='blink', r=255, g=255, b=255)  # blink with white color
rospy.sleep(5)

set_effect(effect='rainbow') # parking done
rospy.sleep(5)

rospy.spin()


image_pub = rospy.Publisher('~debug', Image)
# Publishing the processed image (at the end of the image_callback function):

image_pub.publish(bridge.cv2_to_imgmsg(cv_image, 'bgr8'))
land()
rospy.Subscriber('mavros/rc/in', RCIn, rc_callback)
