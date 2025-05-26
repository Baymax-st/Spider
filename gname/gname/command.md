## 创建一个爬虫项目

```bash
scrapy startproject <project_name>
# <project_name> 是项目名称，不能包含空格和特殊字符
# 例如：创建一个名为 myproject 的项目
scrapy startproject myproject
```
运行以上命令后，会在当前目录下创建一个名为 myproject 的文件夹，里面包含了 Scrapy 项目的基本结构和文件。

项目结构如下：

```
myproject/
    scrapy.cfg
    myproject/
        __init__.py
        items.py
        middlewares.py
        pipelines.py
        settings.py
        spiders/
            __init__.py
```

## 创建一个爬虫

```bash
scrapy genspider <spider_name> <domain>
# <spider_name> 是爬虫名称，<domain> 是爬虫要抓取的网站域名
```
运行以上命令后，会在 spiders 目录下创建一个名为 <spider_name>.py 的文件，里面包含了爬虫的基本代码结构。

项目文件的基本结构如下：

```
myproject/
    scrapy.cfg
    myproject/
        __init__.py
        spiders/
            __init__.py
            <spider_name>.py
        items.py
        middlewares.py
        pipelines.py
        settings.py
```

## 介绍其中项目文件的作用

`scrapy.cfg` 是配置文件，不需要改动，不能删除
`items.py` 用来定义爬取出来的数据类型，基本语法是 `name= scrapy.Field()`, 其中name是对数据名的规范
`spider_name.py` 是用来输入初始网页和解析Response对象，获取数据的,解析方式有`xpath() css() json()`，以item的方式返回数据给pipeline(经过引擎)
`pipilines.py` 用来定义管道，即解析后的数据的存储方式，每一个类定义了一种存储方式，类名可以自定义，方法 `def process_item()`是固定的，方法名不能修改
`settings.py` 用来开启各个组件，例如可以通过取消注释开启pipeline、middleware等

## 杂项

setting.py中设置日志级别：`LOG_LEVEL = 'WARNING'` 表示只展示warning及以上的日志

items.py中定义好数据名后需要在<spider_name>.py中导入： `from myproject.items import <spider_name>Item`

在<spider_name>.py中使用items.py中定义好的数据名：
```python
data_name = <spider_name>Item()  # 将<spider_name>替换为你的爬虫名，即scrapy genspider spider_name domain.com 中的spider_name
data_name['name'] = name  
data_name['category'] = category
```

