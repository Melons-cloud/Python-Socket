#导入模块
import socket

#创建实例
sk =socket.socket();
#定义绑定ip和port
ip_port=("127.0.0.1",8888)
#绑定监听
sk.bind(ip_port)
#最大连接数
sk.listen(5)
#提示信息
print("")
#接收数据
conn,address=sk.accept()