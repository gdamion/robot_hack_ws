import rospy
from nav_msgs.msg import OccupancyGrid


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", type(data.data))


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("map", OccupancyGrid, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
