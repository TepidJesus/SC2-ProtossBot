from sc2.bot_ai import BotAI
from sc2.data import Difficulty, Race
from sc2.main import run_game
from sc2.player import Bot, Computer
from sc2 import maps
from sc2.ids.unit_typeid import UnitTypeId

class Actions:

    def __init__(self) -> None:
        pass

    def skirmish(self):
        pass

    def retreat(self):
        pass

    def last_stand(self):
        pass

    def scout(self):
        pass

    def attack(self):
        pass  

    def defend(self):
        pass

    def take_objective(self):
        pass

    def build(self): ### Commences Next Stage of Build Path
        if self.supply_used == 13:
            

    def drop_pylon(self):
        pass

    def expand(self):
        pass