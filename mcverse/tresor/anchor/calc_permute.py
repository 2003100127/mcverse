import umiche as uc


pct_reads, pct_anchor_reads = uc.pipeline.anchor(
    scenario='pcr_del',
    # scenario='seq_del',
    # scenario='seq_ins',
    # scenario='pcr_ins',
    param_fpn='../../data/tresor/anchor/params_anchor.yml',
)

# print(pct_reads)
# print(pct_anchor_reads)

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
    # 0.2,
    # 0.3,
]

uc.vis.anchor_efficiency(
    criteria=criteria,
    quant_captured=pct_reads,
    quant_anchor_captured=pct_anchor_reads,
    condition='PCR deletion error rate',
    # condition='Sequencing deletion error rate',
    # condition='Sequencing insertion error rate',
    # condition='PCR insertion error rate',
)

uc.vis.anchor_efficiency_simple(
    criteria=criteria,
    quant_captured=pct_reads,
    quant_anchor_captured=pct_anchor_reads,
    condition='PCR deletion error rate',
    # condition='Sequencing deletion error rate',
    # condition='Sequencing insertion error rate',
    # condition='PCR insertion error rate',
)

uc.vis.anchor_efficiency_broken(
    criteria=criteria,
    quant_captured=pct_reads,
    quant_anchor_captured=pct_anchor_reads,
    condition='PCR deletion error rate',
    # condition='Sequencing deletion error rate',
    # condition='Sequencing insertion error rate',
    # condition='PCR insertion error rate',
)