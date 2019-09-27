# include <ros/ros.h>
# include <math.h>
# include <std_msgs/ByteMultiArray.h>

int			main(int argc, char** argv)
{
	ROS_INFO("Action DefFloor server: started");
	ros::init(argc, argv, "def_floor_server");
	ros::NodeHandle n;
	ros::Publisher pub = n.advertise<>();

	while (ros::ok())
	{
		std_msgs::ByteMultiArray arr_msg;
		arr_msg.layout.dim.size = 74;
		arr_msg.layout.s
		pub.publish(arr_msg);
	}
	return 0;
}

/*
std_msgs/MultiArrayLayout layout
  std_msgs/MultiArrayDimension[] dim
    string label
    uint32 size
    uint32 stride
  uint32 data_offset
byte[] data
*/
