#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简易命令行计算器
功能：加、减、乘、除、连续计算
适合新手学习 & GitHub 展示
"""

def add(a, b):
    """加法"""
    return a + b

def subtract(a, b):
    """减法"""
    return a - b

def multiply(a, b):
    """乘法"""
    return a * b

def divide(a, b):
    """除法（处理除零错误）"""
    if b == 0:
        return "错误：除数不能为 0"
    return a / b

def main():
    print("=" * 30)
    print("    🎉 Python 标准计算器 🎉")
    print("=" * 30)
    print("支持操作：")
    print("  +  加法")
    print("  -  减法")
    print("  *  乘法")
    print("  /  除法")
    print("  q  退出")
    print("=" * 30)

    while True:
        # 获取用户输入
        choice = input("\n请输入运算符（+ - * /），或输入 q 退出：")

        # 退出条件
        if choice.lower() == "q":
            print("👋 感谢使用计算器，再见！")
            break

        # 判断是否是有效运算符
        if choice not in ["+", "-", "*", "/"]:
            print("❌ 无效输入，请重新输入！")
            continue

        # 尝试获取数字
        try:
            num1 = float(input("请输入第一个数字："))
            num2 = float(input("请输入第二个数字："))
        except ValueError:
            print("❌ 错误：请输入有效的数字！")
            continue

        # 计算
        if choice == "+":
            result = add(num1, num2)
        elif choice == "-":
            result = subtract(num1, num2)
        elif choice == "*":
            result = multiply(num1, num2)
        elif choice == "/":
            result = divide(num1, num2)

        # 输出结果
        print(f"\n✅ 结果：{num1} {choice} {num2} = {result}")

# 程序入口
if __name__ == "__main__":
    main()