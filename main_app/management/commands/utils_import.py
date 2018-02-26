from django.core.management.base import BaseCommand

from main_app.models import Person, Works, Studies, Certificate
from datetime import date


def add_person():
    listperson = [
        {
            "name": "\u0412\u0430\u0441\u0438\u043b\u0438\u0439",
            "surname": "\u041c\u043e\u0441\u043a\u0432\u0438\u043d",
            "logo": "/static/img/my_photo.jpg",
            "logo_alt": "My photo",
            "birth_day": "1990/11/12",
            "age": 26,
            "city": "\u041a\u0430\u043b\u0443\u0433\u0430",
            "phone": "+7 910 511 07 85",
            "my_email": "vasiliy.moscvin@yandex.ru"
        }
    ]

    for i in listperson:
        Person.objects.create(**i)


def add_work():
    listwork=[
        {
            "name": "\u041a\u0443\u0440\u0447\u0430\u0442\u043e\u0432\u0441\u043a\u0438\u0439 \u0438\u043d\u0441\u0442\u0438\u0442\u0443\u0442",
            "logo": "/static/img/my_jobs/job_icon_1.png",
            "logo_alt": "NRCKI logo",
            "e_address": "/works/1/",
            "address": "\u0433.\u041c\u043e\u0441\u043a\u0432\u0430",
            "post": "\u0438\u043d\u0436\u0435\u043d\u0435\u0440-\u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c",
            "work_from": date(2012, 7, 1),
            'work_to': date(2014, 9, 1)
        },
        {
            "name": "\u041a\u0440\u044b\u043c\u0441\u043a\u0430\u044f a\u0441\u0442\u0440\u043e\u0444\u0438\u0437\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u043e\u0431\u0441\u0435\u0440\u0432\u0430\u0442\u043e\u0440\u0438\u044f (\u041a\u0440\u0410\u041e)",
            "logo": "/static/img/my_jobs/job_icon_2.png",
            "logo_alt": "CrAO logo",
            "e_address": "/works/2/",
            "address": "\u0440\u0435\u0441\u043f. \u041a\u0440\u044b\u043c, \u043f\u043e\u0441. \u041d\u0430\u0443\u0447\u043d\u044b\u0439",
            "post": "\u0438\u043d\u0436\u0435\u043d\u0435\u0440",
            "work_from": date(2016, 12, 1),
            'work_to': date.today()
        }

    ]

    for i in listwork:
        Works.objects.create(**i)


def add_studies():
    liststudies = [
        {
            "name": "GeekBrains",
            "logo": "/static/img/my_studies/courses_icon/geekbrains.jpg",
            "logo_alt": "geekbrains icon",
            "e_address": "https://geekbrains.ru/"
        },
        {
            "name": "Stepic",
            "logo": "/static/img/my_studies/courses_icon/stepik.png",
            "logo_alt": "stepik icon",
            "e_address": "https://stepik.org/"
        },
        {
            "name": "Springer",
            "logo": "/static/img/my_studies/courses_icon/springer.png",
            "logo_alt": "springer icon",
            "e_address": "http://www.springer.com/gp/"
        }
    ]

    for i in liststudies:
        Studies.objects.create(**i)


def add_certificate():
    listcertif = [
        {
            "place_sturies": Studies.objects.get(name='GeekBrains'),
            "course": "HTML/CSS. \u0441\u043d\u043e\u0432\u044b \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0441\u0430\u0439\u0442\u043e\u0432",
            "certif": "https://geekbrains.ru/certificates/119863"
        },
        {
            "place_sturies": Studies.objects.get(name='GeekBrains'),
            "course": "JavaScript. \u0423\u0440\u043e\u0432\u0435\u043d\u044c 1. \u043d\u0442\u0435\u0440\u0430\u043a\u0442\u0438\u0432\u043d\u044b\u0435 \u0432\u0435\u0431-\u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f",
            "certif": "https://geekbrains.ru/certificates/125628"
        },
        {
            "place_sturies": Studies.objects.get(name='GeekBrains'),
            "course": "Python. \u0423\u0440\u043e\u0432\u0435\u043d\u044c1. \u0441\u043d\u043e\u0432\u044b \u044f\u0437\u044b\u043a\u0430 \u0438 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0438 \u0432\u0435\u0431-\u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0439",
            "certif": "https://geekbrains.ru/certificates/149615"
        },
        {
            "place_sturies": Studies.objects.get(name='GeekBrains'),
            "course": "\u0432\u0438\u0434\u0435\u043e-\u043a\u0443\u0440\u0441: \u043e\u0441\u043d\u043e\u0432\u044b \u0431\u0430\u0437 \u0434\u0430\u043d\u043d\u044b\u0445. \u042f\u0437\u044b\u043a SQL",
            "certif": "https://geekbrains.ru/certificates/157677"
        },
        {
            "place_sturies": Studies.objects.get(name='GeekBrains'),
            "course": "Git. \u044b\u0441\u0442\u0440\u044b\u0439 \u0441\u0442\u0430\u0440\u0442. \u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442 \u043a\u043e\u043c\u0430\u043d\u0434\u043d\u043e\u0439 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0438",
            "certif": "https://geekbrains.ru/certificates/114635"
        },
        {
            "place_sturies": Studies.objects.get(name='Stepic'),
            "course": "\u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043d\u0430 Puthon",
            "certif": "https://stepik.org/certificate/b24673449ac0dca26c52e7327e48f035831eb4d0.pdf"
        },
        {
            "place_sturies": Studies.objects.get(name='Stepic'),
            "course": "Python: \u043e\u0441\u043d\u043e\u0432\u044b \u0438 \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u0435",
            "certif": "https://stepik.org/certificate/8b9c571dc62b5eadc75f53f5df95213a077e64b6.pdf"
        },
        {
            "place_sturies": Studies.objects.get(name='Springer'),
            "course": "Springer English Academy",
            "certif": "https://yadi.sk/i/MNK1ZFy2mVNUi"
        },
        {
            "place_sturies": Studies.objects.get(name='Springer'),
            "course": "How to Write and Submit a Journal Article",
            "certif": "https://yadi.sk/i/5IzIZJDQmXUGN"
        }


    ]

    for i in listcertif:
        Certificate.objects.create(**i)


class Command(BaseCommand):

    def handle(self, *args, **options):
        add_person()
        add_work()
        add_studies()
        add_certificate()