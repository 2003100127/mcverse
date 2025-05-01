# UMIche

## Installation

We strongly suggest installing our software package cloned from its GitHub repository using `pip install .` as there is the latest version of our code. Version `0.1.0` is currently not available for experiment reproducibility.

## Pipeline `heterogeneity`

We can use this pipeline to explore whether merged UMIs originate from the same roots. Specifically, it shows the results in **Supplementary Figure 4**.

Please download the data from the mcverse repository. Then, please decompress it and specify where it is located under attribute `work_dir` in the `params.yaml` file which has the following form.

```{code} python
work_dir: path/to/mclumi-data/

trimmed:
  fastq:
    fpn: None
    trimmed_fpn: None

  umi_1:
    len: 10

  seq:
    len: 100

  read_struct: 'umi_1'


fixed:
  pcr_num: 8
  pcr_err: 0.00001
  seq_err: 0.001
  ampl_rate: 0.85
  seq_dep: 400
  umi_num: 50
  permutation_num: 10
  umi_unit_pattern: 1
  umi_unit_len: 10
  seq_sub_spl_rate: 0.333
  sim_thres: 3


varied:
  pcr_nums: [ # pcr_nums_err_2d_spl0.33
    1, 2, 3,
    4, 5, 6, 7,
    8, 9, 10, 11, 12,
    13, 14, 15, 16,
#    17, 18
#    17, 18, 19, 20,
  ]
  pcr_errs: [
    0.00001,
    0.000025,
    0.00005,
    0.000075,
    0.0001,
    0.00025,
    0.0005,
    0.00075,
    0.001,
    0.0025,
    0.005,
    0.0075,
    0.01,
#    0.025,
    0.05,
#    0.075,
#    0.1,
#    0.2,
#    0.3,
  ]
  seq_errs: [
    0.00001,
    0.000025,
    0.00005,
    0.000075,
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
#    0.2,
#    0.3,
  ]
  ampl_rates: [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
  umi_lens: [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
#  umi_lens: [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
#  umi_nums: [50, 250, 450, 650, 850, 1050]
  umi_nums: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
  seq_deps: [100, 200, 500, 600, 800, 1000, 2000, 3000, 5000 ]
#  seq_deps: [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]


dedup:
  dbscan_eps: 0.5 # o 1.5
  dbscan_min_spl: 5 # o 1
  birch_thres: 0.5 # o 1.8 default 0.5
  birch_n_clusters: None # o None
  hdbscan_min_spl: 3
  aprop_preference: None
  aprop_random_state: 0

  ed_thres: 1
  mcl_fold_thres: 1.6 # 1.6
  iter_num: 100

  inflat_val: 2.7 # 1.1 2.7
  exp_val: 2 # 2 3

#  inflat_val: [1.1, 2.7, 3.6]
#  exp_val: 2

#  exp_val: [2, 3, 4]

  # mcl_ed trace!!!
#  ed_thres: 1
#  mcl_fold_thres: 2 # 1.6
#  inflat_val: 2.7 # 1.1 2.7
#  exp_val: 2 # 2 3
#  iter_num: 100

  # pcr_nums
  # mcl_inflat: 2.3
  # mcl_exp: 2
  # mcl_fold_thres: 1
```

Then, you can run the pipeline as follows.

```{code} python
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
```

It gives output below and saves results in a folder named `seq_errs` under the data folder `mclumi-data`.

Since the method directional is used, the results include:

`directional_apv_cnt.txt`
`directional_apv_pct.txt`
`directional_disapv_cnt.txt`
`directional_disapv_pct.txt`
`directional_dedup.txt`
`directional_node_repr.json`


