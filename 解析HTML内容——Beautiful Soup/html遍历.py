from bs4 import BeautifulSoup
import os

if __name__ == '__main__':
    url = 'http://python123.io/ws/demo.html'
    headers = {'User-Agent': 'Mozilla/5.0'}
    root = r'F:\Spider\解析HTML内容——Beautiful Soup'
    name = 'python123.html'
    path = os.path.join(root, name)
    # print(path)
    with open(path, 'r') as f:
        html = f.read()
        soup = BeautifulSoup(html, 'lxml')

    # 下行遍历
    # 使用tag.contents获取标签下的所有子标签
    head = soup.head
    print(head.contents)  # 获取head标签下的所有子标签
    body = soup.body
    print(body.contents)  # 获取body标签下的所有子标签
    # 使用tag.children获取标签下的所有子标签
    for child in body.children:
        print(child)
    # 使用tag.descendants获取标签下的所有子标签，包括孙子标签
    for child in body.descendants:
        print(child)

    # 上行遍历
    # 使用tag.parent获取标签的父标签
    print(head.parent)
    # 使用tag.parents获取标签的所有父标签
    for parent in head.parents:
        if parent is None:
            break
        else:
            print(parent)  # 获取head标签的所有父标签

    # 平行遍历
    print(head.next_sibling)  # 获取head标签的下一个兄弟标签，无兄弟节点时返回None
    for sibling in head.next_siblings:
        if sibling is None:
            break
        else:
            print(sibling)
    print(head.previous_sibling)  # 获取head标签的上一个兄弟标签，无兄弟节点时返回None
    for sibling in head.previous_siblings:
        if sibling is None:
            break
        else:
            print(sibling)

