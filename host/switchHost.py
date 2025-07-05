
import requests
import io
import re

# 从接口获取host列表，然后修改本地hosts文件，同名的host只保留第一个
def switchHost(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            hosts = response.text.split('\n')
            hosts = [host for host in hosts if host != '' and host.startswith('#') == False]
            path = r'C:\Windows\System32\drivers\etc\hosts'
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
            arr = text.split('\n')
            m = []
            for line in arr:
                if not 'github' in line:
                    m.append(line)
            m.append('\n'.join(hosts))
            text = '\n'.join(m)
            print(text)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(text)
                print('write hosts file success. please ipconfig /flushdns')
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

switchHost('https://raw.hellogithub.com/hosts')