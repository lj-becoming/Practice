# 文件读写练习
import os

dir = os.getcwd()
path_hello = os.path.join(dir, "hello.txt")

# open()打开文件
hello_file = open(path_hello, "r")

# read()读取文件
hello_content = hello_file.read()
print(hello_content)

"""
或者使用for循环读取文件
for line in hello_file:
    print(line)
"""

sonnet_file = open("sonnet29.txt")
print(sonnet_file.readlines())
sonnet_file.seek(0)    # 回到文件开头
print(sonnet_file.read())

# 写入文件
beef_file = open("beef.txt", "w")
beef_file.write("Hello world!\n")
beef_file.close()
beef_file = open("beef.txt", "a")
beef_file.write("beef is not a vegetable.")
beef_file.close()
beef_file = open("beef.txt", "r")
beef_connet = beef_file.read()
beef_file.close()
print(beef_connet)