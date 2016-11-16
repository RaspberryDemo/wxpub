<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=0">
        <title>逍遥游论坛</title>
        <!-- 引入 WeUI -->
        <link rel="stylesheet" href="{{ url_for('static', filename='css/site.css') }}"/>
    </head>
    <body>

    最新文章列表       
    {% for f in findings %}
        <h3>{{ f.title }}</h3>
        <pre>{{ f.content }}</pre>
    {% endfor %}


    </body>
</html>
