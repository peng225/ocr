#!/usr/bin/python3

from PIL import Image
import sys

import pyocr
import pyocr.builders

def init(specifiedLang):
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        return None
    # The tools are returned in the recommended order of usage
    tool = tools[0]

    langs = tool.get_available_languages()
    print(f"Available languages: {', '.join(langs)}")
    lang = langs[0]
    if specifiedLang in langs:
        lang = specifiedLang
    else:
        print(
            f"warn: specified language '{specifiedLang}' is not available on this system."
        )
    return tool, lang

def imageToText(tool, imageName, lang):
    return tool.image_to_string(
        Image.open(imageName), lang=lang, builder=pyocr.builders.TextBuilder()
    )

def main():
    if 3 < len(sys.argv):
        print(f"usage {sys.argv[0]} [lang] [imageName]")
        sys.exit(1)

    tool, lang = init(sys.argv[1])
    print(f"Will use tool '{tool.get_name()}'")
    print("Will use lang '%s'" % (lang))
    txt = imageToText(tool, sys.argv[2], lang)
    print(txt)

if __name__ == "__main__":
    main()
