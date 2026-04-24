# 定义函数：计算支付后的余额
def pay_balance(balance, cost):
    if balance >= cost:
        return balance - cost
    else:
        return "余额不足"
    
# 主程序
current_balance = 9999.99
cost = 50

# 调用函数
result = pay_balance(current_balance, cost)

print("原余额：", current_balance)
print("消费：", cost)
print("结果:", result)
