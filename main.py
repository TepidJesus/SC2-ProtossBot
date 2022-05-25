from sc2.bot_ai import BotAI
from sc2.data import Difficulty, Race
from sc2.main import run_game
from sc2.player import Bot, Computer
from sc2 import maps
from sc2.ids.unit_typeid import UnitTypeId
import numpy as np
import cv2
import math
from sc2.position import Point2






class ProBot(BotAI):

    async def build_order(self): ### Commences Next Stage of Build Path
        if self.supply_used < 13:
            if self.can_afford(UnitTypeId.PROBE):
                nex = self.townhalls.first
                nex.train(UnitTypeId.PROBE)
        elif self.supply_used == 13:
            if self.structures(UnitTypeId.PYLON).amount < 1:
                nat = await self.get_next_expansion()
                if self.can_afford(UnitTypeId.PYLON) and not self.already_pending(UnitTypeId.PYLON):
                    await self.build(UnitTypeId.PYLON, near=nat)
        elif self.supply_used == 16:
            self.expand_now()

            
    async def on_step(self, iteration: int):
        await self.distribute_workers()
        
        await self.build_order()


        #### MAPPING ####
        map = np.zeros((self.game_info.map_size[0], self.game_info.map_size[1], 3), dtype=np.uint8)
        for mineral in self.mineral_field:
            pos = mineral.position
            c = [175, 255, 255]
            fraction = mineral.mineral_contents / 1800
            if mineral.is_visible:
                map[math.ceil(pos.y)][math.ceil(pos.x)] = [int(fraction*i) for i in c] 
            else:
                map[math.ceil(pos.y)][math.ceil(pos.x)] = [20, 75, 50]  

        for enemy_start_location in self.enemy_start_locations:
            pos = enemy_start_location
            c = [0, 0, 255]
            map[math.ceil(pos.y)][math.ceil(pos.x)] = c

        for friendly_structure in self.structures:
            pos = friendly_structure.position
            for x in range(math.floor(-friendly_structure.sight_range), math.ceil(friendly_structure.sight_range) + 1):
                    for y in range(math.floor(-friendly_structure.sight_range), math.ceil(friendly_structure.sight_range) + 1):
                        if self.is_visible(Point2([pos.x + x,pos.y + y])) and (map[math.ceil(pos.y + y)][math.ceil(pos.x + x)]).tolist() == [0, 0, 0]:
                            c1 = [100, 100, 100]
                            map[math.ceil(pos.y + y)][math.ceil(pos.x + x)] = c1
            if friendly_structure.type_id == UnitTypeId.NEXUS:
                c = [255, 255, 175]
                fraction = friendly_structure.health / friendly_structure.health_max if friendly_structure.health_max > 0 else 0.0001
                map[math.ceil(pos.y)][math.ceil(pos.x)] = [int(fraction*i) for i in c]
            
            else:
                c = [0, 255, 175]
                fraction = friendly_structure.health / friendly_structure.health_max if friendly_structure.health_max > 0 else 0.0001
                map[math.ceil(pos.y)][math.ceil(pos.x)] = [int(fraction*i) for i in c]

        for enemy_unit in self.enemy_units:
            pos = enemy_unit.position
            c = [100, 0, 255]
            fraction = enemy_unit.health / enemy_unit.health_max if enemy_unit.health_max > 0 else 0.0001
            map[math.ceil(pos.y)][math.ceil(pos.x)] = [int(fraction*i) for i in c]


        for enemy_structure in self.enemy_structures:
            pos = enemy_structure.position
            c = [0, 100, 255]
            fraction = enemy_structure.health / enemy_structure.health_max if enemy_structure.health_max > 0 else 0.0001
            map[math.ceil(pos.y)][math.ceil(pos.x)] = [int(fraction*i) for i in c]

        for vespene in self.vespene_geyser:
            pos = vespene.position
            c = [255, 175, 255]
            fraction = vespene.vespene_contents / 2250

            if vespene.is_visible:
                map[math.ceil(pos.y)][math.ceil(pos.x)] = [int(fraction*i) for i in c]
            else:
                map[math.ceil(pos.y)][math.ceil(pos.x)] = [50,20,75]

        for friendly_unit in self.units:
            pos = friendly_unit.position
            for x in range(math.floor(-friendly_structure.sight_range), math.ceil(friendly_structure.sight_range) + 1):
                    for y in range(math.floor(-friendly_structure.sight_range), math.ceil(friendly_structure.sight_range) + 1):
                        if self.is_visible(Point2([pos.x + x,pos.y + y])) and (map[math.ceil(pos.y + y)][math.ceil(pos.x + x)]).tolist() == [0, 0, 0]:
                            c1 = [100, 100, 100]
                            map[math.ceil(pos.y + y)][math.ceil(pos.x + x)] = c1
            c = [175, 255, 0]
            fraction = friendly_unit.health / friendly_unit.health_max if friendly_unit.health_max > 0 else 0.0001
            map[math.ceil(pos.y)][math.ceil(pos.x)] = [int(fraction*i) for i in c]

        cv2.imshow('map', cv2.flip(cv2.resize(map, None, fx=4, fy=4, interpolation=cv2.INTER_NEAREST), 0))
        cv2.waitKey(1)

run_game(maps.get("AcropolisLE"),[Bot(Race.Protoss, ProBot()), Computer(Race.Zerg, Difficulty.Hard)], realtime=False)