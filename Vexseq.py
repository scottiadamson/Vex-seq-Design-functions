import pybedtools

def get_sequence(reference_fasta, coordinates, strand):
    """Takes coordinates and returns sequence
    bed_coor is space separated"""
    bed_coor = pybedtools.BedTool(coordinates, from_string=True)
    fasta = pybedtools.example_filename(reference_fasta)
    seq = bed_coor.sequence(fi=fasta)
    seq_str = open(seq.seqfn, 'r').read()
    pybedtools.cleanup(remove_all=True)
    return seq_str.replace('>', '').split('\n')[0:-1]
    #['chr10:13489241-13489394', 'AAAATGTAAATGCGTTTTATTTACCTGTTGGTGGTAGAGCAATGCCGTCCAGTCTTTCATCACTGTCCGCGATCTCTGCTGGTTACAAACATAAGACACAAATCTCATTAGTTCCAGGGAGCACATTCATTTTACAGAAAATAGTGATGTAAT']

def substitute_variant(sequence_reference, var_loc, var_ref, var_alt):
    ref_bounds = sequence_reference[0] 
    ref_lower = int(ref_bounds.split(':')[1].split('-')[0])+1
    seq = sequence_reference[1]
    ref_var_len = len(var_ref)
    rel_pos = int(var_loc) - ref_lower
    ref = seq[rel_pos:rel_pos + ref_var_len]
    new_seq = list(seq)
    if len(var_ref) ==1:
        new_seq[rel_pos] = var_alt
    else:
        for i in range(rel_pos, rel_pos + ref_var_len):
            new_seq.pop(rel_pos)
        new_seq.insert(rel_pos, var_alt)
    return ''.join(new_seq)

def rev_comp(string):
    comp = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'U': 'A', 'a' : 't', 'c': 'g', 'g': 'c', 't' : 'a', 'u': 'a', 'N': 'N', 'n':'n'}
    new_seq = []
    for item in list(string):
        new_seq.append(comp(item))
    return ''.join(string)[::-1]

def comp(string):
    comp = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'U': 'A', 'a' : 't', 'c': 'g', 'g': 'c', 't' : 'a', 'u': 'a','N': 'N', 'n':'n'}
    new_seq = []
    for item in list(string):
        new_seq.append(comp(item))
    return ''.join(string)
