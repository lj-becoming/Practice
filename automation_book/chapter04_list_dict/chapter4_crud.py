# 字典 增删改查 练习
user = {
    "id": 2333,
    "name": "Justin",
    "balance": 9999.99
}

# 查
print(f"姓名： {user["name"]}")

# 改
user["balance"] = 8888.88
print(f"修改后余额： {user["balance"]}")

# 增
user["phone"] = "1380013800"
print(f"添加手机号后： {user}")

# 删
del user["phone"]
print(f"删除手机号后： {user}")

# 列表操作
user_list = []

# 增加元素
user_list.append(user)
print(f"列表添加用户: {user_list}")

# 遍历
for u in user_list:
    print(f"ID: {u['id']}， 姓名： {u['name']}")