```markdown
01/05/2025 21:54:04 logger: =========>the neighbor: 223
01/05/2025 21:54:04 logger: =========>the neighbor: 1568
01/05/2025 21:54:04 logger: =========>the neighbor: 2856
01/05/2025 21:54:04 logger: ======>visited UMI nodes: {2691, 2564, 2181, 1795, 2699, 13, 1677, 655, 1814, 2071, 157, 2846, 2850, 2856, 41, 1322, 2601, 2225, 2482, 2102, 191, 321, 2242, 2755, 2758, 2505, 1486, 1115, 1631, 223, 2401, 1768, 119, 762}
01/05/2025 21:54:04 logger: {2691, 2564, 2181, 1795, 2699, 13, 1677, 655, 1814, 2071, 157, 2846, 2850, 2856, 41, 1322, 2601, 2225, 2482, 2102, 191, 321, 2242, 2755, 2758, 2505, 1486, 1115, 1631, 223, 2401, 1768, 119, 762}
01/05/2025 21:54:04 logger: =========>the neighbor: 223
01/05/2025 21:54:04 logger: =========>the neighbor: 768
01/05/2025 21:54:04 logger: =========>the neighbor: 383
01/05/2025 21:54:04 logger: ======>visited UMI nodes: {2691, 2564, 2181, 1795, 2699, 13, 1677, 655, 1814, 2071, 157, 2846, 2850, 2856, 41, 1322, 2601, 2225, 2482, 2102, 191, 321, 2242, 2755, 2758, 2505, 1486, 1115, 1631, 223, 2401, 1768, 119, 762, 383}
01/05/2025 21:54:04 logger: {2691, 2564, 2181, 1795, 2699, 13, 1677, 655, 1814, 2071, 157, 2846, 2850, 2856, 41, 1322, 2601, 2225, 2482, 2102, 191, 321, 2242, 2755, 2758, 2505, 1486, 1115, 1631, 223, 2401, 1768, 119, 762, 383}
01/05/2025 21:54:04 logger: =========>the neighbor: 13
01/05/2025 21:54:04 logger: =========>the neighbor: 157
01/05/2025 21:54:04 logger: =========>the neighbor: 655
01/05/2025 21:54:04 logger: =========>the neighbor: 1568
01/05/2025 21:54:04 logger: ======>visited UMI nodes: {2691, 2564, 2181, 1795, 2699, 13, 1677, 655, 1814, 2071, 157, 2846, 1568, 2850, 2856, 41, 1322, 2601, 2225, 2482, 2102, 191, 321, 2242, 2755, 2758, 2505, 1486, 1115, 1631, 223, 2401, 1768, 119, 762, 383}
01/05/2025 21:54:04 logger: {2691, 2564, 2181, 1795, 2699, 13, 1677, 655, 1814, 2071, 157, 2846, 1568, 2850, 2856, 41, 1322, 2601, 2225, 2482, 2102, 191, 321, 2242, 2755, 2758, 2505, 1486, 1115, 1631, 223, 2401, 1768, 119, 762, 383}

No.16->0.1 for seq_errs dedup cnt: 434
    pn0  pn1  pn2  pn3  pn4  pn5  pn6  pn7  pn8  pn9
0    50   50   50   50   50   50   50   50   50   50
1    50   50   50   50   50   50   50   50   50   50
2    50   50   50   50   50   50   50   50   50   50
3    50   50   50   50   50   50   50   50   50   50
4    50   50   50   50   50   50   50   50   50   50
5    50   50   50   50   50   50   50   50   50   50
6    50   50   50   50   50   50   50   50   50   50
7    50   50   50   50   50   50   50   50   50   50
8    51   51   51   51   51   51   51   51   51   51
9    52   53   52   52   52   52   52   53   52   53
10   54   53   55   56   56   54   55   55   56   55
11   63   65   63   66   64   64   65   59   61   62
12   70   70   66   65   66   71   63   67   70   67
13   89   89   83   89   87   92   92   92   87   86
14  150  134  147  142  144  139  138  135  139  137
15  294  283  284  286  272  291  280  283  289  285
16  455  436  431  454  449  445  460  435  480  434
```