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
    ref_bounds, seq = sequence_reference
    _, lower = ref_bounds.split(':')
    ref_lower = int(next(iter(lower.split('-'))))
    rel_pos = int(var_loc) - ref_lower - 1
    new_seq = seq[:rel_pos] + var_alt + seq[rel_pos + len(var_ref):]
    return ''.join(new_seq)

def rev_comp(string):
    comp = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'U': 'A', 'a' : 't', 'c': 'g', 'g': 'c', 't' : 'a', 'u': 'a', 'N': 'N', 'n':'n'}
    new_seq = []
    for item in list(string):
        new_seq.append(comp(item))
    return ''.join(new_seq)[::-1]

def comp(string):
    comp = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'U': 'A', 'a' : 't', 'c': 'g', 'g': 'c', 't' : 'a', 'u': 'a','N': 'N', 'n':'n'}
    new_seq = []
    for item in list(string):
        new_seq.append(comp(item))
    return ''.join(new_seq)
