# function 练习
# 用户支付函数

def pay(balance, cost):
    if cost <= 0:
        return "金额不能小于等于0"
    if balance >= cost:
        return balance - cost
    else:
        return "余额不足"

# 日志函数
def log(user_id, username, cost):
    return f"[{user_id}] {username} 消费 {cost} 元"

# 主程序
user_id = 2333
username = "Jsutin"
balance = 9999.99

# 第一次消费
cost_1 = 100
balance = pay(balance, cost_1)
print(log(user_id, username, cost_1))
print(f"当前余额： {balance}")

# 第二次消费
cost_2 = 200
balance = pay(balance, cost_2)
print(log(user_id, username, cost_2))
print(f"当前余额: {balance}")

