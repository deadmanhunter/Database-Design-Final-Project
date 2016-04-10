from django.db import models

# Create your models here.

# Universe the character is from
class Universe(models.Model):
    universe_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.universe_name

# Playable character from the game
class Heroes(models.Model):
	hero_name = models.CharField(max_length=200, unique=True)
	home_universe = models.ForeignKey(Universe)
	base_health = models.IntegerField()
	base_mana = models.IntegerField()
	base_attack = models.IntegerField()
	attack_range = models.IntegerField()
	passive_ability_name = models.CharField(max_length=200)
	passive_ability_description = models.CharField(max_length=500)
	has_alternates = models.BooleanField()

        def __unicode__(self):
            return self.hero_name
                # "home_universe": self.home_universe,
                # "base_health": self.base_health,
                # "base_mana": self.base_mana,
                # "base_attack": self.base_attack,
                # "attack_range": self.attack_range,
                # "passive_ability_name": self.passive_ability_name,
                # "passive_ability_description": self.passive_ability_description,
                # "has_alternates": self.has_alternates





# Basic low powered abilities that all heroes have
class Abilities(models.Model):
    hero_id = models.ForeignKey(Heroes)
    default_button = models.CharField(max_length=1)
    ability_name = models.CharField(max_length=200)
    ability_type = models.CharField(max_length=200)
    ability_description = models.CharField(max_length=500)

    def __unicode__(self):
        return self.ability_name

# Powerful high leveled abilities that all heroes have
class Ultimate(models.Model):
    hero_id = models.ForeignKey(Heroes)
    ultimate_name = models.CharField(max_length=200)
    ultimate_type = models.CharField(max_length=200)
    ultimate_description = models.CharField(max_length=500)

    def __unicode__(self):
        return self.ultimate_name
