# 正则表达式练习
import re

# 匹配手机号
phone = "1380013800"
pattern = r"^1[3-9]\d{9}$"
result = re.match(pattern, phone)

if result:
    print("手机号格式正确")
else:
    print("手机号格式错误")

# 匹配纯英文用户名
username = "Justin123"
user_pattern = r"^[a-zA-Z0-9_][3,16]$"
if re.match(user_pattern, username):
    print("用户名格式正确")
else:
    print("用户名格式错误")