import tomli

with open("character.toml", mode="rb") as fp:
    conf = tomli.load(fp)


print(conf["character"])