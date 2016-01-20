# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False,
                                        auto_created=True,
                                        primary_key=True)),
                ('answer', models.CharField(max_length=200,
                                            verbose_name=b'Answer text')),
                ('answer_description',
                 models.TextField(max_length=20000,
                                  verbose_name=b'Answer description')),
                ('is_true', models.BooleanField(default=False,
                                                verbose_name=b'is true')),
            ], ),
        migrations.CreateModel(name='Game',
                               fields=[
                                   ('id', models.AutoField(verbose_name='ID',
                                                           serialize=False,
                                                           auto_created=True,
                                                           primary_key=True)),
                                   ('start_on', models.DateTimeField(
                                       auto_now_add=True,
                                       verbose_name=b'when was started')),
                                   ('stop_on', models.DateTimeField(
                                       verbose_name=b'when was stoped')),
                               ], ),
        migrations.CreateModel(
            name='GameQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False,
                                        auto_created=True,
                                        primary_key=True)),
                ('asked_at',
                 models.DateTimeField(auto_now_add=True,
                                      verbose_name=b'When was asked')),
                ('answered_at',
                 models.DateTimeField(null=True,
                                      verbose_name=b'When was answered',
                                      blank=True)),
                ('answer', models.ForeignKey(blank=True,
                                             to='testapp.Answer',
                                             null=True)),
                ('game', models.ForeignKey(to='testapp.Game')),
            ], ),
        migrations.CreateModel(name='Gamers',
                               fields=[
                                   ('id', models.AutoField(verbose_name='ID',
                                                           serialize=False,
                                                           auto_created=True,
                                                           primary_key=True)),
                                   ('tgm_chatid', models.CharField(
                                       max_length=200,
                                       verbose_name=b'Telegram chat id')),
                               ], ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False,
                                        auto_created=True,
                                        primary_key=True)),
                ('question', models.CharField(max_length=2000,
                                              verbose_name=b'Question text')),
                ('created_on',
                 models.DateTimeField(auto_now_add=True,
                                      verbose_name=b'When was created')),
                ('changed_on',
                 models.DateTimeField(auto_now=True,
                                      verbose_name=b'When was last changed ')),
                ('published', models.BooleanField(default=False,
                                                  verbose_name=b'is published')
                 ),
                ('qtype', models.CharField(max_length=10,
                                           verbose_name=b'question type',
                                           choices=[
                                               (b'O', b'open question'), (
                                                   b'C', b'close question')
                                           ])),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            }, ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False,
                                        auto_created=True,
                                        primary_key=True)),
                ('name', models.CharField(max_length=200,
                                          verbose_name=b'Test name')),
                ('created_on',
                 models.DateTimeField(auto_now_add=True,
                                      verbose_name=b'When was created')),
                ('changed_on',
                 models.DateTimeField(auto_now=True,
                                      verbose_name=b'When was last changed ')),
            ], ),
        migrations.CreateModel(
            name='TestQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False,
                                        auto_created=True,
                                        primary_key=True)),
                ('question', models.ForeignKey(to='testapp.Question')),
                ('test', models.ForeignKey(to='testapp.Test')),
            ], ),
        migrations.AddField(
            model_name='test',
            name='questions',
            field=models.ManyToManyField(to='testapp.Question',
                                         through='testapp.TestQuestion'), ),
        migrations.AddField(model_name='gamequestion',
                            name='question',
                            field=models.ForeignKey(to='testapp.Question'), ),
        migrations.AddField(model_name='game',
                            name='gamer',
                            field=models.ForeignKey(to='testapp.Gamers'), ),
        migrations.AddField(
            model_name='game',
            name='questions',
            field=models.ManyToManyField(to='testapp.Question',
                                         through='testapp.GameQuestion'), ),
        migrations.AddField(model_name='game',
                            name='test',
                            field=models.ForeignKey(to='testapp.Test'), ),
        migrations.AddField(model_name='answer',
                            name='question',
                            field=models.ForeignKey(to='testapp.Question'), ),
        migrations.AlterUniqueTogether(
            name='testquestion',
            unique_together=set([('test', 'question')]), ),
        migrations.AlterUniqueTogether(
            name='gamequestion',
            unique_together=set([('game', 'question')]), ),
    ]
