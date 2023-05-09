#!/usr/bin/env python3

#text='Convert *scanlist.csv to *.dat. Multiple *scanlist.csv for a single subject are ok. Each subject is demarcated by -s|--sub.'
text='Convert *EV.txt to fidl event file. Multiple *EV.txt are combined to a single fidl event file. Multiple runs are accepted.'

#print(text)

import argparse
parser=argparse.ArgumentParser(description=text,formatter_class=argparse.RawTextHelpFormatter)

#parser.add_argument('-s','--sub',action='append',nargs='+',help='Input scanlist.csv(s). Each subject is written to its own file (eg 10_1002.dat and 10_2002.dat). Ex. -s 10_1002_scanlist.csv -s 10_2002a_scanlist.csv 10_2002b_scanlist.csv')
#parser.add_argument('-e','--EV',action='append',nargs='+',help='Input FSL event files. Each invocation of this option designates the event files for a single run.\nEx. -e EV_Easy_10_2000_LH1_EV.txt EV_Hard_10_2000_LH1_EV.txt -e EV_Easy_10_2000_LH2_EV.txt EV_Hard_10_2000_LH2_EV.txt')
#parser.add_argument('-b','--bold',action='append',nargs='+',help='BOLD time series. The number of BOLDs must equal the number of -e/--EV options.\nEx. -b run1_LH.nii.gz run2_LH.nii.gz')
#START230401
parser.add_argument('-e','--ev','-ev','-EV','--EV',action='append',nargs='+',help='Input FSL event files. Each invocation of this option designates the event files for a single run.\nEx. -e EV_Easy_10_2000_LH1_EV.txt EV_Hard_10_2000_LH1_EV.txt -e EV_Easy_10_2000_LH2_EV.txt EV_Hard_10_2000_LH2_EV.txt')
#parser.add_argument('-b','--bold','-bold','-BOLD','--BOLD',action='append',nargs='+',help='BOLD time series. The number of BOLDs must equal the number of -e options.\nEx. -b run1_LH.nii.gz run2_LH.nii.gz or -b run1_LH.nii.gz -b run2_LH.nii.gz')
parser.add_argument('-b','--bold','-bold','-BOLD','--BOLD',action='extend',nargs='+',help='BOLD time series. The number of BOLDs must equal the number of -e options.\nEx. -b run1_LH.nii.gz run2_LH.nii.gz or -b run1_LH.nii.gz -b run2_LH.nii.gz')

#START230402
parser.add_argument('-o','--out','-out','-OUT','--OUT',help='Name of fidl output file.')

##EV_Easy_10_2000_LH1_EV.txt  EV_Easy_10_2000_RH1_EV.txt  EV_Hard_10_2000_LH1_EV.txt  EV_Hard_10_2000_RH1_EV.txt
##EV_Easy_10_2000_LH2_EV.txt  EV_Easy_10_2000_RH2_EV.txt  EV_Hard_10_2000_LH2_EV.txt  EV_Hard_10_2000_RH2_EV.txt
##EV_Easy_10_2000_LH3_EV.txt  EV_Easy_10_2000_RH3_EV.txt  EV_Hard_10_2000_LH3_EV.txt  EV_Hard_10_2000_RH3_EV.txt


#parser.add_argument('-a','--all',help='Write all subjects to a single file. Individual files are still written.')
#parser.add_argument('-o','--out',help='Write all subjects to a single file. Individual files are not written.')
args=parser.parse_args()

#print(f'args={args}')
#exit()

#if args.sub:
#    print(f'-s --sub {args.sub}')
#    #if args.all: print(f'-a --all {args.all}')
#    print(f'args.all={args.all}')
#    if args.out: print(f'-o --out {args.out}')
#    print(f'args.out={args.out}')
#else:
#    exit()
#START230401
#if not args.ev or not args.bold:
#if args.ev & args.bold:
#    print(f'ev={args.ev}')
#    print(f'bold={args.bold}')
#else:
#    exit()
if not args.ev:
    print('Missing FSL event file(s).')
    exit()
if not args.bold:
    print('Missing bold run(s).')
    exit()

#print(f'len(args.ev)={len(args.ev)}')
#print(f'len(args.bold)={len(args.bold)}')

if len(args.ev)!=len(args.bold):
    print(f'You have specified {len(args.ev)} -e option(s) and {len(args.bold)} bolds. Must be equal! Abort!')
    exit()

#START230402
if not args.out:
    print('Missing name of fidl output file. Abort!')
    exit()

#import subprocess

#for i in args.ev:
#    print(f'i={i}') 
#    for j in range(len(i)):

import pathlib
import subprocess

p0=pathlib.Path(args.out).parent
print(f'p0={p0}')
p0.mkdir(parents=True,exist_ok=True)

