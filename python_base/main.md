# python 基礎
## python 環境安裝
- linux系統安裝前，先執行
    - `sudo apt-get update`
    - `sudo apt-get upgrade`
    - `sudo apt-get dist-upgrade`
- 安裝python3
    - `sudo apt-get install python3`
- 檢查python version
    - `python -VV`
- 安裝pip
    - `sudo apt-get install python-pip`
- 升級pip version
    - `sudo pip install --upgrade pip`
- 安裝python module
    - `pip install [module name]`
## python module 導入與使用
- (1)import [module name]
    - 在object前加上模塊名稱作為前綴
    ```python=
    import requests
    r = requests.get('https://google.com')
    ```
- (2)from [module name] import [object name]
    - 導入明確指定的object，可只輸入少量code，不需要在object前加上模塊名稱作為前綴
    ```python=
    from math import sin
    sin(2.5)
    ```
## python list 列表
- 最基本的數據結構，包括**表**、**元組**、**字典**等
- (1)創建列表
    - `student = ['num', 'name', 'age']`
    - 也可通過list()將元組、字串、字典等類型轉為列表
    - `num = list((1,2,3,4,5,6,7,8,9))`
- (2)刪除列表
    - 單一元素
        - `del list[position]`
    - 整個列表
        - `del list`
- (3)在列表尾部添加元素
    - 單一元素
        - `list.append('element name')`
    - 結合列表
        - `list.extend([list name])`
- (4)在列表指定位置添加
    - `list.insert(4, 'a')`
- (5)刪除列表中首次出現元素
    - `list.remove([element name])`
- (6)刪除並返回列表中
    - `list.pop()`
    - `list.pop([position])`
- (7)返回指定元素在列表中出現次數
    - `list.count([element name])`
- (8)將列表中所有元素逆序
    - `list.reverse()`
- (9)對列表中元素進行排序
    - `list.sort(key=str, reverse=False)`
    - key:排序依據，reverser:False(升序)、True(降序)

## python tuple 元組
- 屬於不可變序列，創建後無法對其元素進行增刪改查，但對元素的速度要比列表快得多，且期待代碼更安全(不可更改)
- `tuple = ('a','b','c',1,2,3)`

## python dictory 字典
- 包含{key, value}的可變序列，其key不能重複
- (1)創建字典
    - `dic = dict('lab':'nslab','url':'https://google0com')
- (2)修改字典中元素
    - `dic['lab'] = 'tcgs'`
- (3)添加新元素
    - `dic['number'] = '99'`
- (4)返回字典所有元素
    - `dic.items()`
- (5)刪除字典中元素
    - `del dic['url']`

## python 控制結構
- if
```python=
std_Score = int(input('Scores of stds: '))
if(std_Score < 60):
    print('failed')
elif(60 < std_Score < 80):
    print('okay')
else:
    print('nice')
```
- for、while循環
```python=
x = int(input('x = '))
y = int(input('y = '))
sum1 = 0
sum2 = 0

for i in range(1,x+1):
    sum1 += i
print('sum1 = ', sum1)

while y!=0:
    sum2 += y
    y -= 1
print('sum2 = ', sum2)
```
- try...except...else[finally]
    - try 引發異常語句
    - except 捕捉其異常
    - else 沒有異常即執行
    - finally 無論try是否正常執行，總會獲得執行


## python 檔案處理
- `open(file[, mode='r'[, buffering=-1]])`
    - file:檔案名稱，若該檔案不在當前目錄，則需找其相對路徑or絕對路徑
    - mode:開檔後的處理方式，包含w、a、r、+、b
		- r:讀取(檔案需存在)
		- w:新建檔案寫入(檔案可不存在，若存在則清空)
		- a:資料附加到舊檔案後面(游標指在EOF)
		- r+: 讀取舊資料並寫入(檔案需存在且游標指在開頭)
		- w+: 清空檔案內容，新寫入的東西可在讀出(檔案可不存在，會自行新增)
		- a+: 資料附加到舊檔案後面(游標指在EOF)，可讀取資料
		- b :二進位模式
    - buffering:讀寫文件的緩衝模式。
        - 0:不緩衝
        - 1:使用型緩衝
        - >1:緩衝區大小
        - -1(預設)
```python=
f = open('demo.txt','r')
print(f.readline())       # 讀取第一行內容
print(f.read())           # 讀取所有內容
f.close()
```

## socket 網路編程
- socket式計算機之間進行網路通信的一套程序接口，相當於sender & recivier間建立的通訊管道
- TCP(transmission control protol)
    - `conncet(address)` 連接遠程計算機
    - `send(byte[,flags])` 發送訊息
    - `recv(bufsize[,flags])` 接收訊息
    - `bind(address)` 綁定位址
    - `listening(backlog)`開始監聽，等待客戶端連接
    - `accept()` 響應客戶端請求
- server.py
    ```python=
    import socket
    language = {'what is your name':'i am shizu', 'how old are you':'18', 'bye':'88'}
    HOST = "127.0.0.1"
    PORT = 6666
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    print("listening at port 6666")
    conn, addr = s.accept()
    print('connect by: ',addr)
    while True:
        data = conn.recv(1024)
        data = data.decode()
        if not data:
            break
        print('received message:' + data)
        conn.sendall(language.get(data, 'Nothing').encode())
    conn.close()
    s.close
    ```
- client.py
```python=
import socket,sys
HOST = "127.0.0.1"
PORT = 6666
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((HOST, PORT))
except Exception as e:
    print("server not found")
    sys.exit()
while True:
    c = input("you say:")
    s.sendall(c.encode())
    data = s.recv(1024)
    data = data.decode()
    print("received:" + data)
    if(c.lower())=='bye':
        break
s.close()

```

## 可執行文件轉換
- 開發者分享程序時，為方便用戶在未安裝環境下可執行，須將開發好之程式進行打包
- **PyInstaller** 是常見的執行文件打包工具，但只能在與執行的系統類型相同的環境下可運行。
- windows
    - 安裝~~`python setup.py install`~~`pip install pyinstaller`
    - 打包`pyinstaller -F -i [.ico] [.py]`
        - 將python檔與需要綁定的icon放置通一個資料夾，生成exe在dist
- linux
    - 安裝`python setup.py install`
    - 打包`pyinstaller -F [.py]`
