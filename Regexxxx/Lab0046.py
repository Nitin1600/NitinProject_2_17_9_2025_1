# import re
#
# Out = re.search("what to search", "where to search")

# import re
# inp_str = ("I am in India")
# out_str = re.search("India", inp_str)
# print(out_str)

# import re
#
# inp_str = "I am in India"
# out_str = re.search("id", inp_str)
# print(out_str)

# if out_str:
#     print("found")
# else:
#     print("not found")

# import re
#
# inp_str = "I am learning coding"
# out_str = re.search("Python|coding", inp_str)
# print(out_str)
#
# if out_str:
#     print("found")
# else:
#     print("not found")

# import re
#
# inp_str = "I am learning Python"
# # out_str = re.search("Python|coding", inp_str)
# # out_str = re.search("learning Python|coding", inp_str)
# out_str = re.search("learning Python|coding", inp_str)
# print(out_str)
#
# if out_str:
#     print("found")
#     print(out_str.group())
#     print(out_str.start())
#     print(out_str.end())
# else:
#     print("not found")

# import re
#
# exp = "IPv[46]"
# inp = '''Windows IP Configuration
#
# Ethernet adapter Ethernet 2:
#
#    Media State . . . . . . . . . . . : Media disconnected
#    Connection-specific DNS Suffix  . :
#
# Wireless LAN adapter Local Area Connection* 1:
#
#    Media State . . . . . . . . . . . : Media disconnected
#    Connection-specific DNS Suffix  . :
#
# Wireless LAN adapter Local Area Connection* 2:
#
#    Media State . . . . . . . . . . . : Media disconnected
#    Connection-specific DNS Suffix  . :
#
# Wireless LAN adapter Wi-Fi:
#
#    Connection-specific DNS Suffix  . : cisco.com
#    IPv6 Address. . . . . . . . . . . : 10.233.65.13
#    Subnet Mask . . . . . . . . . . . : 255.255.192.0
#    Default Gateway . . . . . . . . . : 10.233.64.1'''
#
#
# out= re.search(exp,inp)
# if out:
#     print(out.group())
# else:
#     print("not found")
#
# import re
# exp = "IPv[46]"
# inp='''Windows IP Configuration
#
#
# Ethernet adapter Ethernet 2:
#
#    Media State . . . . . . . . . . . : Media disconnected
#    Connection-specific DNS Suffix  . :
#
# Wireless LAN adapter Local Area Connection* 1:
#
#    Media State . . . . . . . . . . . : Media disconnected
#    Connection-specific DNS Suffix  . :
#
# Wireless LAN adapter Local Area Connection* 2:
#
#    Media State . . . . . . . . . . . : Media disconnected
#    Connection-specific DNS Suffix  . :
#
# Wireless LAN adapter Wi-Fi:
#
#    Connection-specific DNS Suffix  . : cisco.com
#    IPv6 Address. . . . . . . . . . . : 10.233.65.13
#    Subnet Mask . . . . . . . . . . . : 255.255.192.0
#    Default Gateway . . . . . . . . . : 10.233.64.1'''
# out = re.search(exp,inp)
# if out:
#     print(out.group())
# else:
#     print("not found")

# import re
# # exp = '10.126.102.[1][267]'# if we want to match
# exp = '10.126.102.[1][^267]'# if don't want to match use ^
# inp = """10.126.102.9
# 10.126.102.14
# 10.126.102.17
# 10.126.102.19
# 10.126.102.20
# 10.126.102.22
# 10.126.102.26
# """
#
# out = re.search(exp, inp)
# if out:
#     print(out.group())
# else:
#     print("not found")

# import re
#
# exp = "\d\d\d.\d\d\d"
# exp = "\d{3}.\d{3}"
# exp = "\d{1,3}.\d{1,3"
# out = re.findall(exp)
# print(out)

# import re

# inp = "In Python regular expressions, metacharacters are special characters that define patterns and have unique meaning"
# exp = "\w+"
# out = re.search(exp,inp)
# print(out.group())

# inp ="In Python regular expressions, metacharacters are special characters that define patterns and have unique meaning"
# exp ="\w+"
# out = re.search(exp,inp)
# print(out.group())

# import re

# inp = "aaa8901.8912bbb"
# exp = "\d+.\d+"
# out = re.search(exp,inp)
# if out:
#     print(out.group())
# else:
#     print("not found")
# import re
# inp = "aaa8901X8912bbb"
# exp="\d+.\d+"
# out = re.search(exp,inp)
# if out:
#     print(out.group())
# else:
#     print("not found")

# import re
#
# inp = "8901.8912"
# exp = r"^\d+.\d+$"
# out = re.search(exp,inp)
# if out:
#     print(out.group())
# else:
#     print("not found")
#
# inp = "8901.8912"
# exp=r"^\d+.\d+$"
# out = re.search(exp,inp)
# if out:
#     print(out.group())
# else:
#     print("not found")


# import re

# inp = "8901j8912"
# exp = r"^\d+\.\d+$"
# out=re.search(exp,inp)
# if out:
#     print(out.group())
# else:
#     print("not found")

# inp = "8901j8912"
# exp=r"^\d+\.\d+$"
# out = re.search(exp,inp)
# if out:
#     print(out.group())
# else:
#     print("not found")

# import re
#
# inp = "I n Python regular expressions, metacharacters are special characters that define patterns and have unique meaning - 99"
# # exp = r"(([a-z+])(\s*-\s*)) (\d+)"
# exp = r"(([a-z]+)(\s*-\s*)) (\d+)"
# out = re.search(exp,inp)
# if out:
#     print(out.group())
#     print(out.group(1))
#     print(out.group(2))
#     print(out.group(3))
#     print(out.group(4))

# import re
# exp = r"(\d{2}).\1"
# # exp = r"(\d{2}).\1"
# inp = "85.85"
# out = re.search(exp,inp)
# print(out)

# import re
#
# exp = r"(\d{2})(\d{2}).\2\1"
# inp = "8541.4185"
# out = re.search(exp,inp)
# print(out.group())
#
# exp = r"(\d{2})(\d{2}).\2\1"
# inp="8541.4185"
# out = re.search(exp,inp)
# print(out.group())

# import re
#
# result = re.findall(r"(\d+)", "abc123xyz456")
# print(result)

# import re
#
# result = re.finditer(r"(\d+)","abc123xyz456")
# for num in result:
#     print(num.group())

# import re
# Result = re.sub(exp,replace,inp,flags=re.|)

# import re
#
# text = "Hello World! Hello Universe!"
# result = re.sub(r"Hello","Hi",text)
# print(result)

# import re
#
# re.split(exp,inp,maxsplit=0)

# import re
#
# text = "Apple;Banana,Orange|Grape"
# result = re.split(r"[;|,]",text)
# print(result)

import paramiko

import paramiko
import time
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('10.104.253.207', port=22, username='root',
            password='Cisco@123', timeout=3)
# Open interactive shell
shell = client.invoke_shell()

# Send a command
shell.send("ls -l\n")
time.sleep(1)  # wait for command to execute

# Receive output
output = shell.recv(5000).decode("utf-8")
print(output)

# Send another command
shell.send("pwd\n")
time.sleep(1)
print(shell.recv(5000).decode("utf-8"))

# Close connection
client.close()

# import logging
#
# logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
# logger = logging.getLogger("MyLogger")
# logger.info("Hello from logger")




