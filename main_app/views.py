from django.shortcuts import render, render_to_response, get_object_or_404
import datetime
from main_app.models import Person, Works, Studies, Certificate
# Create your views here.


def main(request):
    my_data = Person.objects.all()[0]
    return render_to_response('index.html', {'my_email': my_email,'my_data': my_data})


def my_work(request):
    works = Works.objects.all()
    return render_to_response('my_work.html', {'my_email': my_email, 'works': works})


def my_studies(request):
    place_of_study = Studies.objects.all()
    certificate = Certificate.objects.all()
    #check = request.POST.get('twostud')
    #if not check:
    #    return render_to_response('my_studies.html', {'my_email': my_email,
    #                                                  'place_of_study': place_of_study,
    #                                                  'certificate': certificate,
    #                                                  'two': False})
    #else:
    return render_to_response('my_studies.html', {'my_email': my_email,
                                                  'place_of_study': place_of_study,
                                                  'certificate': certificate})


def get_work(request, id):
    work = get_object_or_404(Works, id=id)
    return render_to_response('About_work.html', {'my_email': my_email,
                                                  'work': work})


my_email = 'vasiliy.moscvin@yandex.ru'