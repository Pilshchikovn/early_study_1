from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedBackForm
from .models import Feedback
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView,UpdateView


# Тоже самое только через FormView. ПЕРЕМЕННАЯ ДЛЯ HTML ДОЛЖНА НАЗЫВАТЬСЯ ТОЛЬКО form
# _____________________________________________________________
#
#
# class FeedBackView(FormView):
#     form_class = FeedBackForm
#     template_name ='feedback/feedback.html'
#     success_url = '/done'
#     #написать метод чтобы дать указание куда эти данные дальше отправить и что с ними делать
#     def form_valid(self, form):
#         form.save()
#         return super(FeedBackView, self).form_valid(form)

# с помощью CreateViev мы можем избавться от метода formvalid
class FeedBackView(CreateView):
    model = Feedback
    # fields = ['name', 'surname']
    form_class = FeedBackForm
    template_name = 'feedback/feedback.html'
    success_url = '/done'

class FeedBackViewUpdate(UpdateView):
    model = Feedback
    form_class = FeedBackForm
    template_name = 'feedback/feedback.html'
    success_url = '/done'

# class FeedBackView(View):
#     def get(self, request):
#         form = FeedBackForm()
#         return render(request, 'feedback/feedback.html', context={'form': form})
#
#     def post(self, request):
#         form = FeedBackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/done')
#         else:
#             return render(request, 'feedback/feedback.html', context={'form': form})


# Основные только эти 2 строчки Это Template view. Это значит просмотреть шаблон
# ________________________________________________________________________________
class DoneView(TemplateView):
    template_name = 'feedback/done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Ivanov I.I.'
        context['date'] = '23.08.20202'
        return context


# class ListFeedbackView(TemplateView):
#     template_name = 'feedback/list_feedback.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         feedbacks = Feedback.objects.all()
#         context['all'] = feedbacks
#         return context

# Основные только эти 2 строчки Это ListView view. Это значит просмотреть шаблон. В HTML обязательно object_list
# если не меняем
# ________________________________________________________________________________
class ListFeedbackView(ListView):
    template_name = 'feedback/list_feedback.html'
    model = Feedback
    # context_object_name = 'feedback'

    # def get_queryset(self):
    # фильтрует данные
    #     queryset=super().get_queryset()
    #     filter_qs = queryset.filter(rating__gt=4)
    #     return filter_qs


# Это Template view. Это значит просмотреть шаблон
# ________________________________________________________________________________
# class DetailFeedBack(TemplateView):
#     template_name = 'feedback/detail_feedback.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         id_feedback = kwargs['id_feedback']
#         feedback = Feedback.objects.get(id=id_feedback)
#         context['current'] = feedback
#         return context

# Это DetailView. Посмотреть детальную информацию. То же самое, только по-другому
# <!--ИМЯ ДОЛЖНО БЫТЬ ТОЛЬКО feedback в HTML
# ОНА БЕРЕТСЯ ИЗ НАЗВАНИЯ ВАШЕЙ МОЖЕЛИ В НИЖНЕМ РЕГИСТЕ
# ИЛИ object
# ________________________________________________________________________________
class DetailFeedBack(DetailView):
    template_name = 'feedback/detail_feedback.html'
    model = Feedback
    # или можно задать свое имя
    # context_object_name = 'feed'


# class DoneView(View):
#     def get(self,request):
#         return render(request, 'feedback/done.html')


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


# def update_feedback(request, id_feedback):
#     feed = Feedback.objects.get(id=id_feedback)
#     if request.method == "POST":
#         form = FeedBackForm(request.POST, instance=feed)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect(f'/{id_feedback}')
#     else:
#         form = FeedBackForm(instance=feed)
#     return render(request, 'feedback/feedback.html', context={'form': form})

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
