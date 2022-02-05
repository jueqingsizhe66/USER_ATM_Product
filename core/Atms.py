import json

from core.Users import User


class ATM(object):
    """实现ATM，用户信息的增删改查，管理员信息获取
    # 此处如果需要支持多个账户同时登陆，
    # 需要为每个用户建立独立的文件来存放信息，
    # 避免同时读写时信息不统一
    ## 知识点  类的新式写法和老式写法
    """
    def get_users(self):
        """获取所有账户信息,return{dict}"""
        with open("../db/user.json", "r", encoding="utf-8") as f:
            users = json.load(f)
            return users

    def set_users(self, users):
        """设置所有用户信息,users{dict}"""
        with open("../db/user.json", "w", encoding="utf-8") as f:
            json.dump(users, f, indent="\t")
            return True

    def get_user(self, id):
        """获取单个用户信息,id{str},return{dict}"""
        users = self.get_users()
        user = users.get(id)
        return user

    def set_user(self,id, user):
        """设置单个用户信息,id{str},user{dict}"""
        users = self.get_users()
        users[id]=user
        self.set_users(users)

    def remove_user(self,id):
        """删除单个用户信息,id{str}"""
        users = self.get_users()
        if users:
            users.pop(id)
            self.set_users(users)
            return True
        else:
            return False

    def add_user(self, password, balance, limit, isLock):
        """添加新用户
        :param password: {str}密码
        :param balance: {int}余额
        :param limit: {int}额度
        :param isLock: {bool}是否锁定
        :return: id{str}新用户id
        """
        users = self.get_users()
        max_id = "000000"
        if users != {}:
            max_id = max(users.keys())
        cur_id = str(int(max_id) + 1).zfill(6)  # id自动+1，补足6位
        users[cur_id] = {
            "password": password,
            "balance": balance,
            "limit":limit,
            "isLock":isLock
        }
        self.set_users(users)
        return cur_id

    def get_manager(self):
        """获取管理员信息,return{dict}"""
        with open("../db/manager.json", "r") as f:
            manager = json.load(f)
            return manager




def main():
    user = User("000001","123456")
    user.repayment(1000)
    user.draw_money(100)

if __name__ == "__main__":
    main()