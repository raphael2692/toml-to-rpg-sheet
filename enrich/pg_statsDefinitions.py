from enrich.computantions import get_abilityScoresModifiers,get_abilityRef

class Pg_statsClass:
    def __init__(self,conf):
        self.conf= conf
        self.stats =  conf["stats"]
        self.skills =  conf["skills"]["skills_prof"]
        self.savingT =  conf["skills"]["saving_throws_prof"]
        self.proficiency_bonus =  conf["skills"]["proficiency_bonus"]

    def makeComputations(self):
        self.computeModifiers()
        self.compute_skills()
        self.compute_saving_throws()

        return self.conf
    
    def computeModifiers(self):
        statMods = {}

        for statName,value in self.stats.items():
            modifier=get_abilityScoresModifiers(value)
            statMods[statName+"_mod"] = modifier

        self.statMods=statMods
        self.conf["statMods"]=statMods

    def compute_skills(self):
        skillMods = {}

        for skillName,profToken in self.skills.items():
            statName=get_abilityRef(skillName)
            skillMod=self._compute_modifier(statName,profToken)
            skillMods[skillName] = skillMod

        self.skillMods=skillMods
        self.conf["skills"]["skills"]=skillMods

    def compute_saving_throws(self):
        savingMods = {}
        for statName,profToken in self.savingT.items():
            skillMod=self._compute_modifier(statName,profToken)
            savingMods[statName] = skillMod

        self.savingMods=savingMods
        print(savingMods)
        self.conf["skills"]["saving_throws"]=savingMods

    def _compute_modifier(self,name,prof_token):
            modifier = int(self.statMods[ name+"_mod"])
            prof_multiplier=len([char for char in prof_token if char=="*"])            
            prof_modifier=(int(self.proficiency_bonus)*prof_multiplier)
            skill_mod = modifier + prof_modifier
            if skill_mod >=0 : skill_modstr = "+" + str(skill_mod) 
            else: skill_modstr = str(skill_mod) 
            return skill_modstr       
