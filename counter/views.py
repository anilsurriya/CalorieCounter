from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return redirect('auth_cal:login')
    import json
    import requests
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': 'h60Q+bRzlrLtWo/Mjy02IA==8wSTzD9TztVMwyxu'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        if api == b"":
            return render(request, home.html)
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})