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
	flight_status(carrier, number, year, month, day)

def flight_status(carrier, flight, year, month, day):
	appID = "0526ef83"
	appKEY = "bc5bcb10062dc8fac64cb3705adc318d"
	URL = "https://api.flightstats.com/flex/flightstatus/rest/v2/json/flight/status/" + carrier + "/" + flight + "/dep/" + year + "/" + month + "/" + day +"?appId=0526ef83&appKey=bc5bcb10062dc8fac64cb3705adc318d&utc=false"
	response = requests.get("https://api.flightstats.com/flex/flightstatus/rest/v2/json/flight/status/AA/100/dep/2015/09/22?appId=0526ef83&appKey=bc5bcb10062dc8fac64cb3705adc318d&utc=false")
	page = json.loads(response.text)
	print page["flightStatuses"][0]["departureDate"]["dateLocal"]

if __name__ == '__main__':
	main()