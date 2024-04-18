import random
from files import ItemLib

itemHistory = []

class Item:
    def __init__(self, minstats, maxstats):
        self.type = None
        self.stats = []
        self.minstats = minstats
        self.maxstats = maxstats
        
    def pickStat(self, statpool): #picks stat from forwarded statpool and pops used stat to avoid duplicates
        stat = []
        rndstat = random.randint(0,len(statpool)-1)
        stat.append(statpool[rndstat][0])
        stat.append(random.randint(statpool[rndstat][1][0],statpool[rndstat][1][1]))
        statpool.pop(rndstat) 
        return stat

    def createStatPool(self): #creates manipulatable pool of stats to work with.
        statpool = []
        for i in range(len(ItemLib.ItemLib.offensive)):
            statpool.append(ItemLib.ItemLib.offensive[i])
        for i in range(len(ItemLib.ItemLib.defensive)):
            statpool.append(ItemLib.ItemLib.defensive[i])
        for i in range(len(ItemLib.ItemLib.attributes)):
            statpool.append(ItemLib.ItemLib.attributes[i])
        return statpool

    def rollItem(self): #Generates the actual item with stats
        self.type = ItemLib.ItemLib.types[random.randint(0,len(ItemLib.ItemLib.types)-1)]
        statamount = random.randint(self.minstats, self.maxstats)
        i = 0
        statpool = self.createStatPool()

        while i < statamount:
            stat = self.pickStat(statpool)

            self.stats.append(stat)
            i += 1

def createItem(minstats, maxstats):
    newitem = Item(minstats, maxstats)
    newitem.rollItem()
    itemHistory.append(newitem)
    if len(itemHistory) > 10:
        itemHistory.pop(0)