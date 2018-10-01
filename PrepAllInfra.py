from InfraPrepMode import InfraPrepMode
import os

def prepinfra(sourcefile,destfolder):
    infraprep=InfraPrepMode(sourcefile)
    if infraprep.valid:
        infraprep.Prep(destfolder)
    else:
        print('failed to prep'+sourcefile)

def main():

    mainfolder=os.path.dirname(__file__)
    prepinfra(os.path.join(mainfolder, 'Maps/ChallangeMap/Map.csv'), os.path.join(mainfolder, 'Maps/ChallangeMap/'))
    prepinfra(os.path.join(mainfolder, 'Maps/NoControllingPointsMap/Map.csv'), os.path.join(mainfolder, 'Maps/NoControllingPointsMap/'))
    prepinfra(os.path.join(mainfolder, 'Maps/SimpleMovingMap/Map.csv'), os.path.join(mainfolder, 'Maps/SimpleMovingMap/'))
    prepinfra(os.path.join(mainfolder, 'Maps/TestMap/Map.csv'), os.path.join(mainfolder, 'Maps/TestMap/'))
    prepinfra(os.path.join(mainfolder, 'Maps/TestSimpleMap/Map.csv'), os.path.join(mainfolder, 'Maps/TestSimpleMap/'))

if __name__ == "__main__":
    main()