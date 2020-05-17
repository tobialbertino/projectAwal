from django.shortcuts import render


def index(request):
	context = {
		'title':'Home Page',
		'content':'ini adalah home page dari website ini'
	}

	return render(request,'index.html',context)