import rospy
from std_msgs.msg import Int32MultiArray, MultiArrayDimension

def talker():
	index = 0
	pub = rospy.Publisher("toggle_led", Int32MultiArray, queue_size=100)
	rospy.init_node('led_publisher', anonymous=True)
	rate = rospy.Rate(1)
	msg1 = Int32MultiArray()
	msg1.layout.data_offset = 0
	msg1.layout.dim = [MultiArrayDimension()]
	msg1.layout.dim[0].label = "leds"
	msg1.layout.dim[0].size = 24
	msg1.layout.dim[0].stride = 24
	while not rospy.is_shutdown():
		if index % 2 == 0:
			msg1.data = [0 for i in range(24)]
		else:
			msg1.data = [255 for i in range(24)]
		pub.publish(msg1)
		rate.sleep()
		index += 1

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		print ("shit_happen")

	
