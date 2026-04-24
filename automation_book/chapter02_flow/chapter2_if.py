# 练习：控制流
# 场景：判断用户余额是否足够支付

# 用户数据
user_id = 2333
username = "Justin"
balance = 9999.99

# 输入消费金额
cost = float(input("请输入消费金额："))

# 判断余额是否足够
if balance >= cost:    #余额足够
    new_balance = balance  - cost
    print(f"\n支付成功")
    print(f"余额：{balance}")
    print(f"消费：{cost}")
    print(f"剩余：{new_balance}")
else:      #余额不足
    print(f"\n支付失败")
    print(f"余额不足！当前余额：{balance}")

# 日志
log = f"[{user_id}]{username} 尝试消费{cost}元"
print("\n日志:", log)


