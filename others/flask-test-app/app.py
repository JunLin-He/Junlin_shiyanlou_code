from flask import Flask, render_template, make_response, request

app = Flask(__name__)

'''
app.config.update({
	'SECRET_KEY': 'a random string'
})
'''

@app.route('/user/<username>')
def user_index(username):
	resp = make_response(render_template('user_index.html', username=username))
	resp.set_cookie('username', username)
	return resp
	#return render_template('user_index.html', username=username)

@app.route('/')
def index():
	username = request.cookies.get('username')
	return 'Hello {}'.format(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return 'Post {}'.format(post_id)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

if __name__ == '__main__':
	app.run()
