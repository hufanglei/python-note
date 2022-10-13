import time

# s_time = time.time()
# # 打印时间戳
# print(time.time())
#
# time.sleep(3)
#
# print(f"cost {time.time() - s_time }")
print(time.localtime(1333333000))
# 0时区时间
# print(time.gmtime())
# # 时间转时间戳
# print(time.mktime(time.localtime()))
# # 格式化时间 时间转字符串
# print(time.strftime("%Y-%m/%d"))  #时间转字符串

# time_str = time.strftime("%Y-%m-%d %H:%M:%S")
# print(time.strptime(time_str, "%Y-%m-%d %H:%M:%S"))

import datetime

d = datetime.datetime.now()
print(d.today())
print(d.timetuple())
print(datetime.datetime.fromtimestamp(22222))

print(d + datetime.timedelta(5))
# -5天 加4个小时
print(d + datetime.timedelta(-5, hours=5))
# 指定日期
print(d.replace(year=2120, month=8))
