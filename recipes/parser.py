#!/usr/bin/env python

import yaml
import sys
import pprint

if __name__ == '__main__':
    pp = pprint.PrettyPrinter(indent=4, width=80)
    print(sys.argv[1])
    stream = open(sys.argv[1], 'r')
    dictionary = yaml.load(stream, Loader=yaml.SafeLoader)
    pp.pprint(dictionary)
    #for key, value in dictionary.items():
    #    pp.print (key + " : " + str(value))
