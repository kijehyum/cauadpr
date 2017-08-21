from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Ad_video, Ad_outdoor, Ad_ent


def index(request):
	return render(request, 'vote/index.html')

def video(request):
	vid_candidates = Ad_video.objects.all()

	if request.POST:
		vid_id = request.POST.get('vid_id')

		vid = Ad_video.objects.get(id=vid_id)

		vid.result += 1
		vid.save()
		
		return HttpResponseRedirect('/outdoor')

	context_dict = {
		'vid_candidates': vid_candidates,
	}
	
	return render(request, 'vote/video.html', context_dict)

def outdoor(request):
	out_candidates = Ad_outdoor.objects.all()

	if request.POST:
		out_id = request.POST.get('out_id')

		out = Ad_outdoor.objects.get(id=out_id)
		
		out.result += 1
		out.save()

		return HttpResponseRedirect('/entertainment')

	context_dict = {
		'out_candidates': out_candidates,
	}

	return render(request, 'vote/outdoor.html', context_dict)

def entertainment(request):
	ent_candidates = Ad_ent.objects.all()

	if request.POST:
		ent_id = request.POST.get('ent_id')

		ent = Ad_ent.objects.get(id=ent_id)

		ent.result += 1
		ent.save()
		
		return HttpResponseRedirect('/exit')

	context_dict = {
		'ent_candidates': ent_candidates,
	}

	return render(request, 'vote/entertainment.html', context_dict)

def exit(request):
	return render(request, 'vote/exit.html')
