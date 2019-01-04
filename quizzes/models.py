from django.shortcuts import get_list_or_404
import random
from django.db import models

# Create your models here.


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
        return f"Odnośnie {self.lecture} wykładu,\n{self.question_text}"

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

    def throw_mega_answers(self):
        """
        Returns:
            list -- contain answers that user will see on quiz, max lenght of list-4, min-len( all answers belong to question)
        """
        a = get_list_or_404(self.answers)
        random.shuffle(a)
        ans = a[:4]
        return ans

    def check_mega_answer(self, quiz_answers, user_answers):
        """
        Arguments:
            quiz_answers {database object} -- all answers that user have option to pick
            user_answers {database object} -- answers that user send in request

        Returns:
            Boolean -- True if all answers was correct
        """
        correct = 0
        ans = 0
        for q in quiz_answers:
            if q.correct:
                ans += 1
        for q in user_answers:
            if q.correct:
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

    def __str__(self):
        return f'Odnośnie {self.question.lecture} pytania {self.question.question_text} \n{self.text}'