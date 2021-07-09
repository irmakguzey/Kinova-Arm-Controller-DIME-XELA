import rospy 
import tf

from std_msgs.msg import Float64MultiArray, MultiArrayDimension

from IPython import embed

REFERENCE_FRAME = 'j2n6s300_link_base'
END_EFFECTOR_FRAME = 'j2n6s300_link_6'

class Transformer(object):
    def __init__(self, rate = 50):
        try:
            rospy.init_node('transform_listener')
        except:
            pass

        self.listener = tf.TransformListener()
        self.Rate = rospy.Rate(rate)

    def record_and_publish(self):
        # br = tf.TransformBroadcaster()

        message = Float64MultiArray()
        message.data = []

        self.pub = rospy.Publisher('/j2n6s300_driver/end_effector_rotation',Float64MultiArray, queue_size=10)

        while not rospy.is_shutdown():
            try:
                (translation, rotation) = self.listener.lookupTransform(REFERENCE_FRAME, END_EFFECTOR_FRAME, rospy.Time(0))
                # rotation = str(rotation)
                message.data = [-rotation[0], -rotation[1], -rotation[2], -rotation[3]]
                self.pub.publish(message)
                self.Rate.sleep()

            except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                print('Not able to get transformation!') 
            
            rospy.sleep(0.1)

if __name__ == '__main__':
    t = Transformer()
    t.record_and_publish()