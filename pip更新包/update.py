# -*- coding: utf-8 -*-
"""
@Time ： 11/12/2020 12:54
@Auth ： Codewyf
@File ：update.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""
import pip
from subprocess import call
from pip._internal.utils.misc import get_installed_distributions
for dist in get_installed_distributions():
    call("pip install --upgrade " + dist.project_name, shell=True)