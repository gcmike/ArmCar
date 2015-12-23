import web

urls = (
	'/hello', 'hello'
)

class hello:
	def GET(self):
		data = web.input(name="tmp",id='10')
		data.id = str(2*int(data.id))
		return 'Hello, ' + data.name + ' and id is ' + data.id + '!'

if __name__ == "__main__":
	app = web.application(urls,globals())
	app.run()
