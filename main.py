#!/usr/local/bin/python3.10

list="/mnt/c/Users/mcavoylocal/nillap71/zacks/fidlpy/old_wo35847.list"
print(f'here-1={list}')
#
#import utils.read_list
#
#utils.read_list.read_list(list)



text='Learning how to create to package. List -l|--list.'
print(text)
import argparse
parser=argparse.ArgumentParser(description=text,formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-l','--list',action='append',nargs='+',help='Input list(s).')
args=parser.parse_args()
if args.list:
    print(f'-l --list {args.list}')
else:
    exit()

list=args.list
print(f'here0={args.list}')

import utils.read_list

for i in args.list:
    print(f'i={i}')
    print(f'i[0]={i[0]}')
    #utils.read_list.read_list(i[0])
    for j in range(len(i)):
        utils.read_list.read_list(i[j])
