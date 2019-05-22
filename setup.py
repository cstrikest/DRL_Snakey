#!/usr/bin/env python3

__author__ = "Yxzh"

from setuptools import setup, find_packages


with open("README.md", "r") as fh:
	long_description = fh.read()
setup(
	name = "DRL_Snakey",
	version = "1.1.1r",
	description = "A Deep Reinforcement Learning study package. With game environment.",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	license = "GPL",
	include_package_data = True,
	install_requires = [
		"numpy",
		"tensorflow",
		"h5py",
		"pygame",
		"matplotlib"
	],
	author = "YANG Xuezhi",
	author_email = "cstrikest@gmail.com",
	url = "https://github.com/cstrikest/DRL_Snakey",
	packages = find_packages(),
	zip_safe = True,
	classifiers = [
		"Programming Language :: Python :: 3.6",
		"Environment :: MacOS X",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
		"Natural Language :: Chinese (Simplified)",
		"Topic :: Scientific/Engineering :: Artificial Intelligence",
	],
)
