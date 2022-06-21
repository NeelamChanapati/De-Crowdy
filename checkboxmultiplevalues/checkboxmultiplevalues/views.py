from django.shortcuts import render
from checkboxmultiplevalues.models import chkboxcourse

def savevalues(request):
	if request.method == 'POST':
		if request.POST.get('coursename'):
			savedata = chkboxcourse()
			savedata.coursename= request.POST.get('coursename')
			savedata.save()
			return render(request, 'index.html')

	else:
		return render(request, 'index.html')
