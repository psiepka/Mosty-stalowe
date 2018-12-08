from django.shortcuts import render, redirect, get_list_or_404
from .models import Quiz, QuestionQuiz
from random import shuffle
# Create your views here.

w2_q1 = Quiz('W których mostach występuje siła rozporowa?',['ramowym', 'łukowym', 'wiszącym', 'belkowym - gerberowskim'], ['ramowym','łukowym',])
w2_q2 = Quiz('Wprowadzenie zmiennej wysokości belek ciągłych w mostach powoduje :',['zwiększenia momentów podporowych','zminiejszenie momentów podporowych', 'zmniejszenia momentów przęsłowych','zwiększenie momentów przęsłowych'],['zmniejszenia momentów przęsłowych','zwiększenia momentów podporowych'])
w2_q3 = Quiz('Które z systemów statycznych powinno stosować się przy dużych i bardzo dużych rozpiętościach?',['belkowy', 'kratowy', 'wiszący', 'wantowy'],['wiszący', 'wantowy'])
w2_q4 = Quiz('Które czynniki określają wymagania gospodarcze?', ['tworzywo z którego wykonamy obiekt', 'skrajnie mostu','wykorzystanie terenu pod mostem', 'przekrój geologiczny pod mostem'],['wykorzystanie terenu pod mostem'])
w2_q5 = Quiz('Które zdania odpowiadają mostom podwieszanym?',['pomost przenosi momenty zginające i siły podłużne', 'siły poziome przenoszone są na przyczółki','pomost może być blachownicą lub kratą', 'krzywoliniowy kształt ciegien'], ['pomost przenosi momenty zginające i siły podłużne', 'pomost może być blachownicą lub kratą'])
w2_q6 = Quiz('Które z cech są zaletami mostów stalowych? (w porównaniu do mostów wykonanych z betonu)',['trwałość', 'monolityczność', 'wrażliwość na obciążenie o charakterze dynamicznym','odporność na korozje'], [])
w2_q7 = Quiz('Które z systemów statycznych mostów nie stosuje się na teranach rzecznych lub \'podmokłych\'?',['mosty ramowe','mosty belkowe', 'mosty wiszące', 'mosty łukowe'], ['mosty ramowe'])
w2_q8 = Quiz('Obciążenie pionowe wywołuje oddziaływanie poziome na fundament zwrócone w kierunku przeszkody - to zdanie dotyczy?',['mostów łukowych','mostów ramowych', 'mostów wiszących', 'mostów podwieszanych'], ['mostów wiszących', 'mostów podwieszanych'])
w2_q9 = Quiz('Dynamicznie które rozwiązanie jest najkorzystniejsze w kontekscie mostów kratowych?',['z jadą górą', 'z jazdą pośrednią', 'z jazdą dołem'], ['z jazdą dołem',])
w2_q10 = Quiz('Które z rozwiązań mostów belkowych, jest niewrażliwe na osiadanie podpór?', ['swobodnie podparte jednoprzęsłowe','wieloprzęsłowe — ciągle o zmiennej wysokości', 'zespół przęseł swobodnie podpartych w moście wieloprzęsłowym', 'wieloprzęsłowe - przegubowe'],['swobodnie podparte jednoprzęsłowe', 'zespół przęseł swobodnie podpartych w moście wieloprzęsłowym', 'wieloprzęsłowe - przegubowe'])
wyklad2_quiz = [w2_q1, w2_q2, w2_q3, w2_q4, w2_q5, w2_q6, w2_q7, w2_q8, w2_q9, w2_q10]


def quiz_2(request):
    quiz = wyklad2_quiz
    quiz_e = enumerate(quiz)
    context = {
        'quiz_e':quiz_e,
        'title':'Quiz 2',
        'quiz': quiz,
    }
    if request.method == "POST":
        result = 0
        data = {}
        for i in range(len(quiz)):
            data[i] = quiz[i].check_answer_basic(request.POST.getlist(str(i)))
            if data[i] == True:
                result += 1
        result = round((result/len(quiz))*100)
        return render(request, 'quizzes/result.html', {'wynik':request.POST.getlist(str(i)), 'data':data})
    return render(request, 'quizzes/quiz_2.html', context=context)


