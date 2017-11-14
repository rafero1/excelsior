from logbox import Message
import random


class Fighter:
    """
    fighter module for entities. Allows fighting.
    """
    def __init__(self, hp, sp, atk, df, spd, skills=None):
        self.max_hp = hp
        self.hp = hp
        self.max_sp = sp
        self.sp = sp
        self.atk = atk
        self.df = df
        self.spd = spd
        self.skills = skills

    def attack(self, target, skill):
        result = []
        damage = max(0, skill.dmg + int(self.atk*0.5) * int(self.spd * 0.3) - target.fighter.df + random.randint(-5,+5))
        kwargs = { 'actor': self.owner.name.capitalize(), 'target': target.name, 'amount': str(damage) }

        if damage > 0:
            result.append({
                'message': Message(skill.message.format(**kwargs))
                })

            result.extend(target.fighter.take_hit(damage))
        else:
            result.append({'message': Message('{0} tries to attack {1} but the damage is mitigated'.format(self.owner.name.capitalize(), target.name))})
        skill.timeout = 0
        return result

    def take_hit(self, value):
        result = []
        self.hp -= value
        if self.hp <= 0:
            result.append({'dead': self.owner})
        return result
