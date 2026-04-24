# for 循环练习

user_list = ["小明","小红","小刚","张三"]

# 遍历所有用户
for user in user_list:
    print(f"欢迎： {user} 登录系统")

# 循环 + 计算
prices = [10, 20, 30, 40]
total = 0

for p in prices:
    total = total + p

print(f"\n总金额： {total}")
