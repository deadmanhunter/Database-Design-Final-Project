# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

def loadData(apps, schema_editor):

    # Load universes
    Universe = apps.get_model("hots", "Universe")

    Universe(universe_name="Starcraft").save()
    Universe(universe_name="Diablo").save()
    Universe(universe_name="World of Warcraft").save()
    Universe(universe_name="Earth").save()
    Universe(universe_name="Overwatch").save()


    # Load heroes
    Heroes = apps.get_model("hots", "Heroes")

    #Heroes(hero_name='', home_universe=Universe.objects.get(universe_name=""), base_health=0, base_mana=0, base_attack=0, attack_range=0, passive_ability_name='', passive_ability_description="", has_alternates=False).save()
    Heroes(hero_name='Abathur', home_universe=Universe.objects.get(universe_name="Starcraft"), base_health=713, base_mana=0, base_attack=27, attack_range=1, passive_ability_name='Locust Strain', passive_ability_description='Spawns a Locust to attack down the nearest lane', has_alternates=False).save()
    # Heroes(hero_name='Azmodan', home_universe=Universe.objects.get(universe_name="Diablo"), base_health=2,848, base_mana=500, base_attack=88, attack_range=5.5, passive_ability_name='General of Hell', passive_ability_description="", has_alternates=False).save()


    # Load basic Abilities
    Abilities = apps.get_model("hots", "Abilities")

    #Abilities(hero_id=Heroes.objects.get(hero_name=""), default_button="", ability_name="", ability_type="", ability_description="").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Abathur"), default_button="q", ability_name="Symbiote", ability_type="Special", ability_description="Assist another allied Unit or Combat Structure, allowing you to shield them and use new Abilities.Cannot be used on another Hero's Summons.").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Abathur"), default_button="w", ability_name="Toxic Nest", ability_type="Summon", ability_description="Charge Spawn a mine that becomes active after a short time. Deals 50 (+15 per level) damage and reveals the enemy for 4 seconds. Lasts 90 seconds.").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Abathur"), default_button="q", ability_name="Symbiote - Stab", ability_type="Damage", ability_description="Shoots a spike towards target area that deals 113 (+4% per level) damage to the first enemy it contacts.").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Abathur"), default_button="w", ability_name="Symbiote - Spike Burst", ability_type="Damage", ability_description="Deals 111 (+4% per level) damage to nearby enemies.").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Abathur"), default_button="e", ability_name="Symbiote - Carapace", ability_type="Shield", ability_description="Shields the assisted ally for 150 (+4% per level). Lasts for 8 seconds.").save()


    # Load Ultimates
    Ultimate = apps.get_model("hots", "Ultimate")

    # Ultimate(hero_id=Heroes.objects.get(hero_name=""), ultimate_name="", ultimate_type="", ultimate_description="").save()

    Ultimate(hero_id=Heroes.objects.get(hero_name="Abathur"), ultimate_name="Ultimate Evolution", ultimate_type="Summon", ultimate_description="Clone target allied Hero and control it for 20 seconds. Abathur has perfected the clone, granting it 20% Ability Power, 20% bonus Attack Damage, and 10% bonus Movement Speed. Cannot use their Heroic Ability.").save()
    Ultimate(hero_id=Heroes.objects.get(hero_name="Abathur"), ultimate_name="Evolve Monstrosity", ultimate_type="Summon", ultimate_description="Turn an allied Minion or Locust into a Monstrosity.").save()

class Migration(migrations.Migration):

    dependencies = [
        ('hots', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(loadData)
    ]