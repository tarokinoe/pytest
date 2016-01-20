# -*- encoding: utf-8 -*-

from django.contrib import admin
from testapp.models import Answer, Game, GameQuestion, \
    Player, Question, Test, TestQuestion


class TestQuestionInline(admin.TabularInline):
    model = TestQuestion
    extra = 1


class TestAdmin(admin.ModelAdmin):
    list_display = ('name', 'published')
    list_filter = ('published', )
    inlines = [TestQuestionInline, ]


admin.site.register(Test, TestAdmin)


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', )
    inlines = [AnswerInline, ]


admin.site.register(Question, QuestionAdmin)


class AnswerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Answer, AnswerAdmin)


class TestQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'test')
    list_filter = ('test', )


admin.site.register(TestQuestion, TestQuestionAdmin)


class PlayerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Player, PlayerAdmin)


class GameAdmin(admin.ModelAdmin):
    pass


admin.site.register(Game, GameAdmin)


class GameQuestionAdmin(admin.ModelAdmin):
    list_filter = ('game', )


admin.site.register(GameQuestion, GameQuestionAdmin)
