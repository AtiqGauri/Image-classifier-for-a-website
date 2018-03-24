from django.shortcuts import render
import os
from django.conf import settings
#from settings import PROJECT_ROOT

#file_ = open(os.path.join(os.path.dirname(os.path.dirname(__file__)),'prediction.txt'))
p = os.path.join(os.path.dirname(os.path.dirname(__file__))) + "\\prediction.txt"
def post_list(request):
	file_= open(p, 'r+')
	c ={1:file_.readline(), 2: 'hello', 3: 4}
	d={}
	d = file_.readlines()
	#for line in file_.readlines():
	#	d = {l: line}
	#	l+=1
	return render(request, 'web/post_list.html', {'d': d})