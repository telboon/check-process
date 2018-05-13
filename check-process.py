#!/usr/bin/python3

import os
import sys
import datetime
import subprocess

def main():
    seconds=10

    if len(sys.argv)==1:
        print("Running "+sys.argv[0]+" for 10 seconds")
        print("Usage:")
        print(sys.argv[0]+" <seconds>")

    elif len(sys.argv)==2:
        seconds=int(sys.argv[1])

    elif len(sys.argv)>2:
        print("Wrong usage")
        print("Usage:")
        print(sys.argv[0]+" <seconds>")
        sys.exit(0)

    #start doing work
    startTime=datetime.datetime.now()


    while datetime.datetime.now()-startTime < datetime.timedelta(0,seconds):
        oldProcs=[]
        newProcs=[]

        #old
        checkProc = subprocess.Popen(["/bin/bash", "-c", "ps -eF | awk '{print $2}'"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        for line in checkProc.stdout:
            oldProcs.append(line[:-1].decode("utf8"))

        #new
        checkProc = subprocess.Popen(["/bin/bash", "-c", "ps -eF | awk '{print $2}'"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        for line in checkProc.stdout:
            newProcs.append(line[:-1].decode("utf8"))

        #check diff
        for i in newProcs:
            if not(i in oldProcs):
                sys.stdout.write("New: ")
                sys.stdout.flush()
                checkProc = subprocess.Popen(["/bin/bash", "-c", "ps -eF | grep "+i], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                for line in checkProc.stdout:
                    print(line[:-1].decode("utf8"))

        for i in oldProcs:
            if not(i in newProcs):
                sys.stdout.write("Died: ")
                sys.stdout.flush()
                checkProc = subprocess.Popen(["/bin/bash", "-c", "ps -eF | grep "+i], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                for line in checkProc.stdout:
                    print(line[:-1].decode("utf8"))

if __name__ == "__main__":
    main()
