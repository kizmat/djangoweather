from django.shortcuts import render

# Create your views here.

def home(request):

	import json
	import requests

	if request.method == "POST":
		zipcode = request.POST['zipcode']
				# http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=735BE194-0A39-403A-9ADD-E6D5A5CC2CC0
		api_request = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode='+zipcode+'&distance=5&API_KEY=735BE194-0A39-403A-9ADD-E6D5A5CC2CC0')

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "API Error...."

		if api[0]['Category']['Name'] == "Good":
	  		category_description = "The AQI value for your community is between 0 and 50. Air quality is satisfactory and poses little or no health risk."
	  		category_color = "good"
		elif api[0]['Category']['Name'] == "Moderate":
			category_description = "The AQI is between 51 and 100. Air quality is acceptable; however, pollution in this range may pose a moderate health concern for a very small number of individuals. People who are unusually sensitive to ozone or particle pollution may experience respiratory symptoms."
			category_color = "moderate"
		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_description = " When AQI values are between 101 and 150, members of sensitive groups may experience health effects, but the general public is unlikely to be affected. •	Ozone: People with lung disease, children, older adults, and people who are active outdoors are considered sensitive and therefore at greater risk.•	Particle pollution: People with heart or lung disease, older adults,1 and children are considered sensitive and therefore at greater risk." 
			category_color = "usg"
		elif api[0]['Category']['Name'] == "Unhealthy":
			category_description = "Everyone may begin to experience health effects when AQI values are between 151 and 200. Members of sensitive groups may experience more serious health effects. " 
			category_color = "unhealthy"
		elif api[0]['Category']['Name'] == "Very Unhealthy":
			category_description = "AQI values between 201 and 300 trigger a health alert, meaning everyone may experience more serious health effects. "
			category_color = "veryunhealthy"
		elif api[0]['Category']['Name'] == "Hazardous":
			category_description = "AQI values over 300 trigger health warnings of emergency conditions. The entire population is even more likely to be affected by serious health effects. "
			category_color = "hazardous"
		
		return render(request, 'home.html', {'api': api, 'category_description': category_description, 'category_color': category_color})

	else:

		#zip code api
		#api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=735BE194-0A39-403A-9ADD-E6D5A5CC2CC0")
		#kuwait Latitude API
		api_request = requests.get("http://www.airnowapi.org/aq/observation/latLong/current/?format=application/json&latitude=29.3117&longitude=47.4818&distance=100&API_KEY=735BE194-0A39-403A-9ADD-E6D5A5CC2CC0")
		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "API Error...."

		if api[0]['Category']['Name'] == "Good":
	  		category_description = "The AQI value for your community is between 0 and 50. Air quality is satisfactory and poses little or no health risk."
	  		category_color = "good"
		elif api[0]['Category']['Name'] == "Moderate":
			category_description = "The AQI is between 51 and 100. Air quality is acceptable; however, pollution in this range may pose a moderate health concern for a very small number of individuals. People who are unusually sensitive to ozone or particle pollution may experience respiratory symptoms."
			category_color = "moderate"
		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_description = " When AQI values are between 101 and 150, members of sensitive groups may experience health effects, but the general public is unlikely to be affected. Ozone: People with lung disease, children, older adults, and people who are active outdoors are considered sensitive and therefore at greater risk. Particle pollution: People with heart or lung disease, older adults, and children are considered sensitive and therefore at greater risk." 
			category_color = "usg"
		elif api[0]['Category']['Name'] == "Unhealthy":
			category_description = "Everyone may begin to experience health effects when AQI values are between 151 and 200. Members of sensitive groups may experience more serious health effects. " 
			category_color = "unhealthy"
		elif api[0]['Category']['Name'] == "Very Unhealthy":
			category_description = "AQI values between 201 and 300 trigger a health alert, meaning everyone may experience more serious health effects. "
			category_color = "veryunhealthy"
		elif api[0]['Category']['Name'] == "Hazardous":
			category_description = "AQI values over 300 trigger health warnings of emergency conditions. The entire population is even more likely to be affected by serious health effects. "
			category_color = "hazardous"
		
		
		return render(request, 'home.html', {'api': api, 'category_description': category_description, 'category_color': category_color})

def about(request):
	return render(request, 'about.html', {})
