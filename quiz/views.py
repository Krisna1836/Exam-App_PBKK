from django.shortcuts import render
from .data.questions import questions_data

def home(request):
    materials = [
        {"key": "auth", "name": "Authentication & Security"},
        {"key": "forms", "name": "Forms & Static Files"},
        {"key": "orm", "name": "ORM & Migration"},
    ]

    return render(request, 'home.html', {'materials': materials})


def username(request, material):
    return render(request, 'username.html', {'material': material})


def quiz(request, material):
    questions = questions_data.get(material, [])

    return render(request, 'quiz.html', {
        'questions': questions,
        'material': material
    })


def result(request):
    return render(request, 'result.html')


def history(request):
    return render(request, 'history.html')