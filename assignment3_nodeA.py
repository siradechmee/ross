import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talkerA', anonymous=True)
    rate = rospy.Rate(10)
    rospy.Subscriber("chatter2", String, callback)
    while not rospy.is_shutdown():
        hello_str = input("node A say = :")
        #rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
  
talker()