---
title: python之socket实现
date: 2019-06-05 19:33:00
tags: python,socket
categories: python
---
# 题外话
## python的函数反射
**问题**:如果不知道一个对象的方法，参数等等，如何调用对象里的方法呢？

**解决方法**:
1. 通过hasattr()来判断对象d中是否有对应字符串的方法c,其中hasattr(d,c)，d为对象obj，c为输入字符串
2. 通过getattr(d,c)获取d对象里的对应的方法映射的内存地址
3. 通过setattr(d,c,z)相当于'd.c = z'
4. 通过delattr(d,c)顾名思义,删除

代码:
```python
def bulk(self):#想要嵌入或修改的方法
    print("%s is yelling..." % self.name)

class Dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating %s" % (self.name,food))

d = Dog("liu")#定义对象
choice = input(">>:").strip()#输入方法名
if hasattr(d,choice):#看是否d中有该方法
    # delattr(d,choice)
    func = getattr(d,choice)#有则获取
    func("shit")#带参执行
else:
    # setattr(d,choice,bulk)
    # d.talk(d)
    setattr(d,choice,'miss')
    print( getattr(d,choice) )

print(d.name)

```
---
# 正篇
socket的流程:***三次握手，四次断开***
## python中的socket
**前置**:需要socket包(import socket)

**socket中的参数**：
- Socket families(地址簇)
    - socket.AF_UNIX #unix本机进程间通信
    - socket.AF_INET #IPV4，默认
    - socket.AF_INET6 #IPV6
- Socket Types
    - socket.SOCK_STREAM # for tcp，默认
    - socket.SOCK_DGRAM # for udp
    - socket.SOCK_RAW #for 原始套接字,可修改IP地址头（可伪造IP地址实现洪水攻击）
    - socket.SOCK_RDM #安全可靠的UDP形式，保证传到不保证顺序

**写一个简单的socket程序**：

服务器端:
```python
import socket

server = socket.socket()
server.bind(('localhost',6969))#绑定要监听的端口
server.listen()#监听,参数为最大挂起连接,一般5到10个

print('开始等待请求')
while True:
    conn,addr = server.accept()#等待客户端发送请求
    print('已接受到请求')#连接后服务器端会被占线，这种方法只能同时跟一个人对话
    while True:

        print(conn,addr)
        #conn就是客户端连过来而在服务器端为其生成的一个连接实例
        #实例conn:<socket.socket fd=712, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 6969), raddr=('127.0.0.1', 51280)>
        #地址addr:('127.0.0.1', 51280),51280为随机端口


        data = conn.recv(1024)
        print('recv:',data.decode())
        if not data:
            print('client has lost...')
            break
        conn.send(data.upper())#返回data的大写字母形式

server.close()
```
客户端:
```python
import socket

client = socket.socket()#声明socket类型，同时生成socket连接对象
client.connect(('localhost',6969))#连接本机ip的6969端口

while True:
    msg = input('>>:').strip()
    if len(msg) == 0:continue
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)#接收1024字节的数据,如果数据超过该值，剩下的将存储在缓冲区(32K)等待下次接受
    print('recv:',data.decode())

client.close()
```
**注意问题**:
1. 在python2里可以发str，byte等，python3只能发byte类型,所以要注意转换类型。可以用```b'字符串'```，但是这种方法只能转换在ASCII码里存在的字符，即大小写字母，数字和符号，中文是不行的。这时候要用```.encode('utf-8')```,相当于相当于先转成能接受的ASCII码数据再操作。
2. recv()有限制，不仅自身参数的限制还有缓冲区大小的限制，所以传输数据前最好给客户端发送数据大小，依据大小循环接收。
3. 如果想发送命令要求返回服务器端命令执行结果可以用```os.popen(data).read()```\[import os\],**popen这个方法会打开一个管道，返回结果是一个连接管道的文件对象，该文件对象的操作方法同open()，可以从该文件对象中读取返回结果。**。ps：会刷新的命令结果(如：top)要指定范围(如：top -bn 1(因为top会刷新，所以选择1秒内的数据))。
---
## 运用socket写一个FTP服务器
FTP Server流程:
1. 读取文件名
2. 检测文件是否存在
3. 打开文件
4. 检测文件大小  发送文件大小和md5给客户端
5. 等客户端确认  防止粘包
6. 开始边读边发数据

**粘包**:两个send()语句紧挨着可能会使发送的数据同时进入缓冲区合并成一次发送给客户端，造成socket粘包(linux和windows都会出现)。

**md5使用**:
```python
import hashlib # md5

m = hashlib.md5()
m.update(b'test')#必须为byte
m.update(b'abc')
print(m.hexdigest())

m2 = hashlib.md5()
m2.update(n'testabc')
print(m2.hexdigest())
# m 和 m2输出相同
```

