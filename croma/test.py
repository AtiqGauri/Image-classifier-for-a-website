f= open("prediction.txt","r")
d={}
line_num = 1
for line in f:
	d[line_num] = line
	line_num += 1
print(d)



{% for key, value in c.items %}
                <tr>
                    <td> {{ key }} </td> 
                    <td> {{ value }} </td><br />
                </tr>
            {% endfor %}


{% load staticfiles %}
<html>
    <head>
        <title>Predictions</title>
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
        <link rel="stylesheet" href="{% static 'css/blog.css' %}">
    </head>
    <body>
        <div>
            <h1><p style="color:#5c7ad6"><b>{{ let }}</b></p></h1>
        </div>
    </body>
</html>


{% load staticfiles %}
<html>
    <head>
        <title>the XYZ</title>
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
        <link rel="stylesheet" href="{% static 'css/blog.css' %}">
    </head>
    <body>
        <div>
            <h1><a href="/">Django Girls Blog</a></h1>
        </div>

        {% for post in posts %}
            <div>
                <p>published: {{ post.published_date }}</p>
                <h1><a href="">{{ post.title }}</a></h1>
                <p>{{ post.text|linebreaksbr }}</p>
            </div>
        {% endfor %}
    </body>
</html>