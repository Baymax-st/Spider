## ����һ��������Ŀ

```bash
scrapy startproject <project_name>
# <project_name> ����Ŀ���ƣ����ܰ����ո�������ַ�
# ���磺����һ����Ϊ myproject ����Ŀ
scrapy startproject myproject
```
������������󣬻��ڵ�ǰĿ¼�´���һ����Ϊ myproject ���ļ��У���������� Scrapy ��Ŀ�Ļ����ṹ���ļ���

��Ŀ�ṹ���£�

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

## ����һ������

```bash
scrapy genspider <spider_name> <domain>
# <spider_name> ���������ƣ�<domain> ������Ҫץȡ����վ����
```
������������󣬻��� spiders Ŀ¼�´���һ����Ϊ <spider_name>.py ���ļ����������������Ļ�������ṹ��

��Ŀ�ļ��Ļ����ṹ���£�

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








