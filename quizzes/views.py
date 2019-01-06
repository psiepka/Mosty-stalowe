from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import QuestionQuiz, AnswerQuiz
from random import shuffle, choice
from copy import copy
# Create your views here.


def quiz_start(request, lecture):
    """
    This page load quiz questions and other informations which are needed to start quiz of specific lecture.
    All data is store in request.session.
    I program this in that way, that quest can use quizzes and see thier result without registration and login.
    Arguments:
        lecture {int} -- this iteger describe quiz lecture from questions will be base on.
    Returns:
        Page with all quiz of lecture, which we store in database.
    """
    quizes = get_list_or_404(QuestionQuiz, lecture=lecture)
    dict_quizes = {lecture : { q.id : { a : False for a in q.throw_answers() } for q in quizes}}
    shuffle(dict_quizes)
    request.session.flush()
    request.session['quizzes'] = dict_quizes
    request.session['progress'] = {
        lecture : {
            'lenght' : len(request.session['quizzes'][lecture]),
            'remained' : [q.id for q in quizes]
            }
    }
    request.session.set_expiry(0)
    shuffle(request.session['progress'][lecture]['remained'])
    question = request.session['progress'][lecture]['remained'][0]
    return redirect('quiz_base', lecture=lecture, question=question)


def quiz_base(request, lecture, question):
    lec = str(lecture)
    base_quiz = request.session['quizzes']
    if not base_quiz:
        return redirect('quiz_start', lecture=lecture)
    quiz = QuestionQuiz.objects.get(id=question)
    questions_quiz = request.session['quizzes'][lec][str(question)]
    quiz_ans = [ q for q in questions_quiz ]
    progress_current = (request.session['progress'][lec]['lenght'] - len(request.session['progress'][lec]['remained'])) + 1
    progress_all = request.session['progress'][lec]['lenght']
    content = {
        'progress_current': progress_current,
        'progress_all' : progress_all,
        'quiz' : quiz,
        'ans': quiz_ans,
        'title' : 'Quiz',
    }
    if request.method == "POST":
        request.session['quizzes'][str(quiz.lecture)][str(quiz.id)].update(
            {
                a : True for a in quiz_ans if quiz.answers.get(text=a).correct
                }
        )
        prev_ans = { q : b for q, b in request.session['quizzes'][str(quiz.lecture)][str(quiz.id)].items()}
        request.session['quizzes'][str(quiz.lecture)][str(quiz.id)].update(
            { 'outcome': {
                'text' : quiz.question_text,
                'exp' : quiz.explanation,
                'score' : quiz.check_answer(quiz_ans, request.POST.getlist(str(quiz.id))),
                'send' : request.POST.getlist(str(quiz.id)),
                'ans' : prev_ans
            }}
        )
        request.session.modified = True
        del request.session['progress'][lec]['remained'][0]
        try:
            quiz = request.session['progress'][lec]['remained'][0]
            return redirect('quiz_base', lecture=int(lec), question=int(quiz))
        except IndexError:
            return redirect('quiz_result', lecture=lec)
    return render(request, 'quizzes/quiz_base.html', context=content)


def quiz_result(request, lecture):
    if not request.session['quizzes'][str(lecture)]:
        return redirect('quiz_start', lecture=lecture)
    q_all = 0
    q_correct = 0
    quizzes = request.session['quizzes'][str(lecture)].items()
    for key, val in quizzes:
        q_all += 1
        if val['outcome']['score']:
            q_correct += 1
    result = int((q_correct/q_all)*100)
    context = {
        'lecture' : int(lecture),
        'result': result,
        'quiz': quizzes,
    }
    return render(request, 'quizzes/result_quiz.html', context=context)

def quiz_mega_start(request):
    """
    This page load quiz questions and other informations which are needed to start quiz of every mixed lecture.
    All data is store in request.session.
    I program this in that way, that quest can use quizzes and see thier result without registration and login.
    Arguments:
        none
    Returns:
        Page with all quiz of lecture, which we store in database.
    """
    quiz = choice(get_list_or_404(QuestionQuiz))
    try:
        request.session['mega']
        last_question = QuestionQuiz.objects.filter(id=int(request.session['mega']['id'])).first()
        while quiz == last_question:
            quiz = choice(get_list_or_404(QuestionQuiz))
    except KeyError:
        pass
    question = quiz.id
    return redirect('quiz_mega', question=question)


def quiz_mega(request, question):
    """
    This page load quiz questions and other informations which are needed to start quiz of every mixed lecture.
    All data is store in request.session.
    I program this in that way, that quest can use quizzes and see thier result without registration and login.
    Arguments:
        none
    Returns:
        Page with all quiz of lecture, which we store in database.
    """
    quiz = get_object_or_404(QuestionQuiz, id=question)
    ans = quiz.throw_answers()
    content = {
        'question':quiz,
        'ans':ans,
    }
    if request.method == "POST":
        if 'submit' in request.POST:
            request.session['mega'] = {
                'id': quiz.id,
                'text' : quiz.question_text,
                'exp' : quiz.explanation,
                'score' : quiz.check_answer(ans, request.POST.getlist('mega')),
                'send' : request.POST.getlist('mega'),
                'ans' : ans,
                'answers' : [a for a in ans if AnswerQuiz.objects.filter(question=quiz, text=a).first().correct],
            }
            return redirect('quiz_mega_start')
    return render(request, 'quizzes/quiz_mega.html', context=content)


def quiz_view_all(request, lecture):
    quiz = QuestionQuiz.objects.filter(lecture=lecture)
    return render(request, 'quizzes/quiz_all.html', {'quiz':quiz})
