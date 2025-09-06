import random
import pandas as pd
import tresor as ts

gspl = {
    'Gene_1': 19,
    'Gene_2': 83,
    'Gene_3': 8,
    'Gene_4': 6,
    'Gene_5': 20,
    'Gene_6': 51,
    'Gene_7': 60,
    'Gene_8': 56,
    'Gene_9': 45,
    'Gene_10': 44,
}

df = pd.DataFrame.from_dict(gspl, orient='index', columns=['Sample_1'])

print(df)

random_number = random.choice(range(0, 21))
print(random_number)

ts.gene.simu_pcr_err(
    # initial sequence generation
    gspl=df.T,

    len_params={
        'umi': {
            'umi_unit_pattern': 1,
            'umi_unit_len': 8,
        },
        'seq': 100,
    },
    seq_params={
        'custom': 'ATGCATGCATGCATG',
        'custom_1': 'T' * random_number,
    },
    material_params={
        # 'fasta_cdna_fpn': to('data/Homo_sapiens.GRCh38.cdna.all.fa.gz'),  # None False
    },
    seq_num=50,
    working_dir='D:/Document/Programming/Python/umiche/umiche/data/r1/seqtech/simu/quartzseq2/',

    is_sv_umi_lib=True,
    is_sv_seq_lib=True,
    is_sv_primer_lib=True,
    is_sv_adapter_lib=True,
    is_sv_spacer_lib=True,
    condis=['custom', 'umi', 'custom_1'],
    # condis=['umi', 'seq'],
    # condis=['umi', 'custom', 'seq', 'custom_1'],
    sim_thres=3,
    permutation=0,

    # PCR amplification
    ampl_rate=0.9,
    err_route='err2d',  # bftree sptree err1d err2d mutation_table_minimum mutation_table_complete
    pcr_errors=[1e-05],
    pcr_num=8,
    err_num_met='nbinomial',
    seq_error=0.01,
    # seq_sub_spl_number=200,
    seq_sub_spl_rate=0.8,
    use_seed=True,
    seed=1,

    mode='short_read',  # long_read short_read

    sv_fastq_fp='D:/Document/Programming/Python/umiche/umiche/data/r1/seqtech/simu/quartzseq2/',
    sv_fastq_fn='quartzseq2',
    verbose=False, # True False
)