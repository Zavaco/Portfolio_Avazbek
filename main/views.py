from django.shortcuts import render, redirect
from .models import *
from .forms import ClientForm
# Create your views here.


def main_content(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    main_page = MainPage.objects.all()
    menu = Menu.objects.all()
    about_page = About.objects.all()
    service_page = Service.objects.all()
    resume_page = Resume.objects.all()
    work_page = Work.objects.all()
    contact_page = Contact.objects.all()
    context = {
        'main_page': main_page,
        'menu': menu,
        'about_page': about_page,
        'service_page': service_page,
        'resume_page': resume_page,
        'work_page': work_page,
        'contact_page': contact_page,
        'form': form,
    }
    return render(request, 'main/index.html', context)


