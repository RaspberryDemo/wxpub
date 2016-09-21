<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=0">
        <title>在线监测</title>
        <!-- 引入 WeUI -->
        <link rel="stylesheet" href="https://res.wx.qq.com/open/libs/weui/0.4.2/weui.css"/>
    </head>
    <body>
        <!-- 使用 -->
        
        <div class="weui_cells_title">当前服务状态检测</div>
    <div class="weui_cells">
        {% for it in items %}
        <div class="weui_cell">
            <div class="weui_cell_hd">
              {% if it.up %}
                <i class="weui_icon_success"></i>
              {% else %}
                <i class="weui_icon_warn"></i>
              {% endif %}
            </div>
            <div class="weui_cell_bd weui_cell_primary">
                <p>&nbsp;&nbsp;{{ it.service }}</p>
            </div>
            <div class="weui_cell_ft">
                    {% if it.up %}
                        服务在线
                    {% else %}
                        服务离线
                    {% endif %}
            </div>
        </div>
        {% endfor %}
    </div>
    </body>
</html>
