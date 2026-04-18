from django.shortcuts import render
from .data.questions import questions_data
from .models import QuizHistory


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
    if request.method == 'POST':
        username = request.POST.get('username', 'Anonymous')
        material = request.POST.get('material', '')
        questions = questions_data.get(material, [])

        correct = 0
        wrong = 0

        for q in questions:
            submitted_answer = request.POST.get(f'q{q["id"]}', '')
            if submitted_answer == q['answer']:
                correct += 1
            else:
                wrong += 1

        total = correct + wrong
        score = round((correct / total) * 100) if total > 0 else 0

        QuizHistory.objects.create(
            username=username,
            material=material,
            score=score,
            correct=correct,
            wrong=wrong,
        )

        return render(request, 'result.html', {
            'username': username,
            'material': material,
            'correct': correct,
            'wrong': wrong,
            'score': score,
            'total': total,
        })

    return render(request, 'result.html')


def history(request):
    histories = QuizHistory.objects.all()
    return render(request, 'history.html', {'histories': histories})