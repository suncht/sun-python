from python_learning.jvm_learning.jvm_proxy import *
from python_learning.jvm_learning.java_helper import *
import os.path
import datetime
import time

jvmPath = 'D:\\Program Files\\jdk\\jdk1.8.0_51\\jre\\bin\server\\jvm.dll'
jarPath = os.path.join(os.path.abspath('.'), 'E:/') + 'jdwl-pyapi-0.0.1-SNAPSHOT.jar'

with JvmProxy(jvmPath, jarPath) as jvmProxy:
    jmqHelper = JvmProxy.new_java_object('com.jd.pyapi.JmqHelper')
    msg = jmqHelper.getMessage('111')
    print(msg)

    user = JvmProxy.new_java_object('com.jd.pyapi.User', jLong(2), "suncht")
    print(user)

    ToolUtils = JvmProxy.tool_utils()
    print(ToolUtils.currentDateTime())

    str = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
    print(ToolUtils.parseDate(str))

    counter = 100000000
    starttime = datetime.datetime.now()
    jmqHelper.compute(counter)
    endtime = datetime.datetime.now()

    print((endtime - starttime).total_seconds())

    result = 0
    starttime = datetime.datetime.now()
    for i in range(counter):
        result += i

    endtime = datetime.datetime.now()

    print((endtime - starttime).total_seconds())
