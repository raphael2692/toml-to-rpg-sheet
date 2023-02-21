import tomli
import jinja2
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from enrich.player import PlayerStats
from _logger import logger
import markdown

with open("inputs/character.toml", mode="rb") as f:
    conf = tomli.load(f)
templateLoader = jinja2.FileSystemLoader(searchpath="templates")
templateEnv = jinja2.Environment(loader=templateLoader)

# sheet building
template = templateEnv.get_template( "base.html" )

# magic happens
player_stats=PlayerStats(conf)
new_conf=player_stats.make_computations()

with open(f"inputs/features_and_traits.md", "r") as f:
    features_and_traits = f.read()

features_and_traits = markdown.markdown(features_and_traits)
new_conf.update({"features_and_traits": features_and_traits})

with open(f"inputs/other_proficiency_languages.md", "r") as f:
    other_proficiency_languages = f.read()

other_proficiency_languages = markdown.markdown(other_proficiency_languages)
new_conf.update({"other_proficiency_languages": other_proficiency_languages})

with open(f"inputs/equipment.md", "r") as f:
    equipment = f.read()

equipment = markdown.markdown(equipment)
new_conf.update({"equipment": equipment})

with open(f"inputs/attacks_and_spellcasting.md", "r") as f:
    attacks_and_spellcasting = f.read()

attacks_and_spellcasting = markdown.markdown(attacks_and_spellcasting)
new_conf.update({"attacks_and_spellcasting": attacks_and_spellcasting})

with open(f"inputs/inventory.md", "r") as f:
    inventory = f.read()

inventory = markdown.markdown(inventory)
new_conf.update({"inventory": inventory})

with open(f"inputs/notes.md", "r") as f:
    notes = f.read()

notes = markdown.markdown(notes)
new_conf.update({"notes": notes})

logger.debug(new_conf)
template_vars = new_conf
output_text = template.render(template_vars)

# to save the results
# char_name = conf["character"]["name"]

with open(f"docs/index.html", "w") as fh:
    fh.write(output_text)
