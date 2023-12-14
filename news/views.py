from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from django.contrib.auth import login, logout

from .models import News, Categories
from .forms import NewsForm, UserRegisterForm, UserLoginForm




def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегестрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')


class HomeNews(ListView):
    model = News
    paginate_by = 20

    def get_queryset(self):
         return News.objects.filter(is_published=False).select_related('category')



class NewsByCategories(ListView):
    model = News
    paginate_by = 20

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=False).select_related('category')

    def get_context_data(self):
        context = super().get_context_data()
        context['active_category'] = Categories.objects.get(pk=self.kwargs['category_id'])
        return context


class NewDetail(DetailView):
    model = News
    context_object_name = 'new'


class CreateNew(CreateView):
    form_class = NewsForm
    template_name = 'news/create_new.html'


