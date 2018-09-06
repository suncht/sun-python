# from jpype import *

import jpype
import os.path

from python_learning.jvm_learning.java_helper import *

jarpath = os.path.join(os.path.abspath('.'), 'E:/')
print(jarpath)
# jvmPath = jpype.getDefaultJVMPath()
jvmPath = 'D:\\Program Files\\jdk\\jdk1.8.0_51\\jre\\bin\server\\jvm.dll'
jpype.startJVM(jvmPath, "-ea",
               "-Djava.class.path=%s" % (jarpath + 'jdwl-pyapi-0.0.1-SNAPSHOT.jar'))

try:
    aa = jpype.JClass('com.jd.pyapi.JmqHelper2')
except Exception as e:
    print(e)

while True:
    JmqHelper = jpype.JClass('com.jd.pyapi.JmqHelper')
    jmq = JmqHelper()
    msg = jmq.getMessage('111')
    print(msg)


    UserClass = jpype.JClass('com.jd.pyapi.User')
    user = UserClass(jpype.java.lang.Long(2))
    user.userName = 'dff'
    user.id = jpype.java.lang.Long(11)
    print(user)

    msg = jmq.getMessage(user)
    print(msg)


    msg = jmq.getMessage(jInteger(1), jLong(2), jDouble(3.0), jFloat(4.0))
    print(msg)

    DatabaseHelper = jpype.JClass('com.jd.pyapi.DatabaseHelper')
    db = DatabaseHelper()
    db.init()

    result = db.select("select * from sf_basic_store_info where store_no='110008502'")
    print(result)

    ToolUtils = jpype.JClass('com.jd.pyapi.ToolUtils')
    print(ToolUtils.currentDateTime())

    ToolUtils2 = jpype.JClass('com.jd.pyapi.ToolUtils')
    print(ToolUtils2.currentDateTime())


jsfService = jpype.JClass('com.jd.pyapi.jsf.JdsmartSiteJsfService')()
bbcSiteCondition = jpype.JClass('com.jd.jdgo.master.member.condition.BbcSiteCondition')()
bbcSiteCondition.sourceSiteNo = "110008533"
bbcSiteCondition.source = jpype.java.lang.Integer(2)

siteService = jsfService.siteService()
site = siteService.queryBbcSite(bbcSiteCondition)
print(site.projectName)


jpype.shutdownJVM()
