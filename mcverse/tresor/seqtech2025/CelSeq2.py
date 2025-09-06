import pandas as pd
import tresor as ts

gspl = {
    'Gene_1': 53,
    'Gene_2': 25,
    'Gene_3': 58,
    'Gene_4': 76,
    'Gene_5': 26,
    'Gene_6': 34,
    'Gene_7': 52,
    'Gene_8': 68,
    'Gene_9': 11,
    'Gene_10': 34,
}

df = pd.DataFrame.from_dict(gspl, orient='index', columns=['Sample_1'])

print(df)

ts.gene.simu_pcr_err(
    # initial sequence generation
    gspl=df.T,

    len_params={
        'umi': {
            'umi_unit_pattern': 1,
            'umi_unit_len': 6,
        },
        'seq': 100,
    },
    seq_params={
        'custom': 'ATGCATGC',
        'custom_1': 'T' * 24,
    },
    material_params={
        # 'fasta_cdna_fpn': to('data/Homo_sapiens.GRCh38.cdna.all.fa.gz'),  # None False
    },
    seq_num=50,
    working_dir='D:/Document/Programming/Python/umiche/umiche/data/r1/seqtech/simu/celseq2/',

    is_sv_umi_lib=True,
    is_sv_seq_lib=True,
    is_sv_primer_lib=True,
    is_sv_adapter_lib=True,
    is_sv_spacer_lib=True,
    condis=['umi', 'custom', 'custom_1'],
    # condis=['umi', 'seq'],
    # condis=['umi', 'custom', 'seq', 'custom_1'],
    sim_thres=2,
    permutation=0,

    # PCR amplification
    ampl_rate=0.9,
    err_route='sptree', # bftree sptree err1d err2d mutation_table_minimum mutation_table_complete
    pcr_errors=[1e-05],
    pcr_num=8,
    err_num_met='nbinomial',
    seq_error=0.01,
    # seq_sub_spl_number=200,
    seq_sub_spl_rate=0.8,
    use_seed=True,
    seed=1,

    mode='short_read', # long_read short_read

    sv_fastq_fp='D:/Document/Programming/Python/umiche/umiche/data/r1/seqtech/simu/celseq2/',
    sv_fastq_fn='celseq2',
    verbose=False,  # True False
)