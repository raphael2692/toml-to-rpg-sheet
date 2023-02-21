import tomli
import jinja2
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from enrich.player import PlayerStats
from _logger import logger
from build import build_sheet

class TemplateChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        logger.info(f'event type: {event.event_type}  path : {event.src_path}')
        build_sheet()
        


if __name__ == "__main__":
    
    event_handler = TemplateChangeHandler()
    observer = Observer()
    paths = ["templates", "inputs"]
    for path in paths: 
        observer.schedule(event_handler, path=path, recursive=True)
   
    observer.start()
    logger.info("Listening for changes...")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()