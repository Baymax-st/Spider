# BeautifulSoup库学习

## 基础认知

- 说明：html文件是由标签对（一对尖括号）包裹内容的格式书写，`BeautifulSoup库`是解析、遍历、维护 "标签树" 的功能库
```markdown
以<p>···</p>为例：
<p class="title">···</p>
其中p为标签名称，class为标签属性(Attributes)，可以有0个或者多个定义标签的特性，是一个键值对。
```

## BeautifulSoup库的使用

### BeautifulSoup库的导入

```python
from bs4 import BeautifulSoup
```
或者
```python
import bs4
```

### 用BeautifulSoup类解析html

```python
soup = BeautifulSoup('替换为html文本内容', 'lxml')
```
其中lxml为解析方式，还可以替换为 "lxml", "xml", "html.parser", 或者 "html5lib"

`lxml、 xlm、 html5lib1`都需要使用 `pip install xxx`先下载对应的库

经过以上语句将html中的标签树转化为BeautifulSoup类

### BeautifulSoup类的基本元素

```markdown
|       基本元素        | 说明                                                    |
|:-----------------:|:------------------------------------------------------|
|       `Tag`       | 标签，最基本的信息组织单元，分别用<>和</>标明开头和结尾                        |
|      `Name`       | 标签名称，<p>…</p>的名字是'p',调用格式：<tag>.name                  |
|   `Attributes`    | 标签属性，<p class="title">…</p>的属性是class，调用格式：<tag>.attrs |
| `NavigableString` | 标签内容，<p class="title">…</p>的内容是'…'，调用格式：<tag>.string  |
|     `Comment`     | 标签内容的注释部分，一种特殊的Comment类型                              |
```

### BeautifulSoup类的常用方法

#### 获取标签的基本信息

- `soup.name`：获取标签名称
- `soup.attrs`：获取标签属性
- `soup.string`：获取标签内容
- `soup.text`：获取标签内容，返回unicode格式

#### 下行遍历
- `soup.contents`：获取标签的所有子节点，返回列表格式
- `soup.children`：获取标签的所有子节点，返回迭代器格式
- `soup.descendants`：获取标签的所有子孙节点，返回迭代器格式

#### 上行遍历
- `soup.parent`：获取标签的父节点
- `soup.parents`：获取标签的所有祖宗节点，返回迭代器格式，含本身

#### 平行遍历
- `soup.next_sibling`：获取标签的下一个兄弟节点
- `soup.previous_sibling`：获取标签的上一个兄弟节点
- `soup.next_siblings`：获取标签的所有下一个兄弟节点，返回迭代器格式
- `soup.previous_siblings`：获取标签的所有上一个兄弟节点，返回迭代器格式

#### 查找标签
- `soup.find_all(name, attrs, recursive, string)`：查找标签
- `soup.find(name, attrs, recursive, string)`：查找标签
- `soup.find_parent(name, attrs, recursive)`：查找父节点
- `soup.find_parents(name, attrs, recursive)`：查找父节点
- `soup.find_next_sibling(name, attrs, recursive)`：查找下一个兄弟节点
- `soup.find_next_siblings(name, attrs, recursive)`：查找后续兄弟节点
- `soup.find_previous_sibling(name, attrs, recursive)`：查找上一个兄弟节点
- `soup.find_previous_siblings(name, attrs, recursive)`：查找前序兄弟节点

**参数介绍:** 

- `name` 字符串或列表类型，按标签名称查找标签，当`name==True`显示所有标签，可以使用正则表达式`re.compile('b')`,获取名称中包含`b`的标签
- `attrs` 对标签属性值的检索字符串，可以检索包含某属性或者某属性为某一值的标签`tag.find_all(id=re.compile('link'))`
- `recursive` 默认为True，表示查找所有子孙节点，否则只查找儿子节点
- `string` 检索标签之间字符串的内容





