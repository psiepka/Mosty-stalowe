from quizzes.models import QuestionQuiz, AnswerQuiz

q = QuestionQuiz(lecture=2, question_text='W których mostach występuje siła rozporowa?', explanation='Mosty ramowe i łukowe są mostami rozporowymi.')

a = AnswerQuiz(question=q, text='ramowych', correct=True)

a = AnswerQuiz(question=q, text='łukowych', correct=True)

a = AnswerQuiz(question=q, text='belkowych-gerberowskich', correct=False)

a = AnswerQuiz(question=q, text='wiszących', correct=False)



q = QuestionQuiz(lecture=2, question_text='Wprowadzenie zmiennej wysokości belek ciągłych w mostach powoduje:', explanation='Wprowadzenie do belek ciągłych zmiennej wysokości (rys.wykład 2) utrudnia nieco wykonanie belek, ale wprowadza na ogół korzystne zmiany w przebiegu momentów — prowadzi do zwiększenia momentów podporowych i zmniejszenia momentów przęsłowych.')

a = AnswerQuiz(question=q, text='zwiększenia momentów podporowych', correct=True)

a = AnswerQuiz(question=q, text='zwiększenia momentów przęsłowy', correct=False)

a = AnswerQuiz(question=q, text='zmniejszenia momentów przęsłowych', correct=True)

a = AnswerQuiz(question=q, text='zmniejszenia momentów podporowych', correct=False)



q = QuestionQuiz(lecture=2, question_text='Które z systemów statycznych powinno stosować się przy dużych i bardzo dużych rozpiętościach?', explanation='Mosty wiszące oraz podwieszane (wantowe) stosuje się przy dużych i bardzo dużych rozpiętościach.')

a = AnswerQuiz(question=q, text='belkowy', correct=False)

a = AnswerQuiz(question=q, text='ramowy', correct=False)

a = AnswerQuiz(question=q, text='wiszący', correct=True)

a = AnswerQuiz(question=q, text='wantowy', correct=True)

a = AnswerQuiz(question=q, text='podwieszay', correct=True)

