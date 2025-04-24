from flask import Flask
app = Flask(__name__)     #创建一个名叫 app 的 Flask 应用，它的资源路径是以当前这个 Python 文件为基础。之后写的所有 Flask 路由和功能都要挂在这个 app 对象上

@app.route('/api/hello')    #app.route(...) 是 Flask 提供的函数，用于把 URL 和 Python 函数关联起来。
def hello():
    return {"message": "Hello world from Flask backend!"}

'''
@app.route('/api/goodbye')  # 新增的 URL 路由
def goodbye():
    return {"message": "Goodbye from Flask backend!"}
'''
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)    #启动一个 Flask 服务器，监听 3000 端口，等待接收请求。