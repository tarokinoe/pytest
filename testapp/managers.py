# -*- encoding: utf-8 -*-

from django.db import models
from django.db.models import F
from testapp.exceptions import OpenGameAlreadyExists


class GameManager(models.Manager):
    def create_game(self, player, test):
        #open_games = self.open_games(player=player)
        open_games = player.current_game()
        if open_games:
            raise OpenGameAlreadyExists
        else:
            return self.create(player=player, test=test)
    # def open_games(self, player):
    #    return self.filter(player=player).filter(state=self.model.OPEN)


class PlayerManager(models.Manager):
    def create_tgm_user(self, user):
        player = self.model(tgm_user_id=user.id)
        if user.first_name:
            player.tgm_first_name = user.first_name
        if user.last_name:
            player.tgm_last_name = user.last_name
        if user.username:
            player.tgm_user_name = user.username
        player.save()
        return player


class TestManager(models.Manager):
    def get_by_name(self, testname):
        test = self.model.objects.filter(published=True).filter(
            name__exact=testname).first()
        return test


class GameQuestionManager(models.Manager):
    def right_answers(self, game):
        return self.get_queryset().filter(game=game).exclude(
            player_answer='').filter(player_answer=F('right_answer'))
