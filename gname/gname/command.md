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
        items.py
        middlewares.py
        pipelines.py
        settings.py
        spiders/
            __init__.py
            <spider_name>.py
```








