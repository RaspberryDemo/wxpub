<xml>
<ToUserName><![CDATA[{{ toUser }}]]></ToUserName>
<FromUserName><![CDATA[{{ fromUser }}]]></FromUserName>
<CreateTime>{{ createtime }}</CreateTime>
<MsgType><![CDATA[news]]></MsgType>
<ArticleCount>{{ count }}</ArticleCount>
<Articles>
{% for it in items %}
<item>
<Title><![CDATA[{{ it.title }}]]></Title> 
<Description><![CDATA[{{ it.description }}]]></Description>
<PicUrl><![CDATA[{{ it.picurl }}]]></PicUrl>
<Url><![CDATA[{{ it.url }}]]></Url>
</item>
{% endfor %}
</Articles>
</xml>