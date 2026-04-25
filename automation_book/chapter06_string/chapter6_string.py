# 字符串常用操作(后端日志、参数、接口)

# 基础字符串
username = "  Justin  "
phone = "138-0013-8000"

# 去除空格
username_clean = username.strip()
print(f"清理后用户名： {username_clean}")

# 替换字符
phone_clean = phone.replace("-", "")
print(f"清理后手机号： {phone_clean}")

# 格式化输出
user_id = 2333
balance = 9999.99

log = f"[INFO] 用户{user_id}({username_clean}) 余额： {balance}"
print(log)

# 判断是否包含管检测
if "Jusitn" in username_clean:
    print("匹配到目标用户")

    