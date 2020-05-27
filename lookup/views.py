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

	
	
	return render(request, 'home.html', {'api': api})

def about(request):
	return render(request, 'about.html', {})