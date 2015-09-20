import requests
import json

'''
The function returns the corresponding code for the train station.

Since the function is auto-complete, only part of the city name is needed.
'''

def main():
	city = raw_input("city")
	codes(city)

def codes(city):
	url = "https://api.sandbox.amadeus.com/v1.2/rail-stations/autocomplete?apikey=mbZfPQ5trh2G97whOJeTxGwB5MiHkkoV&term=" + city
	response = requests.get(url)
	parsed = json.loads(response.text)	
	n = 0
	try:
		while parsed[n]:
			print parsed[n]["value"]
			n += 1
	except IndexError:
		pass

if __name__ == "__main__":
	main()
