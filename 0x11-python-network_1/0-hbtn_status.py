#!/usr/bin/python3
"""import module"""

if __name__ == "__main__":
    from urllib import request
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        if response.getcode() == 200:
            content_bytes = response.read()
            content = content_bytes.decode('utf-8')
            print('Body response:')
            print('    - type: {}'.format(type(content_bytes)))
            print('    - content: {}'.format(content_bytes))
            print('    - uft8 content: {}'.format(content))
