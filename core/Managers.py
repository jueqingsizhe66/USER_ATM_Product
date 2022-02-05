# *
# *  @author Zhaoliang Ye 叶昭良(zl_ye@qny.chng.com.cn)
# *  @version V0.1
# *  @Title: Managers.py
# *  @Description: 管理员账户类
# *  @Time: 2022/2/5 16:24
# *
from annotation.anno import log, verify
from core.Atms import ATM


class Manager(object):
    """管理接口"""
    def __init__(self, manager_id, manager_password):
        self.id=manager_id
        self.password=manager_password

    @log
    @verify
    def add_user(self, password, balance=0, limit=1500, isLock=False):
        """添加新用户"""
        atm = ATM()
        user_id = atm.add_user(password, balance, limit, isLock)
        print("账户添加成功，id = %s" % user_id)

    @log
    @verify
    def remove_user(self, id):
        """删除账户 id{str} 账户id"""
        atm = ATM()
        res = atm.remove_user(id)
        if res:
            print("账户删除成功")
        else:
            print("账户不存在")

    @log
    @verify
    def set_user_limit(self, id, limit):
        """设置用户额度"""
        atm = ATM()
        user = atm.get_user(id)
        user["limit"] = limit
        atm.set_user(id, user)
        print("额度修改成功，当前额度为： %s " % limit)

    @verify
    def set_user_islock(self, id, islock):
        """修改账户状态，锁定，解锁"""
        atm = ATM()
        user = atm.get_user(id)
        user["isLock"] = islock
        atm.set_user(id, user)
        print("账户修改成功，当前状态为： %s " % ("锁定" if islock else "正常"))

    def verify_account(self):
        """登陆验证
        :return: {bool} True为通过，False为失败
        """
        atm = ATM()
        manager = atm.get_manager()
        is_pass = False
        if self.id != manager["id"]:
            print("账户验证失败：卡号不存在！")
        else:
            if self.password != manager["password"]:
                print("账户验证失败：密码错误！")
            else:
                print("账户验证成功！")
                is_pass = True
        return is_pass
