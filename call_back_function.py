# -*- coding: utf-8 -*-
# ----------------------------
#!  Copyright(C) 2019
#   All right reserved.
#   文件名称：xxx.py
#   摘   要：xxx
#   当前版本:1.0
#   作   者：崔宗会
#   完成日期：2019-x-x
# -----------------------------


def func_callback(func1, args):
    print("调用函数:")
    func1(args)
    print("____________________")


def f1(x):
    print("回调函数启动:", x)


func_callback(f1, 100)


def func_callback_tuple(func2, *args):
    print("回调函数和元组相结合：")
    func2(args)  # 这里的“*”号可以有，也可以省略。
    print("____________________")


def f2(*x):
    print("带tuple参数回调函数启动：")
    print(type(x), x)



func_callback_tuple(f2, 99, 98, 97, 96)


def func_callback_dic(func, **kwargs):
    print("回调函数和字典相结合：")
    func(**kwargs)  # 两个星号要加上，不能省略
    print("____________________")


def f3(**x):
    print("带dict参数回调函数启动：")
    print(type(x), x)
    print(x['aa']+x['bb']+x['cc'])


func_callback_dic(f3, aa=1, bb=2, cc=3)
