#!/usr/bin/env python3

from setuptools import setup

setup(
    name="whatami",
    version="1.0.0",
    description="You'd better have some thick skin...or a thick skull!",
    long_description=open("README.md").read(),
    license="MIT",
    packages=["libwhatami"],
    scripts=["whatami"],
    package_data={"libwhatami": ["data/*"]},
)
