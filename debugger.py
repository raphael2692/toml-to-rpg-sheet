import tomli
import jinja2
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from enrich.pg_statsDefinitions import Pg_statsClass
from _logger import logger


with open("character.toml", mode="rb") as fp:
    conf = tomli.load(fp)
    

# jinja2 setup
templateLoader = jinja2.FileSystemLoader(searchpath="templates")
templateEnv = jinja2.Environment(loader=templateLoader)

# sheet building
template = templateEnv.get_template( "base.html" )

# magic happens
pg_statsClass=Pg_statsClass(conf)
newConf=pg_statsClass.makeComputations()


templateVars = newConf
outputText = template.render(templateVars)

newConf["skills"]
# to save the results
char_name = conf["character"]["name"]

with open(f"out/{char_name} Sheet.html", "w") as fh:
    fh.write(outputText)

        