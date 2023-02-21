import tomli
from _logger import logger
import markdown
    
def parse_inputs():
    inputs = {}
    
    with open("inputs/character.toml", mode="rb") as f:
        logger.info("Reading player configuration .toml as conf")
        inputs["conf"] = tomli.load(f)

    with open(f"inputs/features_and_traits.md", "r") as f:
        logger.info("Reading player features and traits .md as features_and_traits")
        inputs["features_and_traits"] = markdown.markdown(f.read())
        
    with open(f"inputs/other_proficiency_languages.md", "r") as f:
        logger.info("Reading player other proficiency and languages .md as other_proficiency_languages")
        inputs["other_proficiency_languages"] = markdown.markdown(f.read())

    with open(f"inputs/attacks_and_spellcasting.md", "r") as f:
        logger.info("Reading player attacks and spellcasting .md as attacks_and_spellcasting")
        inputs["attacks_and_spellcasting"] = markdown.markdown(f.read())
        
    with open(f"inputs/equipment.md", "r") as f:
        logger.info("Reading player equipment .md as equipment")
        inputs["equipment"] = markdown.markdown(f.read())
    
    with open(f"inputs/inventory.md", "r") as f:
        logger.info("Reading player inventory .md as inventory")
        inputs["inventory"] = markdown.markdown(f.read())
        
    with open(f"inputs/notes.md", "r") as f:
        logger.info("Reading player notes .md as notes")
        inputs["notes"] = markdown.markdown(f.read())

    logger.debug(inputs)
    
    return inputs
