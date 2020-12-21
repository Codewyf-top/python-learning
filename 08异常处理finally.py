# -*- coding: utf-8 -*-
"""
@Time ： 21/12/2020 20:13
@Auth ： Codewyf
@File ：08异常处理finally.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating

"""
import sys
try:
    f = open('file.txt', r)
    ....# some data processing
except OSError as err:
    print("OS error: {}".format(err))
except:
    print('Unexpected error:', sys.exc_info()[0])
finally:
    f.close()
"""
这段代码中，try block 尝试读取 file.txt 这个文件，并对其中的数据进行一系列的处理，
到最后，无论是读取成功还是读取失败，程序都会执行 finally 中的语句——关闭这个文件流，
确保文件的完整性。因此，在 finally 中，我们通常会放一些无论如何都要执行的语句。
值得一提的是，对于文件的读取，我们也常常使用 with open，你也许在前面的例子中已经看到过，
with open 会在最后自动关闭文件，让语句更加简洁。
"""