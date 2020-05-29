from django.shortcuts import render

# Create your views here.

def home(request):

	import json
	import requests

	# http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=735BE194-0A39-403A-9ADD-E6D5A5CC2CC0
	api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=735BE194-0A39-403A-9ADD-E6D5A5CC2CC0")

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
		category_description = "The AQI is between 51 and 100. Air quality is acceptable; however, pollution in this range may pose a moderate health concern for a very small number of individuals. People who are unusually sensitive to ozone or particle pollution may experience respiratory symptoms." 
		category_color = "usg"
	elif api[0]['Category']['Name'] == "Unhealthy":
		category_description = "The AQI is between 51 and 100. Air quality is acceptable; however, pollution in this range may pose a moderate health concern for a very small number of individuals. People who are unusually sensitive to ozone or particle pollution may experience respiratory symptoms." 
		category_color = "unhealthy"
	elif api[0]['Category']['Name'] == "Very Unhealthy":
		category_description = "The AQI is between 51 and 100. Air quality is acceptable; however, pollution in this range may pose a moderate health concern for a very small number of individuals. People who are unusually sensitive to ozone or particle pollution may experience respiratory symptoms."
		category_color = "veryunhealthy"
	elif api[0]['Category']['Name'] == "Hazardous":
		category_description = "The AQI is between 51 and 100. Air quality is acceptable; however, pollution in this range may pose a moderate health concern for a very small number of individuals. People who are unusually sensitive to ozone or particle pollution may experience respiratory symptoms."
		category_color = "hazardous"
	
	return render(request, 'home.html', {'api': api, 'category_description': category_description, 'category_color': category_color})

def about(request):
	return render(request, 'about.html', {})
