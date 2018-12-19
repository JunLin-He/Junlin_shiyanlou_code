#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

def hidden_email(email):
	parts = email.split('@')
	parts[0] = '*****'
	return '@'.join(parts)

app.add_template_filter(hidden_email)

@app.route('/')
def index():
	teacher = {
		'name': 'Alan',
		'email': 'GorgeousLin@outlook.com'
	}

	course = {
		'name': 'Golang Basic',
		'teacher': teacher,
		'user_count': 6666,
		'price': 998.0,
		'lab': None,
		'is_private': False,
		'is_member_course': True,
		'tags': ['Python', 'DataAnalysis', 'Linux']
	}
	return render_template('index.html', course=course)


'''
<p> name: {{ course.name }} </p>
<p> user count: {{ course.user_count }} </p>
<p> teacher: {{ course.teacher }} </p>
<p> is_private: {{ course.is_private }} </p>
<p> not exist: {{ course.not_exist }} </p>
{% set result = heavy_operation() %} 
<p> {{ result }} </p>
'''

'''
{% if course.is_private %}
	<p> course {{course.name}} is private </p>
{% elif course.is_member_course %}
	<p> course {{course.name}} is member course </p>
{% else %}
	<p> course {{course.name}} is normal course </p>
{% endif %}

{% for tag in course.tags %}
	<span> {{ tag + ',' }} </span>
{% endfor %}

{% set result = heavy_operation() %}
<p> {{result}} </p>
'''

'''
<div> {{ course_item(course) }} </div>
<p>{{ '=' * 20 }}</p>
<div> {{ course_item(course, type="louplus") }}</div>
'''