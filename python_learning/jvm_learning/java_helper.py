import jpype


def jLong(value):
    return jpype.java.lang.Long(value)


def jDouble(value):
    return jpype.java.lang.Double(value)


def jInteger(value):
    return jpype.java.lang.Integer(value)


def jFloat(value):
    return jpype.java.lang.Float(value)


def jDate(value):
    return jpype.JClass('com.jd.pyapi.ToolUtils').parseDate(value)


