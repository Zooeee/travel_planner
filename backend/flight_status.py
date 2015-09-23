import json
import requests

def main():
	time = raw_input("What date is your flight")
	flight = raw_input("Your flight please")
	times = time.split("-")
	year = times[0]
	month = times[1]
	day = times[2]
	carrier = flight[:2]
	number = flight[2:]
	
	depart = flight_departure(carrier, number, year, month, day)
	arrive = flight_arrival(carrier, number, year, month, day)
	print(depart, arrive)

def flight_departure(carrier, flight, year, month, day):
	appID = "0526ef83"
	appKEY = "bc5bcb10062dc8fac64cb3705adc318d"
	URL = "https://api.flightstats.com/flex/flightstatus/rest/v2/json/flight/status/" + carrier + "/" + flight + "/dep/" + year + "/" + month + "/" + day +"?appId=0526ef83&appKey=bc5bcb10062dc8fac64cb3705adc318d&utc=false"
	response = requests.get(URL)
	page = json.loads(response.text)
	return page["flightStatuses"][0]["departureDate"]["dateLocal"]

def flight_arrival(carrier, flight, year, month, day):
	URL = "https://api.flightstats.com/flex/flightstatus/rest/v2/json/flight/status/" + carrier + "/" + flight + "/dep/" + year + "/" + month + "/" + day +"?appId=0526ef83&appKey=bc5bcb10062dc8fac64cb3705adc318d&utc=false"
	response = requests.get(URL)
	page = json.loads(response.text)
	print(page["flightStatuses"][0]["departureAirportFsCode"])
	print(page["flightStatuses"][0]["arrivalAirportFsCode"])
	return page["flightStatuses"][0]["arrivalDate"]["dateLocal"]

if __name__ == '__main__':
	main()