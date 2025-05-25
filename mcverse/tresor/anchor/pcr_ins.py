import tresor as ts


criteria = [
    1e-05,
    2.5e-05,
    5e-05,
    7.5e-05,
    0.0001,
    0.00025,
    0.0005,
    0.00075,
    0.001,
    0.0025,
    0.005,
    0.0075,
    0.01,
    0.025,
    0.05,
    0.075,
    0.1,
    0.2,
    0.3,
]

permutation_times = 10

for permut_i in range(permutation_times):

    for i, criterion in enumerate(criteria):
        ts.locus.simu_generic(
            len_params={
                'umi': {
                    'umi_unit_pattern': 2,
                    'umi_unit_len': 8,
                },
                'umi_1': {
                    'umi_unit_pattern': 3,
                    'umi_unit_len': 12,
                },
                'barcode': 12,
                'seq': 100,
                'seq_2': 100,
                'adapter': 12,
                'adapter_1': 10,
                'primer': 10,
                'primer_1': 10,
                'spacer': 10,
                'spacer_1': 10,
            },
            seq_params={
                'custom': 'TCTCTCTCTACACGACGCTCTTCCGATCT',  # length 29
                'custom_1': 'BAGC',  # length 4
                'custom_2': 'A',  # length 1
                'custom_3': 'T' * 30,  # length 30
            },
            seq_num=50,
            seq_len=100,
            working_dir='../../data/tresor/simu/pcr_ins/permute_' + str(permut_i) + '/',
            fasta_cdna_fpn=False,
            # fasta_cdna_fpn=to('data/Homo_sapiens.GRCh38.cdna.all.fa.gz'),

            is_sv_umi_lib=True,
            is_sv_seq_lib=True,
            is_sv_primer_lib=True,
            is_sv_adapter_lib=True,
            is_sv_spacer_lib=True,
            # condis=['umi'],
            # condis=['umi', 'seq'],
            condis=['custom', 'adapter', 'custom_1', 'umi', 'custom_2', 'custom_3'],
            sim_thres=3,
            permutation=permut_i,

            # PCR amplification
            ampl_rate=0.9,
            err_route='sptree',  # tree minnow err1d err2d mutation_table_minimum mutation_table_complete
            # pcr_error=criterion,
            pcr_error=1e-05,
            pcr_num=8,
            err_num_met='nbinomial',
            # seq_error=criterion,
            seq_error=0.001,
            seq_sub_spl_number=5000,  # None 200
            # seq_sub_spl_numbers=[5000],  # None 200
            # seq_sub_spl_numbers=[100, 500, 1000, 10000],  # None 200
            # seq_sub_spl_rate=0.333,

            pcr_deletion=True,  # True False
            pcr_insertion=True,
            pcr_del_rate=2.4e-6, # 0.016 0.00004
            # pcr_ins_rate=criterion,
            pcr_ins_rate=criterion, # 0.011 0.00001
            seq_deletion=True,
            seq_insertion=True,
            seq_del_rate=2.4e-6,
            seq_ins_rate=7.1e-7,
            # seq_ins_rate=7.1e-7,

            use_seed=True,
            seed=permut_i,

            verbose=False,  # True False

            sv_fastq_fp='../../data/tresor/simu/pcr_ins/permute_' + str(permut_i) + '/',
            sv_fastq_fn="pcr_ins_" + str(i),
        )