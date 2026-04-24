# list & dict 练习
# 列表list： 有序数据集合
users = ["Justin", "Tom", "Jerry"]
balances = [9999.99, 555, 22]

# 字典 dict: 键值对
user_1 = {
    "id": 2333,
    "name": "Justin",
    "balance": 9999.99,
    "is_vip": True
}

# 嵌套： 列表 + 字典
user_list = [
    {"id": 1001, "name": "Tom", "balance": 555},
    {"id": 1002, "name": "Jerry", "balance": 22},
    {"id": 2333, "name": "Justin", "balance": 9999.99}
]

print(f"用户1信息： {user_1}")
print(f"用户名： {user_1["name"]}")
print(f"账户余额： {user_1["balance"]}")

# 循环打印所有用户
print("\n=== 全部用户 ===")
for u in user_list:
    print(f"ID: {u["id"]} 姓名： {u["name"]} 余额： {u["balance"]}")
