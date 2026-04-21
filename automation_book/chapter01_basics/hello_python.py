#练习：变量、数据类型与基础运算

# 变量和数据类型
user_id = 2333          #整数类型
user_name = "Justin"    #字符串类型
is_active = True        #布尔类型
balance  = 9999.99      #浮点数类型

# 输出变量信息
print("--- 用户信息 ---")
print(f"用户ID: {user_id}")
print(f"用户名： {user_name}")
print(f"是否在线： {is_active}")
print(f"账户余额： {balance}")

# 基础运算
pay = 20.0
new_balance = balance - pay
print(f"消费20元,剩余余额： {new_balance:.2f}")

# 字符串拼接
log_messgae = f"[{user_id}]{user_name}消费了{pay}元，余额更新为{new_balance:.2f}"
print("\n系统日志")
print(log_messgae)