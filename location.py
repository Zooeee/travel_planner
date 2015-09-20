import json
import requests
import sys

'''
The function determines your location by the IATA code.
'''
def main():
	code = raw_input("code")
	location(code)

def location(code):
	url = "https://api.sandbox.amadeus.com/v1.2/location/" + code + "?apikey=mbZfPQ5trh2G97whOJeTxGwB5MiHkkoV"
	page = requests.get(url)
	if page.status_code == 400:
		sys.stderr.write("Please provide a valid city code.")
		sys.exit(1)
	parsed = json.loads(page.text)
	n = 0
	try:
		while parsed["airports"][n]:
			print parsed["airports"][n]["name"]
			n += 1
	except IndexError:
		pass

if __name__ == '__main__':
	main()