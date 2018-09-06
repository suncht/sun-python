from python_learning.jvm_learning.jvm_proxy import *
from python_learning.jvm_learning.java_helper import *
import os.path

jvmPath = 'D:\\Program Files\\jdk\\jdk1.8.0_51\\jre\\bin\server\\jvm.dll'
jarPath = os.path.join(os.path.abspath('.'), 'E:/') + 'jdwl-pyapi-0.0.1-SNAPSHOT.jar'

class MyListener1:
    def handle(self, event):
        print('收到消息1:' + event.message)

class MyListener2:
    def handle(self, event):
        print('收到消息2:' + event.message)

with JvmProxy(jvmPath, jarPath) as jvmProxy:
    # Application = JvmProxy.static_java_object('com.jd.pyapi.Application')
    # Application.start()

    providerFactory = JvmProxy.static_java_object('com.jd.pyapi.bus.MessageProviderFactory')
    provider = providerFactory.getInstance("aaa").getMessageProvider()

    myListener1 = MyListener1()
    proxy1 = JvmProxy.new_interface_object('com.jd.pyapi.bus.EventMessageHandler', instance=myListener1)
    provider.register(proxy1)

    myListener2 = MyListener2()
    proxy2 = JvmProxy.new_interface_object('com.jd.pyapi.bus.EventMessageHandler', instance=myListener2)
    provider.register(proxy2)

    providerFactory.startMessageSend(provider)

    user = JvmProxy.new_java_object('com.jd.pyapi.User', jLong(2), "suncht")
    print(user)
