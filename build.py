"""Builds the installers
"""
from os import remove
from subprocess import check_call
from shutil import copyfile, rmtree

# Copy README file to filename acceptable by setup.
copyfile("README.md", "README")

check_call(["python", "setup.py", "sdist"])
check_call(["python", "setup.py", "bdist_wheel", "--universal"])

remove("README")
rmtree("build")
