# 练习
import os

# 添加路径分隔符
a = os.path.join("usr", "bin", "span")
print(a)

## 测试用，非真实文件
my_files = ["accounts.txt", "details.csv", "invite.docx"]
for filename in my_files:
    print(f"测试用： {os.path.join("~/documents", filename)}") #  print(os.path.join(os.path.expanduser("~/documents"), filename)) 真实情况下应展开

# 当前工作目录
b = os.getcwd()
print(f"当前工作目录： {b}")

# 修改当前工作目录
c = os.path.expanduser("~/Practice")
os.chdir(c)
d = os.getcwd()
print(f"修改后的当前工作目录： {d}") 

# 创建新文件夹
os.chdir(b) # 回到练习文件所在目录
path_folder = os.path.join(b, "food", "fruit", "apple")
os.makedirs(path_folder, exist_ok = True)
print("文件夹已创建")

# 处理绝对路径和相对路径
e = os.path.abspath(".")
print(f"绝对路径（当前工作目录）： {e}")
f = os.path.abspath(os.path.join(".", "food"))
print(f"绝对路径（food目录）： {f}")
g = os.path.isabs(".")
print(f"参数情况： {g}")
h = os.path.isabs(e)
print(f"参数情况： {h}")

## 计算相对路径
i = os.path.relpath(path_folder, b)
print(i)

## 目录名称和基本名称
j = os.path.join(b, "chapter8.1_files_and_file_paths.py")
print(f"本文件的路径： {j}")
print(f"基本名称： {os.path.basename(j)}")
print(f"目录名称： {os.path.dirname(j)}")
print(f"目录名称和基本名称： {os.path.split(j)}")
print(f"文件夹字符串列表： {j.split(os.path.sep)}")

# 查看文件名和文件夹大小
file_size = os.path.getsize(j)
print(f"本文件的大小(byte)： {file_size}")
print(f"当前文件所处目录的所有文件名： {os.listdir(b)}")

total_size = 0
k = "/home/justin/Practice/automation_book"
for filename in os.listdir(k):
    total_size = total_size + os.path.getsize(os.path.join(k, filename))
print(f"我的练习代码文件大小（byte）: {total_size}")

# 检查路径有效性
if os.path.exists(b):print(f"{b} 所指文件夹（或文件）存在")
else:print(f"{b} 所指文件夹（或文件）不存在")

if os.path.isfile(b):print(f"{b} 所指文件存在")
else:print(f"{b} 所指文件不存在")

if os.path.isdir(b):print(f"{b} 所指文件夹存在")
else:print(f"{b} 所指文件夹不存在")