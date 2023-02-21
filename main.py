import tomli
import jinja2
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from enrich.player import PlayerStats
from _logger import logger
import markdown

# TODO remove duplicated code, separate handlers, set reading files outside handlers



class TemplateChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # jinja2 setup
        templateLoader = jinja2.FileSystemLoader(searchpath="templates")
        templateEnv = jinja2.Environment(loader=templateLoader)
        logger.info(f'event type: {event.event_type}  path : {event.src_path}')
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

        logger.debug(new_conf)
        template_vars = new_conf
        output_text = template.render(template_vars)

        # to save the results
        # char_name = conf["character"]["name"]
        
        with open(f"docs/index.html", "w") as fh:
            fh.write(output_text)
        
        


if __name__ == "__main__":
    with open("inputs/character.toml", mode="rb") as f:
        conf = tomli.load(f)
    event_handler = TemplateChangeHandler()
    observer = Observer()
    paths = ["templates", "inputs"]
    for path in paths: 
        observer.schedule(event_handler, path=path, recursive=True)
    observer.start()
    logger.info("Listening for changes in /templates, /inputs ...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()