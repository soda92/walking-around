import sys


def audit_hook(event, args):
    if event in ["urllib.Request", "os.remove"]:
        print(f"{event=} {args=}")
        if event == "os.remove":
            sys.exit(-1)


sys.addaudithook(audit_hook)

import urllib.request

try:
    urllib.request.urlopen("http://example.com")
except:
    pass

with open("file.txt", mode="w") as f:
    f.write("hello world\n")

from os import remove

remove("file.txt")
