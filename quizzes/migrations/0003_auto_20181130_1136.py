# Generated by Django 2.1.3 on 2018-11-30 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0002_auto_20181130_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerQuiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Treść')),
                ('correct', models.BooleanField(verbose_name='Zgodność')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', related_query_name='answer', to='quizzes.QuestionQuiz')),
            ],
        ),
        migrations.RemoveField(
            model_name='anwserquiz',
            name='question',
        ),
        migrations.DeleteModel(
            name='AnwserQuiz',
        ),
    ]
