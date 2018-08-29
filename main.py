import sys
import os
import argparse
from PlaybackMode import PlayBackMode
#sys.path.append(sys.path[0]+'/Game.Utils/')
#from LoggingHelper import *

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-pb", "--pb", required=False,
                    help="Play Back Mode please specifay folder")
    ap.add_argument("-prep", "--prep", required=False,
                    help="Play Back Mode")
    args = ap.parse_args()
    if args.pb:
        playback=PlayBackMode(args.pb)
        if(playback.valid):
            playback.Play()
        else:
            print ('invalid playback folder')

    

if __name__ == "__main__":
    main()

