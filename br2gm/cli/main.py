#!/usr/bin/env python

from __future__ import print_function
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter

from br2gm.parser import Parser
from br2gm.playlist import Playlist

from br2gm.constants import DEFAULT_CREDS

def bbcr1(args):
    parser = Parser(args.URL)
    playlist = Playlist(**vars(args))
    playlist.create(parser.getSongsList())

class CLI():
    def __init__(self):
        self.parser = ArgumentParser(description='A simple tool to parse BBC Radio 1 Chart and create a Google Music Playlist from it.', formatter_class=RawDescriptionHelpFormatter)

    def set_arguments(self):
        self.parser.add_argument("--dry-run", dest="dryrun", default=False, action="store_true",  help="Don't change anything, just output")
        self.parser.add_argument("-l", "--credentials", dest="credentials", default=DEFAULT_CREDS,
                help="Path to a file containing credentials for Google Music account")
        self.parser.add_argument("-u", "--user", dest="user", default=None,
                help="User name you want to use to login to the Google Music account")
        self.parser.add_argument("URL", help="URL of BBC Radio 1 chart website")
        self.parser.set_defaults(func=bbcr1)

    def run(self):
        self.set_arguments()
        args = self.parser.parse_args()
#        if args.verbose:
#            set_logging(level=logging.DEBUG)
#        elif args.quiet:
#            set_logging(level=logging.WARNING)
#        else:
#            set_logging(level=logging.INFO)
        try:
            args.func(args)
        except AttributeError:
            if hasattr(args, 'func'):
                raise
            else:
                self.parser.print_help()
        except KeyboardInterrupt:
            pass
        except Exception as ex:
            if True or args.verbose:
                raise
            else:
                logger.error("Exception caught: %s", repr(ex))   



def main():
    cli = CLI()
    cli.run()

if __name__ == '__main__':
    main()

