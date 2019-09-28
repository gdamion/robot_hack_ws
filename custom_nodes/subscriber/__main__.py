import rospy
from sensor_msgs.msg import LaserScan


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("slam_gmapping", LaserScan, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()