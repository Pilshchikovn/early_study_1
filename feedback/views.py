from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedBackForm
from .models import Feedback
from django.views import View


class FeedBackView(View):
    def get(self,request):
        form = FeedBackForm()
        return render(request, 'feedback/feedback.html', context={'form': form})

    def post(self,request):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/done')
        else:
            return render(request, 'feedback/feedback.html', context={'form': form})


def index(request):
    if request.method == "POST":
        form = FeedBackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect('/done')
    else:
        form = FeedBackForm()
    return render(request, 'feedback/feedback.html', context={'form': form})


def done(request):
    return render(request, 'feedback/done.html')


def update_feedback(request, id_feedback):
    feed = Feedback.objects.get(id=id_feedback)
    if request.method == "POST":
        form = FeedBackForm(request.POST, instance=feed)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect(f'/{id_feedback}')
    else:
        form = FeedBackForm(instance=feed)
    return render(request, 'feedback/feedback.html', context={'form': form})

# ______________________
# def index(request):
#     if request.method == "POST":
#         name = request.POST['name']
#         if len(name)==0:
#             return render(request, 'feedback/feedback.html', context={'got_error': True})
#         print(name)
#         return HttpResponseRedirect('/done')
#     return render(request, 'feedback/feedback.html', context={'got_error': False})
#
#
# def done(request):
#     return render(request, 'feedback/done.html')
# ________________________________________
# def index(request):
#     form = FeedBackForm()
#     if request.method == "POST":
#         name = request.POST['name']
#         if len(name)==0:
#             return render(request, 'feedback/feedback.html', context={'form': form})
#         print(name)
#         return HttpResponseRedirect('/done')
#     return render(request, 'feedback/feedback.html', context={'form': form})
#
#
# def done(request):
#     return render(request, 'feedback/done.html')

# _________________________________________________
# from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from .forms import FeedBackForm
# from .models import Feedback
#
#
# def index(request):
#     if request.method == "POST":
#         form = FeedBackForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             feed = Feedback(name=form.cleaned_data['name'],
#                             surname=form.cleaned_data['surname'],
#                             feedback=form.cleaned_data['feedback'],
#                             rating=form.cleaned_data['rating'])
#             feed.save()
#             return HttpResponseRedirect('/done')
#     else:
#         form = FeedBackForm()
#     return render(request, 'feedback/feedback.html', context={'form': form})
#
#
# def done(request):
#     return render(request, 'feedback/done.html')

#
# _____________________________________________________________
#
# def index(request):
#     if request.method == "POST":
#         form = FeedBackForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect('/done')
#     else:
#         form = FeedBackForm()
#     return render(request, 'feedback/feedback.html', context={'form': form})
#
#
# def done(request):
#     return render(request, 'feedback/done.html')
#
# def update_feedback(request, id_feedback):
#     feed = Feedback.objects.get(id=id_feedback)
#     if request.method == "POST":
#         form = FeedBackForm(request.POST,instance=feed)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect(f'/{id_feedback}')
#     else:
#         form = FeedBackForm(instance=feed)
#     return render(request, 'feedback/feedback.html', context={'form': form})
