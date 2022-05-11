from sc2.bot_ai import BotAI
from sc2.data import Difficulty, Race
from sc2.main import run_game
from sc2.player import Bot, Computer
from sc2 import maps
from sc2.ids.unit_typeid import UnitTypeId

class ProBot(BotAI):
    async def on_step(self, iteration: int):
        if self.townhalls.amount == 0 and self.can_afford(UnitTypeId.NEXUS) :
            self.expand_now()

run_game(maps.get("AcropolisLE"),[Bot(Race.Protoss, ProBot()), Computer(Race.Zerg, Difficulty.Hard)], realtime=False)