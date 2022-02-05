# *
# *  @author Zhaoliang Ye 叶昭良(zl_ye@qny.chng.com.cn)
# *  @version V0.1
# *  @Title: anno.py.py
# *  @Description: (用一句话描述该文件做什么?)
# *  @Time: 2022/2/5 16:20
# *
import os
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# D:\code\PycharmCode\day4\Atm

# 日志文件夹
log_path = os.path.join(BASE_DIR + "/logs/atm.log")

def log(func):
    """
    日志记录模块
    """
    def wrapper(*args, **kwargs):
        f = open(log_path, "a", encoding="utf-8")
        f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\t"+func.__doc__+"\n")
        f.close()
        return func(*args, **kwargs)
    return wrapper

def verify(func):
    """账户验证"""
    def wrapper(self, *args, **kwargs):
        res = self.verify_account()
        if res == True:
            return func(self, *args, **kwargs)
        else:
            pass
    return wrapper


def payMethod(method=1):
    """
    支付方式：
        1. 微信
        2. 支付宝
        3. 银行卡
    """
    def out_wrapper(func):
        if method==1:
            print(f'微信支付')
            pay="weixin"
        elif method==2:
            print(f'支付宝支付')
            pay="alipay"
        else:
            print(f'银行卡支付')
            pay = "atm"
        """账户验证"""
        def wrapper(self, *args, **kwargs):
            res = self.verify_account()
            if res == True:
                return func(self, *args, **kwargs)
            else:
                pass
        return wrapper
    return out_wrapper