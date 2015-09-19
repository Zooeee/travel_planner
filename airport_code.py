from slimit.parser import Parser
import requests

key = "187a8a34dd67ebf522062085f5352c62"	
#city = raw_input("city")
#url = "https://airport.api.aero/airport/match/"
#search = url + city + "?/user_key=" + key
page = requests.get("https://airport.api.aero/airport/match/toronto?user_key=abd027dfd88e5799a6045760e9433a1d")
print page.text
		
