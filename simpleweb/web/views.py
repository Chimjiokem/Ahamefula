from django.shortcuts import render

#Create your views here.
def base(request):
	return render(request,'base.html')
def middle(request):
	return render(request,'middle.html')

def again(request):
	return render(request, 'again.html')
