from urllib.parse import parse_qs
from urllib.parse import urlparse

templates = {
	'main_page': b'This is main page!',
	'hello': b'Hello,',
	b'404': b'No such page, buddy!'
}


routes = {
	b'/': templates['main_page'],
	b'/hello': templates['hello']
}


def render(route, param=b''):
	if route in routes.keys():
		if param.encode('utf-8') != '':
			return (routes[route] + b' ' + param, '200 OK')
		else:
			return (routes[route], '200 OK')
	else:
		return (templates[b'404'], '404 PAGE_NOT_FOUND')


def application(environ, start_response):
	name = parse_qs(urlparse(environ['REQUEST_URI']).query).get('name', [''])
	if name:
		name = name[0]

	route = environ['REQUEST_URI'].split('?')[0].encode('utf-8')

	resp = render(route, param=name.encode('utf-8'))
	start_response(resp[1], [('Content-Type', 'text/plain')])
	return [resp[0]]