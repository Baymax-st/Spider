import requests
import os

def get_image(url, path, headers=None):
    try:
        root, imageName = os.path.split('/')
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url, timeout=30, headers=headers)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
            print('图片保存成功')
        else:
            print('图片已存在')
    except Exception as e:
        print("产生异常",'\n', e)

if __name__ == '__main__':
    # 设置图片保存路径和URL
    root = 'D://'
    url = 'https://photocdn.tv.sohu.com/img/20210223/pic_org_0dd7a68a-38f1-4874-bd64-441db1b1a0a2.png'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    path = os.path.join(root,'剧照.png')
    get_image(url, path, headers)  # 获取图片
