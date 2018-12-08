import random
from django.db import models

# Create your models here.


class Quiz:
    def __init__(self, question, answers, correct):
        self.question = question
        self.answers = answers
        self.correct = correct
        self.asking_questions = []

    def ask_questions(self):
        random.shuffle(self.answers)
        self.asking_questions = self.answers[:]
        if len(self.answers) > 4:
            while len(self.asking_questions) > 4:
                random.shuffle(self.asking_questions)
                del self.asking_questions[0]
            return self.asking_questions
        else:
            return self.asking_questions

    def check_answer(self, answers):
        correct = 0
        ans = 0
        for q in self.asking_questions:
            if q in self.correct:
                ans += 1
        for a in answers:
            if a in self.correct:
                correct +=1
        if correct == ans:
            return True
        else:
            return False

    def check_answer_basic(self, answ):
        correct = 0
        for a in answ:
            if a in self.correct:
                correct += 1
        if correct == len(self.correct):
            return True
        else:
            return False


class QuestionQuiz(models.Model):
    """
    Quiz model which belong to some lecture contain question, explantation and is connectect with anwsers
    """
    LECTURE_CHOICES = (
        (1, 'Wykład 1'),
        (2, 'Wykład 2'),
        (3, 'Wykład 3'),
        (4, 'Wykład 4'),
        (5, 'Wykład 5'),
    )
    lecture = models.IntegerField('Wykład', choices=LECTURE_CHOICES)
    question_text = models.TextField('Pytanie', unique=True)
    explanation = models.TextField('Wytłumaczenie')

    def __str__(self):
        return f"\nQuiz of {self.lecture} lecture, of id {self.id} : '{self.question_text}'\n"

    def throw_answers(self):
        """
        Returns:
            list -- contain answers that user will see on quiz, max lenght of list-4, min-len( all answers belong to question)
        """
        list_answers = [a.text for a in self.answers.all()]
        random.shuffle(list_answers)
        if len(list_answers) > 4:
            answers = []
            for i in range(4):
                answers.append(list_answers.pop())
            return answers
        else:
            return list_answers

    def check_answer(self, quiz_answers, user_answers):
        """
        Arguments:
            quiz_answers {list} -- all answers that user have option to pick
            user_answers {list} -- answers that user send in request

        Returns:
            Boolean -- True if all answers was correct
        """

        correct = 0
        ans = 0
        for q in quiz_answers:
            if self.answers.get(text=q).correct:
                ans += 1
        for q in user_answers:
            if self.answers.get(text=q).correct:
                correct += 1
            else:
                correct -= 1
        if correct == ans:
            return True
        else:
            return False


class AnswerQuiz(models.Model):
    """
    Model belong with QuestionQuiz, it describes answer and define with relation one-to-many with which question in connected.
    """

    question = models.ForeignKey(
        QuestionQuiz,
        on_delete=models.CASCADE,
        related_name='answers',
        related_query_name='answer',
        )
    text = models.TextField('Treść')
    correct = models.BooleanField('Zgodność')