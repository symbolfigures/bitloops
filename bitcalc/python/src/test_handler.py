import json
from main import handler

def test_handler():

	event = {}
	context = {}

	response = handler(event, context)

	status_code = response['statusCode']
	headers = response['headers']
	body = response['body']

	print(f"status code: {status_code}")
	print(f"headers:")
	for key, value in headers.items():
		print(f"  {key}: {value}")
	print("body:")
	print(json.dumps(json.loads(body), indent=2))

if __name__ == '__main__':
	test_handler()






