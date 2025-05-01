import umiche as uc

uc.pipeline.heterogeneity(
    # scenario='pcr_nums',
    # scenario='pcr_errs',
    scenario='seq_errs',
    # scenario='ampl_rates',
    # scenario='umi_lens',
    # scenario='seq_deps',
    # scenario='umi_nums',

    # method='unique',
    # method='cluster',
    # method='adjacency',
    method='directional',
    # method='mcl',
    # method='mcl_val',
    # method='mcl_ed',
    # method='mcl_cc_all_node_umis',
    # method='dbscan_seq_onehot',
    # method='birch_seq_onehot',
    # method='aprop_seq_onehot',
    # method='hdbscan_seq_onehot',
    # method='set_cover',

    # is_trim=True,
    # is_tobam=False,
    # is_dedup=False,

    # is_trim=False,
    # is_tobam=True,
    # is_dedup=False,

    is_trim=False,
    is_tobam=False,
    is_dedup=True,
    is_sv=True,

    param_fpn='../data/umiche/params.yml',
)

