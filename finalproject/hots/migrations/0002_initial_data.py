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

    #Heroes(hero_name='', hero_type="", home_universe=Universe.objects.get(universe_name=""), base_health=0, base_mana=0, base_attack=0, attack_range=0, passive_ability_name='', passive_ability_description="", has_alternates=False).save()
    Heroes(hero_name='Abathur', hero_type="Specialist", home_universe=Universe.objects.get(universe_name="Starcraft"), base_health=713, base_mana=0, base_attack=27, attack_range=1, passive_ability_name='Locust Strain', passive_ability_description='Spawns a Locust to attack down the nearest lane', has_alternates=False).save()
    Heroes(hero_name='Azmodan', hero_type="Specialist", home_universe=Universe.objects.get(universe_name="Diablo"), base_health=2848, base_mana=500, base_attack=88, attack_range=5, passive_ability_name='General of Hell', passive_ability_description="Summon a Demon Lieutenant at an allied Mercenary, Minion, or Summon. The Lieutenant will march with the target, granting 15% increased damage and 15% increased maximum Health to all nearby friendly Mercenaries, Minions, and Summons. Unlimited range.", has_alternates=False).save()
    Heroes(hero_name='Li Li', hero_type="Support", home_universe=Universe.objects.get(universe_name="World of Warcraft"), base_health=1615, base_mana=500, base_attack=66, attack_range=5, passive_ability_name='Fast Feet', passive_ability_description="Upon taking damage, gain 10% Movement Speed for 1 second.", has_alternates=False).save()
    Heroes(hero_name='Tracer', hero_type="Assassin", home_universe=Universe.objects.get(universe_name="Overwatch"), base_health=1270, base_mana=20, base_attack=29, attack_range=6, passive_ability_name='Reload', passive_ability_description="You can Basic Attack while moving, and after attacking 10 times you need to reload over 0.75 seconds. You can manually reload early by activating Reload.", has_alternates=False).save()
    Heroes(hero_name='Sonya', hero_type="Warrior", home_universe=Universe.objects.get(universe_name="Diablo"), base_health=2435, base_mana=100, base_attack=92, attack_range=1, passive_ability_name='Fury', passive_ability_description="Use Fury instead of Mana, which is gained by taking or dealing damage. Using a Basic or Heroic Ability grants 10% Movement Speed for 4 seconds.", has_alternates=False).save()
    Heroes(hero_name='Nova', hero_type="Assassin", home_universe=Universe.objects.get(universe_name="Starcraft"), base_health=1350, base_mana=0, base_attack=109, attack_range=6, passive_ability_name='Permanent Cloak, Sniper', passive_ability_description="Gain Stealth when out of combat for 3 seconds.", has_alternates=False).save()
    Heroes(hero_name='ETC', hero_type="Warrior", home_universe=Universe.objects.get(universe_name="World of Warcraft"), base_health=2659, base_mana=500, base_attack=103, attack_range=1, passive_ability_name='Rockstar', passive_ability_description="When you use a Basic or Heroic ability, give 20% Attack Speed for 4 seconds to all nearby allied Heroes.", has_alternates=False).save()
    Heroes(hero_name='Sylvanas', hero_type="Specialist", home_universe=Universe.objects.get(universe_name="World of Warcraft"), base_health=1515, base_mana=500, base_attack=85, attack_range=5, passive_ability_name='Black Arrows', passive_ability_description="Basic Attacks and Abilities stun Minions, Mercenaries, and Towers for 1 second", has_alternates=False).save()
    Heroes(hero_name='Lt. Morales', hero_type="Support", home_universe=Universe.objects.get(universe_name="Starcraft"), base_health=840, base_mana=500, base_attack=40, attack_range=5, passive_ability_name='Cadeceus Reactor', passive_ability_description="Regenerate 3.12% of your maximum Health every second after not taking damage for 4 seconds.", has_alternates=False).save()
    Heroes(hero_name='Jaina', hero_type="Assassin", home_universe=Universe.objects.get(universe_name="World of Warcraft"), base_health=1420, base_mana=500, base_attack=62, attack_range=5, passive_ability_name='Frostbite', passive_ability_description="All abilities Chill targets, slowing Movement Speed by 25% and amplifying damage from your abilities by 50%. Lasts 4 seconds.", has_alternates=False).save()



    # Load basic Abilities
    Abilities = apps.get_model("hots", "Abilities")

    #Abilities(hero_id=Heroes.objects.get(hero_name=""), default_button="", ability_name="", ability_type="", ability_description="").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Abathur"), default_button="q", ability_name="Symbiote", ability_type="Special", ability_description="Assist another allied Unit or Combat Structure, allowing you to shield them and use new Abilities.Cannot be used on another Hero's Summons.").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Abathur"), default_button="w", ability_name="Toxic Nest", ability_type="Summon", ability_description="Charge Spawn a mine that becomes active after a short time. Deals 50 (+15 per level) damage and reveals the enemy for 4 seconds. Lasts 90 seconds.").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Abathur"), default_button="q", ability_name="Symbiote - Stab", ability_type="Damage", ability_description="Shoots a spike towards target area that deals 113 (+4% per level) damage to the first enemy it contacts.").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Abathur"), default_button="w", ability_name="Symbiote - Spike Burst", ability_type="Damage", ability_description="Deals 111 (+4% per level) damage to nearby enemies.").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Abathur"), default_button="e", ability_name="Symbiote - Carapace", ability_type="Shield", ability_description="Shields the assisted ally for 150 (+4% per level). Lasts for 8 seconds.").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Azmodan"), default_button="q", ability_name="Globe of Annihilation", ability_type="Damage", ability_description="Shoot a globe of destruction, dealing 164↑ damage on impact. Long range.").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Azmodan"), default_button="w", ability_name="Summon Demon Warrior", ability_type="Summon", ability_description="Charge Spawn a Demon Warrior that marches toward a point. Warriors deal 40 (+2 per level) damage per second and last for 10 seconds.").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Azmodan"), default_button="e", ability_name="All Shall Burn", ability_type="Damage", ability_description="Channel a death beam on an enemy dealing 100↑ damage a second. The damage amount grows to 150↑ after 1.5 seconds, then 200↑ after another 1.5 seconds. Does 25% more damage to Structures.").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Li Li"), default_button="q", ability_name="Healing Brew", ability_type="Heal", ability_description="Heal lowest Health ally (prioritizing Heroes)").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Li Li"), default_button="w", ability_name="Cloud Serpent", ability_type="Summon", ability_description="Summon a Cloud Serpent on target allied Hero that automatically attacks nearby enemies").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Li Li"), default_button="e", ability_name="Blinding Wind", ability_type="Blind", ability_description="Throw a cloud of Blinding Wind at the 2 nearest enemies (prioritizing Heroes), dealing 43 (+13 per level) damage. Affected targets miss all Basic Attacks for the next 2 seconds").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Tracer"), default_button="q", ability_name="Blink", ability_type="Dash", ability_description="Dash towards an area").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Tracer"), default_button="w", ability_name="Melee", ability_type="Damage", ability_description="Deal 264.16 (+4% per level) damage to a nearby enemy, prioritizing Heroes. Gain 5% Pulse Bomb charge when damaging an enemy, and 10% against Heroes.").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Tracer"), default_button="e", ability_name="Recall", ability_type="Teleport", ability_description="Return to the position you were at 3 seconds ago, refill your ammo, and remove all negative status effects from yourself.").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Sonya"), default_button="q", ability_name="Ancient Spear", ability_type="Dash", ability_description="Throw out a spear that pulls you to the first enemy hit").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Sonya"), default_button="w", ability_name="Siesmic Slam", ability_type="Damage", ability_description="Deals 176 (+4% per level) damage to the target enemy, and 44 (+4% per level) to enemies behind the target.").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Sonya"), default_button="e", ability_name="Whirlwind", ability_type="Damage", ability_description="Deals 210 (+35 per level) damage to nearby enemies over 3 seconds, and heals for 20% of damage dealt. Healing tripled versus Heroes.").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Nova"), default_button="q", ability_name="Snipe", ability_type="Damage", ability_description="Deals 310 (+4% per level) damage to the first enemy hit.").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Nova"), default_button="w", ability_name="Pinning Shot", ability_type="Slow", ability_description="Deal 50 (+10 per level) damage to an enemy and slow it by 40% for 2.25 seconds.").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Nova"), default_button="e", ability_name="Holo Decoy", ability_type="Decoy", ability_description="Create a Decoy for 5 seconds that appears to attack enemies. Using this Ability does not break Cloak.").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="ETC"), default_button="q", ability_name="Powerslide", ability_type="Dash", ability_description="Slide to a location dealing 67 (+7 per level) damage and stunning enemies hit for 1.25 second.").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="ETC"), default_button="w", ability_name="Face Melt", ability_type="Knock-back", ability_description="Deals 55 (+5 per level) damage to nearby enemies, knocking them back.").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="ETC"), default_button="e", ability_name="Guitar Solo", ability_type="Heal", ability_description="Regenerate 27 (+6.5 per level) Health per second for 4 seconds.").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Sylvanas"), default_button="q", ability_name="Withering Fire", ability_type="Damage", ability_description="Charge Shoot the closest enemy for 48 (+4% per level) damage, preferring Heroes. Stores 5 charges. Gain 1 charge on nearby enemy Minion or Mercenary deaths, and 3 charges on nearby enemy Hero deaths.").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Sylvanas"), default_button="w", ability_name="Shadow Dagger", ability_type="Damage", ability_description="Deals 13.5 (+3.5 per level) damage and an additional 54 (+14 per level) damage over 2 seconds to target unit. The effect spreads to nearby targets.").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Sylvanas"), default_button="e", ability_name="Haunting Wave", ability_type="Teleport", ability_description="Send forth a wave of banshees dealing 41 (+11 per level) damage to all targets. Reactivate to teleport to the banshees' location.").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Lt. Morales"), default_button="q", ability_name="Healing Beam", ability_type="Healing", ability_description="Heal an ally for 200 (+4% per level) health a second as long as they are in range. Reactivate to switch targets, or activate your Trait to cancel the channel.").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Lt. Morales"), default_button="w", ability_name="Safeguard", ability_type="Damage Reduction", ability_description="Grant target ally Resistant, reducing damage taken by 25% for 3 seconds.").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Lt. Morales"), default_button="e", ability_name="Displacement Grenade", ability_type="Knock-back", ability_description="Fire a grenade that explodes on the first enemy hit, dealing 219 (+4% per level) damage, knocking enemies away.").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Jaina"), default_button="q", ability_name="Frost Bolt", ability_type="Damage", ability_description="Deal 190 (+4% per level) damage.").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Jaina"), default_button="w", ability_name="Blizzard", ability_type="Damage", ability_description="Bombard an area with 2 waves of ice, dealing 365 damage each").save()
    Abilities(hero_id=Heroes.objects.get(hero_name="Jaina"), default_button="e", ability_name="Cone of Cold", ability_type="Damage", ability_description="Deal 200 (+4% per level) damage").save()


    # Load Ultimates
    Ultimate = apps.get_model("hots", "Ultimate")

    # Ultimate(hero_id=Heroes.objects.get(hero_name=""), ultimate_name="", ultimate_type="", ultimate_description="").save()

    Ultimate(hero_id=Heroes.objects.get(hero_name="Abathur"), ultimate_name="Ultimate Evolution", ultimate_type="Summon", ultimate_description="Clone target allied Hero and control it for 20 seconds. Abathur has perfected the clone, granting it 20% Ability Power, 20% bonus Attack Damage, and 10% bonus Movement Speed. Cannot use their Heroic Ability.").save()
    Ultimate(hero_id=Heroes.objects.get(hero_name="Abathur"), ultimate_name="Evolve Monstrosity", ultimate_type="Summon", ultimate_description="Turn an allied Minion or Locust into a Monstrosity.").save()
    Ultimate(hero_id=Heroes.objects.get(hero_name="Azmodan"), ultimate_name="Demonic Invasion", ultimate_type="Summon", ultimate_description="Rain a small army of Demonic Grunts down on enemies").save()
    Ultimate(hero_id=Heroes.objects.get(hero_name="Azmodan"), ultimate_name="Black Pool", ultimate_type="Damage Boost", ultimate_description="Create a pool that empowers Azmodan, his Demons, and allied Minions, increasing their attack and ability damage by 75%").save()
    Ultimate(hero_id=Heroes.objects.get(hero_name="Li Li"), ultimate_name="Jug of 1,000 Cups", ultimate_type="Heal", ultimate_description="Rapidly tosses brew to the most injured nearby allies, prioritizing Heroes").save()
    Ultimate(hero_id=Heroes.objects.get(hero_name="Li Li"), ultimate_name="Water Dragon", ultimate_type="Damage", ultimate_description="Summon a Water Dragon that after a delay hits the nearest enemy Hero and all enemies near them").save()
    Ultimate(hero_id=Heroes.objects.get(hero_name="Tracer"), ultimate_name="Pulse Bomb", ultimate_type="Damage", ultimate_description="Fire a bomb that attaches to the first enemy hit, exploding after 2 seconds").save()
    Ultimate(hero_id=Heroes.objects.get(hero_name="Sonya"), ultimate_name="Leap", ultimate_type="Stun", ultimate_description="Leap into the air, dealing 270 (61 + 11 per level) damage to nearby enemies, and stunning them for 1.5 seconds.").save()
    Ultimate(hero_id=Heroes.objects.get(hero_name="Sonya"), ultimate_name="Wrath of the Berzerker", ultimate_type="Damage Boost", ultimate_description="Increase damage dealt by 40%. Reduce the duration of silences, stuns, slows, roots, and polymorphs against you by 50%").save()
    Ultimate(hero_id=Heroes.objects.get(hero_name="Nova"), ultimate_name="Triple Tap", ultimate_type="Damage", ultimate_description="Locks in on the target Hero, then fires 3 shots that hit the first Hero or Structure they come in contact with").save()
    Ultimate(hero_id=Heroes.objects.get(hero_name="Nova"), ultimate_name="Precision Strike", ultimate_type="Damage", ultimate_description="After a 1.5 second delay, deals 1000 (335 + 35 per level) damage to enemies within an area. Unlimited range.").save()
    Ultimate(hero_id=Heroes.objects.get(hero_name="ETC"), ultimate_name="Mosh Pit", ultimate_type="Stun", ultimate_description="After 0.75 seconds, channel to stun nearby enemies for 4 seconds.").save()
    Ultimate(hero_id=Heroes.objects.get(hero_name="ETC"), ultimate_name="Stage Dive", ultimate_type="Slow", ultimate_description="Leap to any location. Deals 340 damage to enemies in the area, slowing them for 3 seconds.").save()
    Ultimate(hero_id=Heroes.objects.get(hero_name="Sylvanas"), ultimate_name="Wailing arrow", ultimate_type="Silence", ultimate_description="Shoot a large arrow that can be detonated to deal damage and silence all enemies hit").save()
    Ultimate(hero_id=Heroes.objects.get(hero_name="Sylvanas"), ultimate_name="Mind Control", ultimate_type="Unit Conversion", ultimate_description="Convert enemy units permanently to your side").save()
    Ultimate(hero_id=Heroes.objects.get(hero_name="Lt. Morales"), ultimate_name="Stim Drone", ultimate_type="Speed Boost", ultimate_description="Grant an allied Hero 75% Attack Speed and 25% Movement Speed for 10 seconds.").save()
    Ultimate(hero_id=Heroes.objects.get(hero_name="Lt. Morales"), ultimate_name="Medivac Dropship", ultimate_type="Global Team Transport", ultimate_description="Target a location for a Medivac transport. For up to 10 seconds before takeoff, allies can right-click to enter the Medivac.").save()
    Ultimate(hero_id=Heroes.objects.get(hero_name="Jaina"), ultimate_name="Ring of Frost", ultimate_type="Damage", ultimate_description="After a 1.5 second delay, create a ring of frost, dealing massive damage and slowing enemies").save()
    Ultimate(hero_id=Heroes.objects.get(hero_name="Jaina"), ultimate_name="Summon Water Elemental", ultimate_type="Summon", ultimate_description="Summon a controllable water elemental to attack and slow your foes").save()


class Migration(migrations.Migration):

    dependencies = [
        ('hots', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(loadData)
    ]