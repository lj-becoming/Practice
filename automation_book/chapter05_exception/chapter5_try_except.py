# 异常处理：防止程序崩溃
username = "Justin"
balance = 8888.88

try:
    # 尝试执行的代码
    cost = float(input("请输入消费金额："))

    if balance >= cost:
        balance = balance - cost
        print(f"支付成功，余额为： {balance: .2f}")
    else:
        print("余额不足")

except ValueError:
    # 出现错误时执行
    print("输入错误！请输入数字！")