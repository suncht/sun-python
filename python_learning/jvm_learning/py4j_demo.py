from py4j.java_gateway import JavaGateway, GatewayParameters, CallbackServerParameters

gateway = JavaGateway(gateway_parameters=GatewayParameters(address='127.0.0.1', port=15000),
                      callback_server_parameters=CallbackServerParameters(address='dev.clover.jd.com', port=15001))
jvm = gateway.jvm
app = gateway.entry_point
value = app.addition(10, 20)
print(value)

# 测试公用类
print(jvm.com.jd.pyapi.ToolUtils.currentDateTime())

# 测试生产者和消费者
class MyListener(object):
    def id(self):
        return 'MyListener'

    def handle(self, event):
        print('收到消息2:' + event.getMessage())

    class Java:
        implements = ["com.jd.pyapi.bus.EventMessageHandler"]

providerFactory = jvm.com.jd.pyapi.bus.MessageProviderFactory
provider = jvm.com.jd.pyapi.bus.MessageProviderFactory.getInstance("aaa").getMessageProvider()
provider.register(MyListener())

#providerFactory.startMessageSendAsync(provider)


jmqHelper = jvm.com.jd.pyapi.JmqHelper()
val = jmqHelper.compute(10000000)
print(val)

# 测试JSF
siteService = app.getBean("siteService")
if siteService is not None:
    print(siteService.getSite(1).getSiteName())


# 测试JMQ
class MyJmqMessageProcessor(object):

    def process(self, topic, message):
        print('收到JMQ消息[%s]: %s' % (message.getTopic(), message.getText()))

    class Java:
        implements = ["com.jd.pyapi.jmq.JmqMessageProcessor"]

jmqMessageListener = app.getBean("commonMessageListener")
jmqMessageListener.register('aaa', MyJmqMessageProcessor())

# 测试JIM
jimClient = app.getBean('jimClient')
jimClient.set('1', 'python_test')
print(jimClient.get('1'))


# 测试JSS
JssHelper = app.getBean('jssHelper')
#JssHelper.upload('py4j', '123456789')

print(JssHelper.download('123456789'))