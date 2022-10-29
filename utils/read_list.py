#!/usr/local/bin/python3.10

class Read_list:
    """returned (passed) parameters"""
    def __init__(self):
        self.msg='OK'
        self.nt4=0
        self.t4=[]
        self.nglm=0
        self.glm=[]
        self.nconc=0
        self.conc=[]    
        self.nimg=0
        self.img=[]
        self.imgt=[]
        self.nev=0
        self.ev=[]
        self.ntxt=0
        self.txt=[]
        self.nidentify=0
        self.identify=[]
        self.nvals=0
        self.vals=[]
        self.next=0
        self.ext=[]
        self.ndtseries=0
        self.dtseries=[]
        self.dtseriest=[]
        self.ndscalar=0
        self.dscalar=[]
        self.dscalart=[]
        self.nnii=0
        self.nii=[]
        self.niit=[]
        self.lcnii=0
        self.nreplace=0
        self.replace=[]
        self.nwmparc=0
        self.wmparc=[]
        self.wmparct=[]

def read_list(glm_list,**kwargs):
    for key,value in kwargs.items():
        if key=='skip':skip=value
    pp=Read_list()

    import pathlib
    path=pathlib.Path(glm_list).parent
    print(f'path={path}')

    with open(glm_list,encoding="utf8",errors='ignore') as f0:
        #while True:
        #    line=f0.readline().rstrip('\t\n\r')
        #    print(f'{line}END')
        #    if not line:break

        for line0 in f0:
            if not line0.strip() or line0.startswith('#'):continue
            print(f'line0={line0}END')
            line1=line0.rstrip('\t\n\r')
            print(f'line1={line1}END')



