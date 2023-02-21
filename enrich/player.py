from enrich.computations import get_ability_scores_modifiers, get_ability_ref, get_proficiency
from _logger import logger
from exceptions import TooManyStarsException

class PlayerStats:
    def __init__(self,conf):
        self.conf= conf

        self.level =  conf["character"]["level"]

        self.stats =  conf["stats"]
        self.skills =  conf["skills"]["skills_prof"]
        self.savingT =  conf["skills"]["saving_throws_prof"]
        #self.proficiency_bonus =  conf["skills"]["proficiency_bonus"]

    def make_computations(self):
        self._compute_proficiency()
        self._compute_modifiers()
        self._compute_skills()
        self._compute_saving_throws()

        return self.conf

    def _compute_proficiency(self):
        self.proficiency_bonus =  get_proficiency(self.level)
        self.conf["skills"]["proficiency_bonus"] = get_proficiency(self.level)


    def _compute_modifiers(self):
        stat_mods = {}

        for stat_name,value in self.stats.items():
            modifier=get_ability_scores_modifiers(value)
            stat_mods[stat_name+"_mod"] = modifier

        self.stat_mods=stat_mods
        self.conf["stat_mods"]=stat_mods

    def _compute_skills(self):
        skill_mods = {}

        for skill_name,prof_token in self.skills.items():
            stat_name=get_ability_ref(skill_name)
            skill_mod=self._compute_modifier(stat_name,prof_token)
            skill_mods[skill_name] = skill_mod

        self.skill_mods=skill_mods
        self.conf["skills"]["skills"]=skill_mods

    def _compute_saving_throws(self):
        saving_mods = {}
        for stat_name,prof_token in self.savingT.items():
            skill_mod=self._compute_modifier(stat_name,prof_token)
            saving_mods[stat_name] = skill_mod

        self.saving_mods=saving_mods
        logger.debug(saving_mods)
        self.conf["skills"]["saving_throws"]=saving_mods

    def _compute_modifier(self,name,prof_token):
            modifier = int(self.stat_mods[ name+"_mod"])
            prof_multiplier=len([char for char in prof_token if char=="*"])     
            if prof_multiplier > 2:
                raise TooManyStarsException
            prof_modifier=(int(self.proficiency_bonus)*prof_multiplier)
            skill_mod = modifier + prof_modifier
            if skill_mod >=0 : 
                skill_modstr = "+" + str(skill_mod) 
            else: 
                skill_modstr = str(skill_mod) 
            return skill_modstr       
