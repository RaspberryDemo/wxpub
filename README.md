微信公众平台Python实现示例
============================

安装依赖环境
----------------------------
```bash
sudo pip install -r requirements.txt
sudo apt-get install nginx -y

```

使用gunicorn部署
----------------------------
```bash
gunicorn -w 4 -D --reload main:app

```

修改nginx配置
----------------------------
```bash
server {
    listen  8080;

    location / {
        proxy_pass http://127.0.0.1:8000;
    }

  }

```

重启nginx服务
----------------------------
```bash
sudo service nginx restart

```
