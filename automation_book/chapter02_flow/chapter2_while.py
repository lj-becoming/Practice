# while循环练习
# 场景：用户反复消费，直到退出

# 用户数据
username = "Justin"
balance = 9999.99

# 消费系统
while True:
    print("\n=== 消费系统 ===")
    print("1. 消费")
    print("2. 退出")

    choice = input("请选择操作（1/2）：")

    if choice == "2":
        print("退出系统，欢迎下次光临！")
        break

    elif choice == "1":
        cost = float(input("输入消费金额："))

        if balance >= cost:
            balance = balance - cost
            print(f"支付成功！剩余：{balance:.2f}")

        else:
            print("余额不足")
    
    else:
        print("输入错误，请重新选择！")