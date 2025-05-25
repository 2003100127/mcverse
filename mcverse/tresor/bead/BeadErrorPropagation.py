import tresor as ts

ts.locus.simu_generic(
    # initial sequence generation
    len_params={
        'umi': {
            'umi_unit_pattern': 1,
            'umi_unit_len': 12,
        },
        'seq': 100,
    },
    seq_params={
        'custom': 'AAGC',
        'custom_1': 'A',
    },
    material_params={
        # 'fasta_cdna_fpn': to('data/Homo_sapiens.GRCh38.cdna.all.fa.gz'),  # None False
    },
    seq_num=50,
    working_dir='../../data/tresor/bead/simu/',

    is_sv_umi_lib=True,
    is_sv_seq_lib=True,
    is_sv_primer_lib=True,
    is_sv_adapter_lib=True,
    is_sv_spacer_lib=True,
    # condis=['umi'],
    condis=['umi', 'seq'],
    # condis=['umi', 'custom', 'seq', 'custom_1'],
    sim_thres=3,
    permutation=0,

    # PCR amplification
    ampl_rate=0.85,
    err_route='mutation_table_complete', # bftree sptree err1d err2d mutation_table_minimum mutation_table_complete
    pcr_error=1e-3,
    pcr_num=10,
    err_num_met='nbinodmial',
    seq_error=0.001,
    seq_sub_spl_number=500, # None 200
    seq_sub_spl_rate=False, # 0.333
    use_seed=True,
    seed=1,

    bead_mutation=True,  # True False
    bead_mut_rate=1e-4,  # 0.016 0.00004
    bead_deletion=True,  # True False
    bead_insertion=True,
    bead_del_rate=0.1/112,  # 0.016 0.00004, 2.4e-7
    bead_ins_rate=7.1e-7,  # 0.011 0.00001, 7.1e-7

    pcr_deletion=True,  # True False
    pcr_insertion=True,
    pcr_del_rate=2.4e-6,  # 0.016 0.00004
    pcr_ins_rate=7.1e-7,  # 0.011 0.00001
    seq_deletion=False,
    seq_insertion=False,
    seq_del_rate=2.4e-6,
    seq_ins_rate=7.1e-7,

    verbose=True, # True False

    mode='short_read',  # long_read short_read

    sv_fastq_fp='../../data/tresor/bead/simu/',
    sv_fastq_fn='example',
)