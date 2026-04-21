# 练习：input输入 + 类型转换
# 模拟用户输入消费金额，计算余额

# 基础数据
user_id = 2333
username = "Justin"
balance = 9999.99

# 获取用户输入
cost = float(input("请输入本次消费金额（单位：元）："))

# 计算新余额
new_balance = balance - cost

# 输出结果
print(f"\n=== 消费完成 ===")
print(f"用户名： {username}")
print(f"原余额： {balance}")
print(f"消费金额： {cost}")
print(f"最新余额：  {new_balance:.2f}")

# 系统日志
log = f"[{user_id}] {username} 消费{cost}元，余额： {new_balance}"
print("\n日志:",  log)