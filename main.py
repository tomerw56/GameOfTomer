import sys
import os
sys.path.append(sys.path[0]+'/Game.Utils/')
from LoggingHelper import *
def main():
    wrap=loggingHelper()
    print("Hello World!")
    wrap.loginfo("hi")


if __name__ == "__main__":
    main()

