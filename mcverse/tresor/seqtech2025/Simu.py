import tresor as ts

gspl = {
    'GAAA': 100,
    'GAAC': 25,
    'GAAT': 58,
    'GAAG': 76,
    'GACA': 26,
    'TAAA': 34,
    'GCAA': 52,
    'GAGA': 68,
    'GATA': 11,
    'GTAA': 34,
}

for gene, gene_exp in gspl.items():
    ts.locus.simu_generic(
        # initial sequence generation
        len_params={
            'umi': {
                'umi_unit_pattern': 1,
                'umi_unit_len': 6,
            },
            'barcode': 8,
            'seq': 100,
            'seq_2': 100,
            'adapter': 10,
            'adapter_1': 10,
            'primer': 10,
            'primer_1': 10,
            'spacer': 10,
            'spacer_1': 10,
        },
        seq_params={
            'custom': 'ATGCATGC',
            'custom_1': 'AAAAAAAAA',
            'custom_2': gene,
        },
        material_params={
            # 'fasta_cdna_fpn': 'data/Homo_sapiens.GRCh38.cdna.all.fa.gz',  # None False
        },
        seq_num=gene_exp,
        working_dir='D:/Document/Programming/Python/umiche/umiche/data/r1/seqtech/simu/',

        is_sv_umi_lib=True,
        is_sv_seq_lib=True,
        is_sv_primer_lib=True,
        is_sv_adapter_lib=True,
        is_sv_spacer_lib=True,
        condis=['umi', 'custom', 'custom_1', 'custom_2'],
        # condis=['umi', 'seq'],
        # condis=['umi', 'custom', 'seq', 'custom_1'],
        sim_thres=3,
        permutation=0,

        # PCR amplification
        ampl_rate=0.9,
        err_route='err2d',  # bftree sptree err1d err2d mutation_table_minimum mutation_table_complete
        pcr_error=1e-05,
        pcr_num=8,
        err_num_met='nbinomial',
        seq_error=0.01,  # 0.005 0.01 0.05 0.1
        seq_sub_spl_number=None,  # None 200 2000
        seq_sub_spl_rate=1,  # 0.333
        use_seed=True,
        seed=1,

        bead_mutation=True,
        bead_mut_rate=1e-4,
        bead_deletion=True,
        bead_insertion=True,
        bead_del_rate=0.1 / 112,
        bead_ins_rate=7.1e-7,

        pcr_deletion=False,
        pcr_insertion=False,
        pcr_del_rate=2.4e-6,
        pcr_ins_rate=7.1e-7,
        seq_deletion=False,
        seq_insertion=False,
        seq_del_rate=2.4e-6,
        seq_ins_rate=7.1e-7,

        verbose=False,  # True False

        mode='short_read',  # long_read short_read

        sv_fastq_fp='D:/Document/Programming/Python/umiche/umiche/data/r1/seqtech/simu/',
        sv_fastq_fn='celseq',
    )