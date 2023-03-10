import re

def get_ability_scores_modifiers(value):
    mapping = {
    "1": "-5",
    "2":  "-4",
    "3":  "-4",
    "4":  "-3",
    "5" : "-3",
    "6" : "-2",
    "7"	: "-2",
    "8":  "-1",
    "9":  "-1",
    "10":"+0" ,
    "11":"+0",
    "12":"+1",
    "13":"+1",
    "14":"+2",
    "15":"+2",
    "16":"+3",
    "17":"+3",
    "18":"+4",
    "19":"+4",
    "20":"+5",
    "21":"+5",
    "22":"+6",
    "23":"+6",
    "24":"+7",
    "25":"+7",
    "26":"+8",
    "27":"+8",
    "28":"+9",
    "29":"+9",
    "30":"+10"    
    }
    
    mod=mapping[value]
    return mod

def get_ability_ref(ability):
    #statRef = re.search('\((.+)\)', ability).group(1)
    mapping= {
    "Dex" : "dexterity",
    "Wis" :"wisdom",
    "Int":"intelligence",
    "Str":"strength",
    "Cha":"charisma",
    }
    
    abilities=["acrobatics_(Dex)",
    "animal_handling_(Wis)",
    "arcana_(Int)",
    "athletics_(Str)",
    "deception_(Cha)",
    "history_(Int)",
    "insight_(Wis)",
    "intimidation_(Cha)",
    "investigation_(Int)",
    "medicine_(Wis)",
    "nature_(Int)",
    "perception_(Wis)",
    "performance_(Cha)",
    "persuasion_(Cha)",
    "religion_(Int)",
    "sleight_of_hand_(Dex)",
    "stealth_(Dex)",
    "survival_(Wis)"]

    skill_dict={}
    for ability_name in abilities:
        skill_name = re.search('(.+)_\(', ability_name).group(1)
        stat_ref = re.search('\((.+)\)', ability_name).group(1)
        skill_dict[skill_name] = stat_ref

    stat_ref = skill_dict[ability]
    stat_name = mapping[stat_ref]
    return stat_name


def get_proficiency(level):
    from_level_to_prof={
        "1":	"+2",
        "2": "+2",
        "3": "+2",
        "4":	"+2",
        "5":	"+3",
        "6":	"+3",
        "7":	"+3",
        "8":	"+3",
        "9":	"+4",
        "10":	"+4",
        "11":	"+4",
        "12":	"+4",
        "13":	"+5",
        "14":	"+5",
        "15":	"+5",
        "16":	"+5",
        "17":	"+6",
        "18":	"+6",
        "19":	"+6",
        "20":  "+6"}
    
    proficiency_mod = from_level_to_prof[level]
    return proficiency_mod