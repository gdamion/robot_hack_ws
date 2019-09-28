import rospy
from geometry_msgs.msg import Twist

def talker():
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.init_node('test_move', anonymous=True)
    rate = rospy.Rate(0.4) # 10hz
    type = 0
    while not rospy.is_shutdown():
        msg = Twist()
	if type == 0:
		msg.linear.x = 6
		type = 1
	else:
		msg.angular.z = 1
		type = 0
        pub.publish(msg)
        rate.sleep()
	msg.angular.z = 0
	msg.linear.x = 0
	pub.publish(msg)

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass

