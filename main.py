from src.speech import text_to_speech, speech_to_text
from src.utils import parse_config

def main():
    config = parse_config()

    h = speech_to_text(lang=config.lang)
    text_to_speech(h, lang=config.lang)

if __name__ == "__main__":
    main()