w3_q1 = Quiz('Wszystkie stalowe pomosty muszą składać się z :', ['podłużnicy', 'dźwigarów głównych', 'poprzecznic', 'płyty pomostowej'],['dźwigarów głównych'])
w3_q2 = Quiz('Zaznacz prawidłowe zdania odnośnie pracy statycznej mostów',['płyta pomostu przekazuje obciążenia z belek pomostowych na dźwigary główne','płyta pomostu przekazuje obciążenia z belek pomostowych na dźwigary główne oraz współpracuje z nimi','niewspółpracująca płyta pomostowa z dźwigarmai głównymi tworzy przestrzenny układ statytczny'],[])
w3_q3 = Quiz('Zaznacz prawidłowe zdania odnośnie poprzecznicy',['poprawiają współpracę między dźwigarami głównymi','w pomoście współpracującym, nie muszą występować', 'w przypadku pomostu z blach nieckowych nie muszą występować', 'w przypadku pomostu z blach ortotropowym nie muszą występować'],['poprawiają współpracę między dźwigarami głównymi','w pomoście współpracującym, nie muszą występować'])
w3_q4 = Quiz('Zaznacz prawidłowe zdania odnośnie poprzecznicy',['poprawiają współpracę między dźwigarami głównymi','w pomoście współpracującym, nie muszą występować', 'w przypadku pomostu z blach nieckowych nie muszą występować', 'w przypadku pomostu z blach ortotropowym nie muszą występować'],['w pomoście współpracującym, nie muszą występować','w przypadku pomostu z blach ortotropowym nie muszą występować'])
w3_q5 = Quiz("Czym w kontekście połaczeń elementów konstrukcji nazywamy 'rybkami'? ", ['żeberka usztywniające', 'usztywnianie poprzeczne', 'nakładki ciągłości', 'otwory w blachach zapobiegającym krzyżowanie się spoin'],['nakładki ciągłości'])
w3_q5 = Quiz('Który z pomostów charakteryzuję się zróżnicowaną sztywnością w kierunkach prostopadłych',['pomost z blach nieckowych', 'pomost amerykański', 'pomost z blach ortotropowej', 'pomost z tworzyw sztucznych'],['pomost z blach ortotropowej'])
w3_q6 = Quiz("Czym w kontekście połaczeń elementów konstrukcji nazywamy 'stolikami' ?", ['żeberka usztywniające', 'usztywnianie poprzeczne', 'nakładki ciągłości','otwory w blachach zapobiegającym krzyżowanie się spoin'], ['żeberka usztywniające'])
w3_q7 = Quiz('W połaczeniu poprzecznicy z podłużnicą ...', ['stolik zwiększa grubość pasa górnego podłużnicy','rybki zwiększają grubość pasa górnego podłużnicy', 'krzyżowanie pasów górnych w jednym poziomie powoduje ograniczenie karbu naprężeń','musimy stosować żeberka usztywniające'],['rybki zwiększają grubość pasa górnego podłużnicy', 'krzyżowanie pasów górnych w jednym poziomie powoduje ograniczenie karbu naprężeń','musimy stosować żeberka usztywniające'])
w3_q8 = Quiz("Czym w kontekście połaczeń elementów konstrukcji nazywamy 'wstawkami' ?", ['żeberka usztywniające', 'usztywnianie poprzeczne', 'nakładki ciągłości','otwory w blachach zapobiegającym krzyżowanie się spoin'], ['żeberka usztywniające'])
w3_q9 = Quiz('Który z elementów powinin być najgrubszy, w pomoście ortotropowym?',['blacha ortotoropowa','pas dolny podłużnicy','pas dolny poprzecznicy','żebro podłuzne'],['blacha ortotoropowa'])
w3_q10 = Quiz('Zaznacz zdania prawdziwe',['pomost zespolony jest pomostem zamkniętym', 'mostownice są stosowane wyłącznie na obiektach mostowych', 'pomost otwarty składa się z belek pomostu oraz płyty pomostowej','mostownice mogą być drewniane oraz stalowe'],['pomost zespolony jest pomostem zamkniętym','mostownice mogą być drewniane oraz stalowe'])
wyklad3_quiz = [w3_q1, w3_q2, w3_q3, w3_q4, w3_q5, w3_q6, w3_q7, w3_q8, w3_q9, w3_q10]


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
    dict_quizes = {lecture : { q.id : { a : None for a in q.throw_answers() } for q in quizes}}
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
    return redirect('quiz_base', lecture=lecture)


def quiz_base(request, lecture):
    lec = str(lecture)
    if not request.session['quizzes'][lec]:
        return redirect('quiz_start',lecture=lecture)
    quiz = QuestionQuiz.objects.get(id=request.session['progress'][lec]['remained'][0])
    quiz_ans = [ q for q in request.session['quizzes'][lec][str(request.session['progress'][lec]['remained'][0])] ]
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
        prev_q = quiz
        prev_ans = quiz_ans
        request.session['quizzes'][str(prev_q.lecture)][str(quiz.id)].update(
            {
                a : True for a in prev_ans if prev_q.answers.get(text=a).correct
                }
        )
        request.session['quizzes'][str(prev_q.lecture)][str(quiz.id)].update(
            { 'outcome': {
                'text' : quiz.question_text,
                'exp' : quiz.explanation,
                'score' : quiz.check_answer(prev_ans, request.POST.getlist(str(quiz.id))),
                'send' : request.POST.getlist(str(quiz.id)),
                'ans' : prev_ans
            }}
        )
        result = quiz.check_answer(prev_ans, request.POST.getlist(str(quiz.id)))
        del request.session['progress'][lec]['remained'][0]
        if not request.session['progress'][lec]['remained']:
            if request.session['quizzes'][lec]:
                q_all = 0
                q_correct = 0
                for key, val in request.session['quizzes'][str(quiz.lecture)].items():
                    q_all += 1
                    if val['score']:
                        q_correct += 1
                result = int((q_correct/q_all)*100)
                return render(request, 'quizzes/result_quiz.html', {'result': result, 'lecture' : int(lecture) })
            else:
                return redirect('quiz_start', lecture=lecture)
        quiz = QuestionQuiz.objects.get(id=request.session['progress'][lec]['remained'][0])
        quiz_ans = [ q for q in request.session['quizzes'][lec][str(request.session['progress'][lec]['remained'][0])] ]
        progress_current = (request.session['progress'][lec]['lenght'] - len(request.session['progress'][lec]['remained'])) + 1
        content = {
            'progress_current': progress_current,
            'progress_all' : progress_all,
            'result' : result,
            'prev_q' : prev_q,
            'quiz' : quiz,
            'ans': quiz_ans,
            'title' : 'Quiz'
            }
        return render(request, 'quizzes/quiz_base.html', context=content)
    return render(request, 'quizzes/quiz_base.html', context=content)
