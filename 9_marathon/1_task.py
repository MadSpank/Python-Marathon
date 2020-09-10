# # len(data) == len(set(data)) and len(data) > 1
# # all(-1 < int(n) < 256 for n in d.split(".") for d in data)
# import re
# data = ["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]
# a = (re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$ ",d) for d in data)
# b = [num.split('.') for num in data]
# print(data)
import this