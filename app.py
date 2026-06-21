from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h1>Flask App v1.0</h1>
    <p>姓名：杨金鑫</p>
    <p>学号：2440664317</p>
    <p>CI/CD部署成功！服务运行正常</p>
    """

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)