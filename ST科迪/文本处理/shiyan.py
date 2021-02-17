import requests


# =============获取代理ip===============
def get_ip():
    response = requests.get(
        'http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=6226c130427f487385ad7b5235bc603c&count=5&expiryDate=0&format=2&newLine=3')
    if response.status_code == 200:
        if response.text[0] == '{':
            print('获取ip失败')
        else:
            return response.text.split('\n')[:-1]
    else:
        print('请求失败')
        print(response)


def get_data():
    ip = get_ip()
    # ip = 1
    while ip == None:
        ip = get_ip()
        if ip:
            proxies = {'http': f'http://{ip[0]}',
                       'https': f'https://{ip[1]}'}
            response = requests.get('https://cd.fang.anjuke.com/loupan/all/p2/', proxies=proxies)
            if response.status_code == 200:
                print(response.text)
                break
            else:
                print('请求失败')
                print(response)
                break

"""
['60.167.102.57:46674', '114.224.113.51:41162', '60.167.103.207:23267', '115.219.0.192:23061', '114.231.7.4:45872']
"""

# proxy = {'http': ip[1], 'https':ip[1]}
if __name__ == '__main__':
    get_data()

