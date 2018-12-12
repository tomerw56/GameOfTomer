
from os import sys,path
sys.path.append((path.dirname(path.abspath(__file__))))


import argparse

from InfraDisplayMode import InfraDisplayMode
from PlaybackMode import PlayBackMode
from InfraPrepMode import InfraPrepMode
from RunGameMode import RunGameMode

#sys.path.append(sys.path[0]+'/Game.Utils/')
#from LoggingHelper import *

def main():
    parser = argparse.ArgumentParser(prog='GameOfTomer')
    subparsers = parser.add_subparsers(help='sub-command help', dest='command')

    parser_pb = subparsers.add_parser('PlayBack', help='PlayBack mode')
    parser_pb.add_argument('playbackfolder', help='playback folder ')

    parser_Infra = subparsers.add_parser('InfraParse', help='InfraParse help')
    parser_Infra.add_argument('sourcefile', help='sources file')
    parser_Infra.add_argument('destfolder', help='destfolder')

    parser_Infra_Display = subparsers.add_parser('InfraDisplay', help='InfraDisplay help')
    parser_Infra_Display.add_argument('mapfilename', help='map file name')
    parser_Infra_Display.add_argument('maximumAllowedPath', help='maximum Allowed Path')

    parser_Infra = subparsers.add_parser('Game', help='Game help')
    parser_Infra.add_argument('botfile', help='bot file list')
    parser_Infra.add_argument('inifile', help='iniFile')
    parser_Infra.add_argument('--gamespercouple', help='how many games are played between a couple',default=4)
    parser_Infra.add_argument('--threads', help='how many threads to use',default=4)

    args = parser.parse_args()
    if args.command.lower()=='PlayBack'.lower():
        playback=PlayBackMode(args.playbackfolder)
        if(playback.valid):
            playback.Play()
        else:
            print ('invalid playback folder')

    if args.command.lower()=='InfraParse'.lower():
        infraprep=InfraPrepMode(args.sourcefile)
        if infraprep.valid:
            infraprep.Prep(args.destfolder)
        else:
            print('failed to prep')

    if args.command.lower()=='InfraDisplay'.lower():
        infradisplay=InfraDisplayMode(args.mapfilename,args.maximumAllowedPath)
        if infradisplay.valid:
            infradisplay.Draw()
        else:
            print('failed to Draw')

    if args.command.lower() == 'Game'.lower():
        rungamemode = RunGameMode(args.botfile, args.inifile,args.gamespercouple,args.threads)
        if rungamemode.valid:
            rungamemode.Run()
        else:
            print('failed to Draw')




if __name__ == "__main__":
    main()

