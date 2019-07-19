import logging
import logging.handlers

#输出到文件，文件路径请使用绝对路径 logs
#输出到控制台，定义输出级别是DEBUG
#不同的输出级别可配置
#并不是所有的封装都需要用类进行封装，类是具体相同的行为和特征才需要用类来进行封装
# 日志里级别有哪几种
# debug info warning error critical

def get_logger():
    logger = logging.getLogger('loans')  # 创建一个日志收集器
    logger.setLevel('DEBUG') # 设置日志级别,给这个日志收集器setLevel（可放配置文件配置）
    #定义日志输出格式
    fmt = '%(asctime)s-[%(levelname)s]-%(filename)s[line:%(lineno)d] -[%(name)s]-[日志信息]:%(message)s'
    format = logging.Formatter(fmt) #定义日志的输出格式
    # a ="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"

    # 输出到指定的文件
    file_handler = logging.handlers.RotatingFileHandler('loans.log',maxBytes=20*1024*1024, backupCount=10, encoding='utf-8')
    file_handler.setLevel('INFO')   #设置文件输出级别（可进行配置化）
    file_handler.setFormatter(format)  # 设置文件输出格式

    #输出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel('DEBUG')
    console_handler.setFormatter(format)

    # 日志收集器与输出渠道进行对接
    logger.addHandler(file_handler) #输出到文件
    logger.addHandler(console_handler)#输出到控制台

    return logger

if __name__ == '__main__':
    log = get_logger()
    log.error("this is error")
    log.debug("this is debug")
