# *
# *  @author Zhaoliang Ye 叶昭良(zl_ye@qny.chng.com.cn)
# *  @version V0.1
# *  @Title: Users.py
# *  @Description: 用户类
# *  @Time: 2022/2/5 16:22
# *
import os
import sys
from annotation.anno import log, verify
from core.Atms import ATM

### 知识点： 模块名和类名不能一致，否则报错  import失败， 即 User模块文件，不能包含User class，否则导入User类失败
class User(object):
    """用户接口"""
    def __init__(self, id, password):
        self.id=id
        self.password=password

    ## 知识点 装饰这模式
    @log
    @verify
    def set_password(self, password):
        """更新密码"""
        atm =ATM()
        user = atm.get_user(self.id)
        user["password"] = password
        atm.set_user(user)
        print("密码修改成功")

    @verify
    def get_balance(self):
        """获取余额"""
        atm = ATM()
        user = atm.get_user(self.id)
        return user["balance"]


    def _add_balance(self, money):
        """增加余额,不需要验证账户"""
        atm = ATM()
        user = atm.get_user(self.id)
        if user != None:  # 验证账户存在
            user["balance"] += money
            if user["balance"] >= -user["limit"]:
                atm.set_user(self.id, user)
                return True
        return False

    @verify
    def _reduce_balance(self, money):
        """减少余额"""
        return self._add_balance(-money)

    @log
    def draw_money(self,money):
        """提现取款 年利率5%"""
        service_charge = int(money * 0.05)
        total = money + service_charge
        res = self._reduce_balance(total)
        if res == True:
            print(f'取款成功，金额 {money},  手续费：{service_charge}' )
        else:
            print("取款失败,余额不足")
        return res

    @log
    def repayment(self,money):
        """还款   """
        res = self._add_balance(money)
        if res ==True:
            print("还款成功")
        else:
            print("还款失败")
        return res

    @log
    def payment(self,money):
        """付款: 银行卡付款和 信用卡付款两种方式"""
        res = self._reduce_balance(money)
        if res == True:
            print("付款成功")
        else:
            print("付款失败,余额不足")
        return res

    @log
    def show_info(self):
        """打印信息"""
        print("账户信息：")
        print("账户ID：",self.id)

    @log
    def remit(self, id, money):
        """转账汇款"""
        reduce_res = self._reduce_balance(money)  #取款
        if reduce_res == True:
            user = User(id, None)
            add_res = user._add_balance(money)  # 存款
            if add_res ==True:
                print("转账成功")
            else:
                self._add_balance(money)  # 存款失败，打回取款账户
                print("转账失败，对方用户异常")
        else:
            print("转账失败，余额不足")

    def verify_account(self):
        """登陆验证,return: {bool} True为通过，False为失败"""
        atm = ATM()
        user = atm.get_user(self.id)
        is_pass = False
        if user == None:
            print("账户验证失败：卡号不存在！")
        else:
            if self.password == user["password"]:
                # print("账户验证成功！")
                is_pass = True
            else:
                print("账户验证失败：密码错误！")
        return is_pass
