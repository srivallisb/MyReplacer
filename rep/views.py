from django.shortcuts import render,redirect
from .models import Replacewords
from rep.rep_func import getnew


def replace(request):
	if request.method=="POST":
			title=request.POST["title"]
			paragraph=request.POST["paragraph"]
			substring_to_be_replaced=request.POST["substring_to_be_replaced"]
			replace_word=request.POST["replace_word"]
			new_para= getnew(paragraph,substring_to_be_replaced,replace_word)
			para= Replacewords.objects.create(
						new_para=new_para
				)
			
			return render(request,"replace_string.html",{"para":para})
	return render(request,"replace_string.html")

