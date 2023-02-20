from enrich.computantions import get_abilityScoresModifiers

class Pg_statsClass:
    def __init__(self,conf):
        self.conf= conf
        self.stats =  conf["stats"]
    
    def makeComputations(self):
        self.computeModifiers()
        return self.conf
    
    def computeModifiers(self):
        statMods = {}

        for statName,value in self.stats.items():
            modifier=get_abilityScoresModifiers(value)
            statMods[statName+"_mod"] = modifier

        self.statMods=statMods
        self.conf["statMods"]=statMods
        
