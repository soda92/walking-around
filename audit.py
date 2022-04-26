import sys

def audit_hook(event, args):
    if event in ['urllib.Request']:
        print(f"Network {event=} {args=}")

sys.addaudithook(audit_hook)

import urllib.request
try:
    urllib.request.urlopen("http://example.com")
except:
    pass