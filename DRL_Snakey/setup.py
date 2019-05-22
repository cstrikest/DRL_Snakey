#!/usr/bin/env python3

__author__ = "Yxzh"

from setuptools import setup, find_packages


with open("README.md", "r") as fh:
	long_description = fh.read()
with open('requirements.txt') as f:
	requirements = [l for l in f.read().splitlines() if l]
setup(
	name = "DRL_Snakey",  # 项目名
	version = "0.9",  # 版本号
	description = "A Deep Reinforcement Learning study package. With game environment.",  # 简介
	long_description = long_description,  # 长简介 这里使用的 readme 内容
	long_description_content_type = "text/markdown",
	license = "GPL",  # 授权
	install_requires = requirements,  # 依赖
	author = "YANG Xuezhi",  # 作者
	author_email = "cstrikest@gmail.com",  # 邮箱
	url = "https://github.com/cstrikest/DRL_Snakey",  # 地址
	packages = find_packages(),
	zip_safe = True
)
