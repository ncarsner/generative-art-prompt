import random
import component_words as words


def generate_prompt_simple():
    component_lists = {
        "Color Palettes": words.color_palettes, # black and white, multicolor, pastel
        "Artistic Styles": words.artistic_styles, # art deco, futurist
        "Mediums": words.mediums, # watercolor, acrylic
        "Subject": words.subjects,
        "Shape": words.subjects,
    }

    # entry_quantifier = "a single portrait orientation image of "
    # exit_qualifier = " at 300 DPI with a transparent background"
    components = []

    for label, comp_list in component_lists.items():
        if random.choice([True, True, True, False]):
            choice = random.choice(comp_list)
            component = {
                "Color Palettes": f"{choice},",
                "Artistic Styles": f"{choice},",
                "Mediums": f"{choice},",
                "Subject": f"{choice}",
                "Shape": f"as a {choice}",
            }.get(label, "")
            components.append(component)

    # return entry_quantifier + " ".join(components) + exit_qualifier if components else "No components selected."
    # return entry_quantifier + " ".join(components) if components else "No components selected."
    return " ".join(components) + ", vertical aspect ratio" if components else "No components selected."

if __name__ == "__main__":
    for _ in range(10):
        print(generate_prompt_simple())
