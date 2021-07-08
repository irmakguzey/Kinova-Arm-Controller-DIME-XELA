import rospy 
import tf

from std_msgs.msg import String

from IPython import embed

REFERENCE_FRAME = 'j2n6s300_link_base'
END_EFFECTOR_FRAME = 'j2n6s300_link_6'

class Transformer(object):
    def __init__(self, rate = 50):
        try:
            rospy.init_node('transform_listener')
        except:
            pass

        self.pub = rospy.Publisher('chatter', String, queue_size=10)

        self.listener = tf.TransformListener()
        self.Rate = rospy.Rate(rate)

    def record_and_publish(self):
        # br = tf.TransformBroadcaster()

        while not rospy.is_shutdown():
            try:
                (translation, rotation) = self.listener.lookupTransform(REFERENCE_FRAME, END_EFFECTOR_FRAME, rospy.Time(0))
                rotation = str(rotation)
                self.pub.publish("Rotation: %s" % rotation)
                self.Rate.sleep()

            except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                print('Not able to get transformation!') 
            
            rospy.sleep(0.1)

if __name__ == '__main__':
    t = Transformer()
    t.record_and_publish()