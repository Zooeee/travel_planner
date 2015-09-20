import json
import requests
import auto_complete_flight
import sys
import datetime

def main():
	origin = raw_input("Where are you travelling from?")
	dest = raw_input("Where are you heading to?")
	date = raw_input("Date?")
	now = datetime.datetime.now()
	o_code = convert_codes(origin)
	d_code = convert_codes(dest)
	if date <= str(now) :
		print("Please enter a valid date.")
		sys.exit(1)
	else:
		match(o_code, d_code, date)

def convert_codes(city):
	city_codes = auto_complete_flight.codes(city)
	code = city_codes[:3]
	return code

def match(origin, destination, date):
	url = "https://api.sandbox.amadeus.com/v1.2/flights/low-fare-search?apikey=mbZfPQ5trh2G97whOJeTxGwB5MiHkkoV&origin="
	search = url + origin + "&destination=" + destination +"&departure_date=" + date + "&travel_class=ECONOMY" + "&non-stop=true&max_price=10000"
	page = requests.get(search)
	parsed = json.loads(page.text)
	tol_counter = 0
	itin_counter = 0
	flig_counter = 0

	#there are still bugs in the function it does not return all of the flights
	#there are bugs in the API as it does not return non-stop
	#the script does not return all the desired flights
	#some iteration must be going wrong

	result = ""
	#print parsed["results"][0]["itineraries"][0]["outbound"]["flights"]
	if len(parsed["results"][0]["itineraries"][0]["outbound"]["flights"]) == 1:
		company = parsed["results"][0]["itineraries"][0]["outbound"]["flights"]["operating_airline"]
		number = parsed["results"][0]["itineraries"][0]["outbound"]["flights"]["flight_number"]
		print company + number

	else:	
		print("not direct flight")

if __name__ == '__main__':
	main()
