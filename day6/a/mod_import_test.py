import sys
import os

d6path = 'E:\\ideawork\\pythonproject\\py8day_camp\\day6'
print(__file__)  # 打印当前脚本文件路径
print(os.path.dirname(__file__))  # 打印当前脚本文件路径
base_path = os.path.dirname(os.path.dirname(__file__))
print(os.path.dirname(os.path.dirname(__file__)))  # 打印当前脚本文件路径
# print(sys.path)
# sys.path.append(d6path)
# print(sys.path)
sys.path.append(base_path)
import my_first_mod
