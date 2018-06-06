import Vexseq, csv

hg19 = '/home/CAM/adamson/Refs/hg19/GRCh37.p13.genome.fa' 
min_ = str(13489316-75)
max_ = str(13489319+75)
bedcoors = "chr10 " + min_ + ' ' + max_
ref_seq = Vexseq.get_sequence(hg19, bedcoors, '+')

#chr10  13489246    13489247    T   C
a=open('test.bed', 'r')
reader = csv.reader(a, delimiter ='\t')
#defsubstitute_variant(sequence_reference, var_loc, var_ref, var_alt):
for line in reader:
    print line
    print Vexseq.substitute_variant(ref_seq, line[1], line[3], line[4])
a.close()
