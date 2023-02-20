import tomli
import jinja2
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from enrich.player import PlayerStats
from _logger import logger
import markdown

# todo questo main è un casino



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
            print("ok")
            print(features_and_traits)
        features_and_traits = markdown.markdown(features_and_traits)

        new_conf.update({"features_and_traits": features_and_traits})
        logger.debug(new_conf)
        templateVars = new_conf
        outputText = template.render(templateVars)

        # to save the results
        char_name = conf["character"]["name"]
        
        with open(f"out/{char_name} Sheet.html", "w") as fh:
            fh.write(outputText)
        
        


if __name__ == "__main__":
    with open("inputs/character.toml", mode="rb") as f:
        conf = tomli.load(f)
    event_handler = TemplateChangeHandler()
    observer = Observer()
    paths = ["templates", "assets", "inputs"]
    for path in paths: 
        observer.schedule(event_handler, path=path, recursive=True)
    observer.start()
    logger.info("Listening for changes in /templates...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()