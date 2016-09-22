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

创建微信公众号菜单
----------------------------
使用以下内容创建菜单
```bash
{
    "button": [
        {
            "type": "click", 
            "name": "内涵段子", 
            "key": "MY_JOKE", 
            "sub_button": [ ]
        }, 
        {
            "name": "精品服务", 
            "sub_button": [
                {
                    "type": "click", 
                    "name": "美剧资讯", 
                    "key": "MY_MEIJU", 
                    "sub_button": [ ]
                }, 
                {
                    "type": "click", 
                    "name": "随便听听", 
                    "key": "MY_MUSIC", 
                    "sub_button": [ ]
                }, 
                {
                    "type": "view", 
                    "name": "服务检测", 
                    "url": "http://loveme.tpddns.cn/status", 
                    "sub_button": [ ]
                }, 
                {
                    "type": "click", 
                    "name": "历史趣闻", 
                    "key": "MY_HISTORY", 
                    "sub_button": [ ]
                }
            ]
        }
    ]
}
```
