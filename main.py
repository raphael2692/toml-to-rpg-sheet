import tomli
import jinja2

with open("character.toml", mode="rb") as fp:
    conf = tomli.load(fp)


# jinja2 setup
templateLoader = jinja2.FileSystemLoader(searchpath="templates")
templateEnv = jinja2.Environment(loader=templateLoader)

# sheet building
template = templateEnv.get_template( "base.html" )
# magic happens
templateVars = conf

outputText = template.render(templateVars)

# print(outputText)

# to save the results
char_name = conf["character"]["name"]
with open(f"out/{char_name} Sheet.html", "w") as fh:
    fh.write(outputText)