# requests库学习

## 方法及简单框架

- Requests库有7个常用方法：request(),get(),head(),post(),put(),patch(),delete()

| 方法                 | 说明                              |
|--------------------|---------------------------------|
| requests.request() | 构造一个请求，支撑以下各方法的基础               |
| requests.get()     | 获取HTML网页的主要方法，对应HTTP的GET        |
| requests.head()    | 获取HTML网页头部信息的方法，对应HTTP的HEAD     |
| requests.post()    | 向HTML网页提交POST请求的方法，对应于HTTP的POST |
| requests.put()     | 向HTML网页提交PUT请求的方法，对应于HTTP的PUT   |
| requests.patch()   | 向HTML网页提交局部修改请求，对应于HTTP的PATCH   |
| requests.delete()  | 向HTML网页提交删除请求，对应于HTTP的DELETE    |

实际上，**后6个方法都是对requests.request()的封装**

### requests.request()方法详解

- requests.request(method, url, **kwargs)

method即为GET、HEAD等

kwargs为控制访问的参数，共有**13个**

1.`params`:参数类型为字典或字节序列，作为参数增加到url中

```python
import requests
kv = {'key1':'value1', 'key2':'value2'}
r = requests.request('GET', 'http://python123.io/ws', params=kv)
print(r.url)
# 输出为http://python123.io/ws?key1=value1&key2=value2
```
2.`data`:字典、字节序列或文件对象，作为Request的内容

```python
import requests
kv = {'key1':'value1', 'key2':'value2'}
r = requests.request('POST', 'http://python123.io/ws', data=kv)
body = '主体内容'
r1 = requests.request('POST', 'http://python123.io/ws', data=body)
# kv与body作为url数据存储到url对应位置
```

3.`json`:JSON格式的数据，作为Request的内容
```python
import requests
kv = {'key1':'value1'}
r = requests.request('POST', 'http://python123.io/ws', json=kv)
# 以上代码将数据提交到url的json域上
```

4.`headers`:字典，HTTP定制头

主要用于模拟request请求的浏览器代理(user-agent)

```python
import requests
hd = {'user-agent':'Chrome/10'}
r = requests.request('POST', 'http://python123.io/ws', headers=hd)
```

5.`cookies`:字典或CookieJar，Request中的cookie

6.`auth`:元组，支持HTTP认证功能

7.`files`:字典类型，是向服务器传输文件时使用的字段

```python
import requests
fs = {'file':open('data.xls', 'rb')}
r = requests.request('POST', 'http://python123.io/ws', files=fs)
```

8.`timeout`:float或tuple类型，是设定超时时间，以秒为单位

加快访问效率，如果超过设定时间没有请求成功，则抛出超时异常

9.`proxies`:字典类型，设定访问代理服务器，可以增加登录认证

```python
import requests
pxs = {'http':'http://user:pass@10.10.10.11:1234',
'https':'https://10.10.10.1:4321'}
r = requests.request('GET', 'http://www.baidu.com', proxies = pxs)
```

10.`allow_redirects`:True/False，默认为True，重定向开关

开启则允许对url重定向(当request请求3xx时会触发重定向),
- 当服务器返回 **3xx 状态码（如 301、302、304）** 时，requests 会自动向重定向的目标 URL 发送新请求。
- 若设为 `False`，则禁止自动跳转，直接返回原始响应对象（响应中包含重定向状态码和 `Location` 头）。
```python
import requests

# 示例1：禁止重定向，手动处理跳转
response = requests.get("http://short.url", allow_redirects=False)
if response.status_code == 302:
    target_url = response.headers["Location"]
    print(f"需跳转到：{target_url}")

# 示例2：默认允许重定向，跟踪完整跳转链
response = requests.get("https://httpbin.org/redirect/2")
print(f"最终状态码：{response.status_code}")  # 输出 200
print(f"重定向历史：{len(response.history)}次")  # 输出 2
```

11.`stream`:True/False，默认为True，获取内容立即下载开关

- `stream=True`：**延迟下载内容**，保持连接打开，需手动通过 `iter_content()` 或 `iter_lines()` 分块读取数据。
- `stream=False`：请求完成后立即完整加载响应内容到内存。
```python
import requests
# 分块下载大文件（避免内存满载）
response = requests.get("https://example.com/large_video.mp4", stream=True)
with open("video.mp4", "wb") as f:
    for chunk in response.iter_content(chunk_size=1024*1024):  # 每块 1MB
        if chunk:
            f.write(chunk)
response.close()

# 获取响应头而不下载内容体（如检查文件大小）
response = requests.head("https://example.com/file.zip")
file_size = response.headers.get("Content-Length")
print(f"文件大小：{file_size} Bytes")
```

12.`verify`:True/Fase，默认为True，认证SSL证书的开关

验证目标服务器的 SSL 证书有效性。

```python
import requests
# 绕过证书验证（危险！仅用于测试）
response = requests.get("https://self-signed.badssl.com", verify=False)

# 使用自定义 CA 证书（企业内网场景）
response1 = requests.get("https://internal-api.company.com", verify="/path/to/corporate_ca_bundle.pem")
```

13.`cert`:本地SSL证书路径

提供客户端 SSL 证书，用于服务器双向认证（mTLS）

cert: Union[str, Tuple[str, str]] = None

- `str`：包含客户端证书和密钥的 **单个文件路径**（需包含私钥，需为 PEM 格式）。
- `Tuple[str, str]`：证书文件路径和私钥文件路径组成的元组。

```python
import requests
# 使用客户端证书（如银行 API 认证）
client_cert = ("/path/client.crt", "/path/client.key")
response = requests.get("https://secure-bank-api.com", cert=client_cert)
```

```python
# 导入requests包
import requests
url = 'http://www.baidu.com'
# 调用requests中的get方法
r = requests.get(url)
```

**get()函数是一个Request对象，r是一个Response对象**

Response对象包含爬虫返回的内容

**Response对象的属性：**

| 属性                  | 说明                            |
|---------------------|-------------------------------|
| r.status_code       | HTTP请求的返回状态，200表示连接成功，404表示失败 |
| r.text              | HTTP响应内容的字符串形式，即url对应的页面内容    |
| r.encoding          | 从HTTPheader中猜测的响应内容编码方式       |
| r.apparent_encoding | 从内容中分析出的响应内容编码方式（备选编码方式）      |
| r.content           | HTTP响应内容的二进制形式,例如还原网页中的图片     |

**Response对象的属性：**

| 异常                        | 说明                               |
|:--------------------------|----------------------------------|
| requests.ConnectionError  | 网络连接错误异常，如DNS查询失败、拒接连接等（连接国外服务器） |
| requests.HTTPError        | HTTP错误异常                         |
| requests.URLRequired      | URL缺失异常                          |
| requests.TooManyRedirects | 超过最大重定向次数，产生重定向异常                |
| requests.ConnectTimeout   | 连接远程服务器超时异常                      |
| requests.Timeout          | 请求URL超时（全过程，包括返回内容）              |

**r.raise_for_status**判断Response返回值是否访问成功，否则抛出**HTTPError**异常

## HTTP（超文本协议）协议

- HTTP的6个方法，分别与requests的后6个方法对应

GET:获取网页内容，如果网页内容太庞大，可能无法返回
HEAD:用较少的流量获取网页的大致信息
POST:在网页后添加数据
PUT:添加数据，并覆盖原本数据
PATCH:局部修改数据
DELETE:删除数据

 