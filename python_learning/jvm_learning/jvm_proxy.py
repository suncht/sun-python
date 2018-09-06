import jpype


class JvmProxy(object):
    def __init__(self, jvm_path, lib_path=None, ext_path=None):
        self.jvm_path = jvm_path
        self.lib_path = lib_path
        self.ext_path = ext_path
        self._is_jvm_ready = False

    def start_jvm(self):
        """
        启动JVM虚拟机
        :return:
        """

        args = ["-ea"]
        if isinstance(self.lib_path, list):
            args.append("-Djava.class.path=%s" % ':'.join(self.lib_path))
        else:
            args.append("-Djava.class.path=%s" % self.lib_path)

        if self.ext_path:
            args.append("-Djava.ext.dirs=%s" % self.ext_path)

        jpype.startJVM(self.jvm_path, *args)

        self._is_jvm_ready = True

    def stop_jvm(self):
        """
        关闭JVM虚拟机
        :return:
        """
        if self._is_jvm_ready:
            jpype.shutdownJVM()


    def __enter__(self):
        self.start_jvm()


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop_jvm()

    @staticmethod
    def new_java_object(class_name, *args):
        """
        实例化java对象
        :param className:
        :return:
        """
        if class_name is None or class_name == '':
            raise Exception('class name is none')

        try:
            class_obj = jpype.JClass(class_name)
            return class_obj(*args)
        except Exception as e:
            print(e)

        return None

    @staticmethod
    def static_java_object(static_class_name):
        if static_class_name is None or static_class_name == '':
            raise Exception('static class name is none')

        try:
            static_class_obj = jpype.JClass(static_class_name)
            return static_class_obj
        except Exception as e:
            print(e)

        return None

    @staticmethod
    def new_interface_object(interface_class_name, instance):
        if interface_class_name is None or interface_class_name == '':
            raise Exception('interface class name is none')
        try:
            jproxy = jpype.JProxy(interface_class_name, inst=instance)
            return jproxy
        except Exception as e:
            print(e)

        return None

    @staticmethod
    def tool_utils():
        return jpype.JClass('com.jd.pyapi.ToolUtils')


