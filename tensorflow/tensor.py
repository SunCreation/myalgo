#%%
import tensorflow as tf
from tensorflow.core.framework import node_def_pb2
hello = tf.constant("Hello, tf :)")
tf.print(hello)
type(hello)
# tf.session()함수가 실행하는 역할을 했었는데, 필요없어졌다.

# 노드 연결 : 다음과 같다.
node1=tf.constant(3,tf.float32)
node2=tf.constant(4,tf.float32)
node3=tf.add(node1, node2)
# node4=tf.add(node3, hello) 이건 오류남.
print(node3)
print(hello)
tf.print(node3)
tf.print(hello)
# tf.print(node4)


#%%
