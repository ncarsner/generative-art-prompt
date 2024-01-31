import random
import component_words as words


def generate_prompt():
    component_lists = {
        "Artistic Styles": words.artistic_styles,
        "Color Palettes": words.color_palettes,
        "Emotions": words.emotions,
        "Geographical Locations": words.geographical_locations,
        "Historical References": words.historical_references,
        "Interactions": words.interactions,
        "Mediums": words.mediums,
        "Perspectives": words.perspectives,
        "Rendering Styles": words.rendering_styles,
        "Subjects": words.subjects,
        "Textures": words.textures,
        "Time of Day": words.time_of_day,
        "Weather Conditions": words.weather_conditions,
    }

    entry_quantifier = "a single portrait orientation image of "
    exit_qualifier = " at 300 DPI with a transparent background"
    components = []

    for label, comp_list in component_lists.items():
        if random.choice([True, False]):
            choice = random.choice(comp_list)
            component = {
                "Emotions": f"{choice}",
                "Artistic Styles": f"{choice} depiction",
                "Subjects": f"of {choice}",
                "Mediums": f"in {choice}",
                "Color Palettes": f"using {choice}",
                "Rendering Styles": f"with {choice} rendering style",
                "Time of Day": f"at {choice}",
                "Weather Conditions": f"in {choice} weather",
                "Geographical Locations": f"in {choice} environment",
                "Historical References": f"in {choice} setting",
                "Interactions": f"{choice}",
                "Textures": f"with {choice} textures",
                "Perspectives": f"from {choice} perspective",
            }.get(label, "")
            components.append(component)

    # return entry_quantifier + " ".join(components) + exit_qualifier if components else "No components selected."
    return entry_quantifier + " ".join(components) if components else "No components selected."

if __name__ == "__main__":
    print(generate_prompt())
