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
        spiders/
            __init__.py
            <spider_name>.py
        items.py
        middlewares.py
        pipelines.py
        settings.py
```

## ����������Ŀ�ļ�������

`scrapy.cfg` �������ļ�������Ҫ�Ķ�������ɾ��
`items.py` ����������ȡ�������������ͣ������﷨�� `name= scrapy.Field()`, ����name�Ƕ��������Ĺ淶
`spider_name.py` �����������ʼ��ҳ�ͽ���Response���󣬻�ȡ���ݵ�,������ʽ��`xpath() css() json()`����item�ķ�ʽ�������ݸ�pipeline(��������)
`pipilines.py` ��������ܵ���������������ݵĴ洢��ʽ��ÿһ���ඨ����һ�ִ洢��ʽ�����������Զ��壬���� `def process_item()`�ǹ̶��ģ������������޸�
`settings.py` ������������������������ͨ��ȡ��ע�Ϳ���pipeline��middleware��

## ����

setting.py��������־����`LOG_LEVEL = 'WARNING'` ��ʾֻչʾwarning�����ϵ���־

items.py�ж��������������Ҫ��<spider_name>.py�е��룺 `from myproject.items import <spider_name>Item`

��<spider_name>.py��ʹ��items.py�ж���õ���������
```python
data_name = <spider_name>Item()  # ��<spider_name>�滻Ϊ�������������scrapy genspider spider_name domain.com �е�spider_name
data_name['name'] = name  
data_name['category'] = category
```

