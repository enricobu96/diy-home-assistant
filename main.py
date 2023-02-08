from src.speech import text_to_speech, speech_to_text
from src.utils import parse_args, download_model, runcmd

def main():
    args, config = parse_args()

    if args.subcommand == 'download':
        if args.model == 'wee' or args.model == 'homongous':
            download_model(args.model)
            runcmd('echo "Hello, World!"', verbose = True)
            exit()
        else:
            print('Please specify proper model size')
            exit()

    h = speech_to_text(lang=config['lang'])
    text_to_speech(h, lang=config['lang'])

if __name__ == "__main__":
    main()