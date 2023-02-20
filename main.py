import tomli
import jinja2
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

with open("character.toml", mode="rb") as fp:
    conf = tomli.load(fp)
    
class TemplateChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # jinja2 setup
        templateLoader = jinja2.FileSystemLoader(searchpath="templates")
        templateEnv = jinja2.Environment(loader=templateLoader)
        print(f'event type: {event.event_type}  path : {event.src_path}')
        # sheet building
        template = templateEnv.get_template( "base.html" )
        
        print(conf)
        
        # magic happens
        templateVars = conf

        outputText = template.render(templateVars)

        # to save the results
        char_name = conf["character"]["name"]
        
        with open(f"out/{char_name} Sheet.html", "w") as fh:
            fh.write(outputText)
        
        


if __name__ == "__main__":
    event_handler = TemplateChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path='templates', recursive=True)
    observer.start()
    print("Listening for changes in /templates...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()