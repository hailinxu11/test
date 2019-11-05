import os
import configparser

# 获取config配置文件
path = os.path.dirname(os.path.dirname(__file__)) + '/config.ini'
# 实例化configParser对象
config = configparser.ConfigParser()
config.read(path, encoding='utf-8')

# 根据标识喝key获取相应的键值
def getConfig(section, key):
    value = config.get(section, key)
    return value

# 获取数据库配置的相应键和值
def getDb(key):
    value = config.get('db', key)
    return value

# 获取日志配置的相应键
def getLog(key):
    value = config.get('log', key)
    return value

# 获取浏览器配置的相应键
def getDriver():
    value = config.getint('browser', 'browser_type')
    return value

# 获取测试的环境
def getDev():
    value = config.getint('dev', 'evn')
    if value == 1:
        value = config.get('dev', 'qa_url')
    elif value == 2:
        value = config.get('dev', 'int_url')
    else:
        value = config.get('dev', 'product_url')
    return value

# 运行结果是否保留的参数
def getResult():
    value = config.getint("result", "is_clear")
    return value

# 是否执行测试用例
def getImplement():
    value = config.getint("implement", "isImplement")
    return value

# 返回邮件服务器
def getServer():
    Smtp_Server = config.get('email', 'Smtp_Server')
    return Smtp_Server

# 邮件发送者邮箱
def getSender():
    Smtp_Sender = config.get('email', 'Smtp_Sender')
    return Smtp_Sender

# 邮件发送者的邮箱密码
def getSender_Pwd():
    Smtp_Sender_Password = config.get('email', 'Smtp_Sender_Password')
    return Smtp_Sender_Password

# 邮件接收者的邮箱
def getReceiver():
    Smtp_Receiver = config.get('email', 'Smtp_Receiver')
    return Smtp_Receiver
