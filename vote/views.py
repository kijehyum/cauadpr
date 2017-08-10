from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Ad_video, Ad_outdoor, Ad_ent


# Create your views here.
def index(request):
	return render(request, 'vote/index.html')

def video(request):
	# vid_candidate = Ad_video.objects.get(id=1)
	vid_candidates = Ad_video.objects.all()
	out_candidates = Ad_outdoor.objects.all()
	ent_candidates = Ad_ent.objects.all()

	if request.POST:
		vid_id = request.POST.get('vid_id')
		# out_id = request.POST.get('out_id')
		# ent_id = request.POST.get('ent_id')

		vid = Ad_video.objects.get(id=vid_id)
		# out = Ad_outdoor.objects.get(id=out_id)
		# ent = Ad_ent.objects.get(id=ent_id)
		vid.result += 1
		vid.save()
		# out.result += 1
		# out.save()
		# ent.result += 1
		# ent.save()
		return HttpResponseRedirect('/outandent')

	context_dict = {
		'vid_candidates': vid_candidates,
		# 'out_candidates': out_candidates,
		# 'ent_candidates': ent_candidates,
	}
	return render(request, 'vote/video.html', context_dict)

# def detail(request, name):
# 	context_dict = {}
# 	return render(request, 'vote/detail.html', context_dict)

def outandent(request):
	return render(request, 'vote/outandent.html')