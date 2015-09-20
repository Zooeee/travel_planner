import json
import requests

'''
The function returns the IATA codes for the corresponding 
'''
def main():
	city = raw_input("city")
	codes(city)

def codes(city):
	url = "https://api.sandbox.amadeus.com/v1.2/airports/autocomplete?apikey=mbZfPQ5trh2G97whOJeTxGwB5MiHkkoV&term=" + city
	response = requests.get(url)
	parsed = json.loads(response.text)	
	n = 0
	result = ""
	try:
		while parsed[n]:
			result += parsed[n]["value"] + parsed[n]["label"]
			n += 1
	except IndexError:
		pass
	return result
	
if __name__ == "__main__":
	main()