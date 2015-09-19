import json
import requests

origin = raw_input("Where are you travelling from?")
dest = raw_input("Where are you heading to?")
date = raw_input("Date?")
url = "https://api.sandbox.amadeus.com/v1.2/flights/low-fare-search?apikey=mbZfPQ5trh2G97whOJeTxGwB5MiHkkoV&origin="
search = url + origin + "&destination=" + dest +"&departure_date=" + date + "&travel_class=ECONOMY"
page = requests.get(search)
parsed = json.loads(page.text)
total = parsed["results"]
tol_counter = 0
itin_counter = 0
flig_counter = 0
while total[tol_counter]:
	try:
		total[tol_counter]["itineraries"][itin_counter]
		
		if total[tol_counter]["itineraries"][itin_counter]["outbound"]["flights"][flig_counter]:
			company = total[tol_counter]["itineraries"][itin_counter]["outbound"]["flights"][flig_counter]["operating_airline"]
			number = total[tol_counter]["itineraries"][itin_counter]["outbound"]["flights"][flig_counter]["flight_number"]
			itin_counter += 1
			print company + number
		else:
			break
		flig_counter += 1
	except IndexError:
		break
	tol_counter += 1
