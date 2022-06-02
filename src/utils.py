from defs import *

from subcontrollers.structure.spawner import Spawner
from subcontrollers.creep.starter import Starter

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')


def get_spawners():
    spawns = []
    for spawn_name in Object.keys(Game.spawns):
        spawns.append(Spawner(spawn_name))
    return spawns


def get_creeps():
    creeps = []
    for creep in Object.keys(Game.creeps):
        prefix = creep.split('_')[0]
        if prefix == 'Starter':
            creeps.append(Starter(creep))
    return creeps


def get_creeps_of_role(role):
    creeps = []
    for creep in Object.keys(Game.creeps):
        prefix = creep.split('_')[0]
        if prefix == role.__name__:
            creeps.append(role(creep))
    return creeps