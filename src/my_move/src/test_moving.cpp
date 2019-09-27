# include <ros/ros.h>
# include <math.h>
# include <geometry_msgs/Twist.h>

using namespace std;

int main(int argc, char **argv)
{
	ros::init(argc, argv, "move_node");

	ros::NodeHandle n;
	ros::Publisher move = n.advertise<geometry_msgs::Twist>("/cmd_vel", 1000);

	ros::Rate loop_rate(2);

	int mode = 0;
	int count = 0;
	while(ros::ok() && count < 4)
	{
		geometry_msgs::Twist msg;

		switch (mode)
		{
		case 0:
			msg.linear.x = 15;
			mode = 1;
			break;
		case 1:
			msg.angular.z = 3;
			mode = 0;
			break;
		default:
			break;
		}
		move.publish(msg);

		loop_rate.sleep();
		ros::spinOnce();
		++count;
	}
	ros::spin();
	return (0);
}
