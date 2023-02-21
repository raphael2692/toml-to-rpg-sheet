
import jinja2
from enrich.player import PlayerStats
from _logger import logger
from _parse_inputs import parse_inputs


def build_sheet():
    inputs = parse_inputs()

    template_loader = jinja2.FileSystemLoader(searchpath="templates")
    template_env = jinja2.Environment(loader=template_loader)

    template = template_env.get_template("base.html")

    # compute stats
    player_stats = PlayerStats(inputs["conf"])
    conf = player_stats.make_computations()

    # add markdowns to player conf
    conf.update({"features_and_traits": inputs["features_and_traits"]})
    conf.update(
        {"other_proficiency_languages": inputs["other_proficiency_languages"]})
    conf.update({"equipment": inputs["equipment"]})
    conf.update(
        {"attacks_and_spellcasting": inputs["attacks_and_spellcasting"]})
    conf.update({"inventory": inputs["inventory"]})
    conf.update({"notes": inputs["notes"]})

    template_vars = conf
    output_text = template.render(template_vars)

    with open(f"docs/index.html", "w") as fh:
        fh.write(output_text)


if __name__ == "main":
    build_sheet()