with open(args.out,mode='wt',encoding="utf8") as o0:
    for i in range(len(args.ev)):
        print(f'i={i}') 
        #b0=subprocess.run("fslinfo "+args.bold[i]+"| grep dim4",capture_output=True,shell=True)
        b0=subprocess.run("fslinfo "+args.bold[i]+"| grep dim4",capture_output=True,shell=True,text=True,encoding='utf-8')
        #print(f'b0.stdout={b0.stdout}')
        #print(f'len(b0.stdout)={len(b0.stdout)}')
        #print(f'b0={b0}')

        #b1=b0.stdout.splitlines()
        #print(f'b1={b1}')
        #print(f'len(b1)={len(b1)}')

        #b1=(b0.stdout.splitlines()[0]).split()
        #print(f'b1={b1}')
        #print(f'len(b1)={len(b1)}')

        #for j in b0.stdout.splitlines():
        #    print(f'j={j}')
        #    print(f'len(j)={len(j)}')

        #b1=b0.stdout.splitlines()
        #for j in b1:
        #    print(f'j={j}')
        #    print(f'len(j)={len(j)}')

        for j in b0.stdout.splitlines():
            b1=j.split()
            #print(f'b1={b1}')
            #print(f'len(b1)={len(b1)}')

            match b1[0]:
                case 'dim4':
                    dim4=b1[1]
                case 'pixdim4':
                    pixdim4=b1[1]
                case other:
                    print(f'No match found for {b1[0]}')
                    exit()
        print(f'dim4={dim4} pixdim4={pixdim4}') 

        #STARTHERE

exit()

#https://docs.python.org/3/library/subprocess.html
#https://stackoverflow.com/questions/72163312/python-run-shell-command-get-stdout-and-stderr-as-a-variable-but-hide-from-u









import re
import pathlib
import csv

str0='#Scans can be labeled NONE or NOTUSEABLE. Lines beginning with a # are ignored.\n'
str1='#SUBNAME OUTDIR T1 T2 FM1 FM2 run1_LH_SBRef run1_LH run1_RH_SBRef run1_RH run2_LH_SBRef run2_LH run2_RH_SBRef run2_RH run3_LH_SBRef run3_LH run3_RH_SBRef run3_RH rest01_SBRef rest01 rest02_SBRef rest02 rest03_SBRef rest03\n'
str2='#----------------------------------------------------------------------------------------------------------------------------------------------\n'

if args.all or args.out:
    if args.all:
        str3=args.all
    elif args.out:
        str3=args.out
    f2=open(str3,mode='wt',encoding="utf8")
    f2.write(str0+str1+str2)


for i in args.sub:
    #print(f'i={i}') 

    d0={"SUBNAME":"NONE",
        "OUTDIR":"NONE",
        "t1_mpr_1mm_p2_pos50":"NONE",
        "t2_spc_sag_p2_iso_1.0":"NONE",
        "SpinEchoFieldMap2_AP":"NONE",
        "SpinEchoFieldMap2_PA":"NONE",
        "run1_LH_SBRef":"NONE",
        "run1_LH":"NONE",
        "run1_RH_SBRef":"NONE",
        "run1_RH":"NONE",
        "run2_LH_SBRef":"NONE",
        "run2_LH":"NONE",
        "run2_RH_SBRef":"NONE",
        "run2_RH":"NONE",
        "run3_LH_SBRef":"NONE",
        "run3_LH":"NONE",
        "run3_RH_SBRef":"NONE",
        "run3_RH":"NONE",
        "rest01_SBRef":"NONE",
        "rest01":"NONE",
        "rest02_SBRef":"NONE",
        "rest02":"NONE",
        "rest03_SBRef":"NONE",
        "rest03":"NONE"}

   
    n0=pathlib.Path(i[0]).stem
    #print(f'here0 n0={n0}')

    #m=re.match('([0-9_]+?)[a-zA-Z]_scanlist|([0-9_]+?)[a-zA-Z]',n0)
    m=re.match('([0-9_]+?)[a-zA-Z]_scanlist|([0-9_]+?)_scanlist|([0-9_]+?)[a-zA-Z]',n0)

    if m is not None: n0=m[m.lastindex]
    subname=n0
    ext='.dat'
    if pathlib.Path(i[0]).suffix=='.dat':ext+=ext
    n0=pathlib.Path(i[0]).with_name(n0+ext)
    #print(f'here1 n0={n0}')
    p0=pathlib.Path(i[0]).parent
    #print(f'here2 p0={p0}')

    d0['SUBNAME']=subname
    d0['OUTDIR']=str(p0)+'/pipeline'

    for j in range(len(i)):
        with open(i[j],encoding="utf8",errors='ignore') as f1:
            csv1=csv.DictReader(f1)
            for row in csv1:

                #START220805
                if row['Scan'].casefold()=='none'.casefold():continue

                for k in d0:
                    if k==row['nii']:
                        d0[k]=str(p0)+'/nifti/'+k+'.nii.gz'
                        break


    if args.out is None:
        with open(n0,mode='wt',encoding="utf8") as f0:
            f0.write(str0+str1+str2)
            f0.write(' '.join(d0.values()))
            f0.write('\n')
        print(f'Output written to {n0}')

    if args.all or args.out:
        f2.write(' '.join(d0.values()))
        f2.write('\n')

if args.all or args.out:
    f2.close() 
    print(f'Output written to {str3}')
