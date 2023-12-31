#!/usr/bin/env python3

def main():
    ## create file object in "r"ead mode
    configfile = open("vlanconfig.cfg", "r")

    ## display file to the screen - .read()
    configblog = configfile.read()

    ## break configblog across line boundaries (strips out \n)
    configlist = configblog.splitlines()

    ## display list wit no "\n"
    print(configlist)

    ## Always close your file
    configfile.close()

if __name__ == "__main__":
    main()
