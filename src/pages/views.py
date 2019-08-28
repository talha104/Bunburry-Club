from django.shortcuts import render


def home(request):
	return render(request, 'pages/home.html', {})

def menu(request):
	return render(request, 'pages/menu.html', {})

def story(request):
	return render(request, 'pages/story.html', {})

def order(request):
	return render(request, 'pages/order.html', {})

def celebrity(request):
	return render(request, 'pages/celebrity.html', {})

def about(request):
	return render(request, 'pages/about.html', {})
