from cgi import parse_qs
from template import html

def application(environ, start_response):
	c = parse_qs(environ['QUERY_STRING'])
	a = c.get('a', [''])[0]
	b = c.get('b', [''])[0]

	if '' in [a,b]:
		a, b = 0, 0
	else:
		a, b = int(a), int(b)
	add = a + b
	mul = a * b
	response_body = html % {
		'Add': add,
		'Mul': mul,
	}
	start_response('200 OK', [
		('Content-Type', 'text/html'),
		('Content-Length', str(len(response_body)))
	])
	return [response_body] 

