#CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO    FORMAT  unknown
#chr10_114724268_Control_Consensus       201     .       GCAAG   GG      21.0076 .       AB=0.4;ABP=3.44459;AC=1;AF=0.5;AN=2;AO=2;CIGAR=1M3D1M;DP=5;DPB=3.8;DPRA=0;EP     P=7.35324;EPPR=9.52472;GTI=0;LEN=3;MEANALT=1;MQM=60;MQMR=60;NS=1;NUMALT=1;ODDS=4.82921;PAIRED=0;PAIREDR=0;PAO=0;PQA=0;PQR=0;PRO=0;QA=76;QR=117;RO=3;RPL=2;RPP=7.3532     4;RPPR=9.52472;RPR=0;RUN=1;SAF=2;SAP=7.35324;SAR=0;SRF=3;SRP=9.52472;SRR=0;TYPE=del     GT:DP:DPR:RO:QR:AO:QA:GL        0/1:5:5,2:3:117:2:76:-5.70966,0,-9.40523
def INFO_parser(line):
    INFO = {}
    for item in str(line).split(';'):
    	INFO[str(item.split('=')[0])] = str(item.split('=')[1])
    return INFO

def vcf_parser(DictReader_line):
    DictReader_line['INFO'] = INFO_parser([str(DictReader_line['INFO'])])
    return DictReader_line 

