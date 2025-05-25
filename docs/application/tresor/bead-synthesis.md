# Bead error propagation through PCR

In this tutorial, we apply **Tresor** to investigate how errors introduced during bead synthesis propagate through PCR amplification and ultimately affect reads in the final sequencing pool.

## Problem
Upon reading [the Tresor article](https://doi.org/10.1101/2025.03.15.643015), some may be curious about a particular statement we included in the **_Introduction_** section:

>"Based on the fact that one out of ten Drop-seq beads suffering from deletion errors according to (Zhang et al. 2019), our simulations initiated with 50 molecules at one gene-by-cell type estimate around 8-14% of final sequencing reads suffering from bead synthesis-induced errors, and notably, this figure can even become doubled if the PCR error rate is elevated by one order of magnitude (i.e., 1e-4 to 1e-3)."

This message contains two key points:

:::{hint} highlights
1. synthesis errors originating from the beads affect **8–14%** of final sequencing reads.

2. If the PCR error rate increases by an order of magnitude, the proportion of bead-error-affected reads due to initial bead synthesis errors can **double**.
:::

But how were these figures derived? We can use **Tresor** to answer this.

## Library installation

To get the data, we can first install **Tresor** (version `0.1.2`).

```{code} shell
# create a conda environment
conda create --name tresor python=3.11

# activate the conda environment
conda activate tresor

pip install tresor==0.1.2
```

## Analysis

Before running the simulations, one of the most critical preparation steps is to define **the error rates** across different stages of the sequencing process, including bead synthesis, PCR amplification, and the final sequencing step. To this end, we reviewed relevant literature to obtain reasonable estimates for these parameters. Once the error rates are determined, the simulations can be conveniently run using just a few simple commands.

### 1. Deletion and insertion error rates

According to [Potapov aand Ong, 2017](https://doi.org/10.1371/journal.pone.0169774), the insertion rate is generally around {math}`7.1×10^−7`, and the deletion rate is around {math}`2.4×10^−6`. In our simulations, we applied the values consistently across all stages, i.e., bead synthesis, PCR amplification, and final sequencing, by setting a unified indel rate to reflect realistic error propagation.

>For the same sample, deletion and insertion (indel) rates were measured to be {math}`2.4×10^−6` and {math}`7.1×10^−7` errors/base, respectively, indicating that the single-molecule sequencing fidelity assay had a much higher background rate for detecting insertions and deletions and these types of errors could not confidently be reported.

### 2. Deletion error rate specific to beads

We identified the deletion error rate specific to bead synthesis, and therefore used this updated value for the `bead_del_rate` parameter. According to a published study by [Zhang et al., 2019](https://doi.org/10.1016/j.molcel.2018.10.020), a deletion error appears on 10% of beads in drop-seq single-cell sequencing.

>"Specifically, about 10% of Drop-seq beads contained a one-base deletion in cell barcodes, which also required extra care during data analysis (see STAR Methods)."
> - by https://doi.org/10.1016/j.molcel.2018.10.020

Based on this rough bead-level error frequency, we then estimated a per-Base deletion error rate. We used a probabilistic model based on the following assumptions.

- Each bead contains **N** sequences, each of length **L** nucleotides.
- The per-nucleotide deletion error rate is denoted as **p**.
- A sequence is considered incorrectly synthesised if it contains at least a deletion error.
- A bead is considered incorrectly synthesised if at least one of its sequences contains a deletion error.

---

We consider the probability that a bead is affected, i.e., at least one sequence contains an error.

$$
\frac{1}{10} = 1 - \left( (1 - p)^L \right)^N
$$

---


We simulated a sequence of length 112, with its UMI of length 12 following 10X V3 chemistry and its genome sequence of length 100. That means **L=112**. We then estimated $p$ for different values of **N (number of sequences per bead)**:

---

| Sequences per bead (N) | Estimated per-base deletion error rate (p) |
|------------------------|--------------------------------------------|
| 50                     | 1.95 × 10⁻⁴                                |
| 100                    | 1.02 × 10⁻⁴                                |
| ...                    | ...                                        |

---

These errors were then used as input parameters for our error-propagation simulations using **Tresor**.

### 3. Realisation

We can run the code below to view the result.

```{code} python
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
        # 'fasta_cdna_fpn': to('data/Homo_sapiens.GRCh38.cdna.all.fa.gz'),
    },
    seq_num=50,
    working_dir='../../data/tresor/bead/simu/',

    is_sv_umi_lib=True,
    is_sv_seq_lib=True,
    is_sv_primer_lib=True,
    is_sv_adapter_lib=True,
    is_sv_spacer_lib=True,
    condis=['umi', 'seq'],
    sim_thres=3,
    permutation=0,

    # PCR amplification
    ampl_rate=0.85,
    err_route='mutation_table_complete', # bftree sptree err1d err2d mutation_table_minimum mutation_table_complete
    pcr_error=1e-4,
    pcr_num=10,
    err_num_met='nbinodmial',
    seq_error=0.01,
    seq_sub_spl_number=500,
    seq_sub_spl_rate=False,
    use_seed=True,
    seed=1,

    bead_mutation=True,
    bead_mut_rate=1e-4,
    bead_deletion=True,
    bead_insertion=True,
    bead_del_rate=0.1/112,
    bead_ins_rate=7.1e-7,

    pcr_deletion=True,
    pcr_insertion=True,
    pcr_del_rate=2.4e-6,
    pcr_ins_rate=7.1e-7,
    seq_deletion=False,
    seq_insertion=False,
    seq_del_rate=2.4e-6,
    seq_ins_rate=7.1e-7,

    verbose=True,

    mode='short_read',
    
    sv_fastq_fp='../../data/tresor/bead/simu/',
    sv_fastq_fn='example',
)
```

It prompts:

```{code} shell
25/05/2025 21:29:45 logger: ======>Before sampling
25/05/2025 21:29:45 logger: =========>Percentage of reads with deletion errors from bead synthesis: 0.07436801881246326
25/05/2025 21:29:45 logger: =========>Percentage of reads with deletion errors from bead synthesis and errors from PCR amplication: 0.084740068867053
```

Repeating the sampling multiple times, we found that the value consistently falls within the range of `8%` to `14%`. The above results were obtained from the full, unsampled sequencing pool after sequencing. However, we further assessed the stability of this estimate by randomly sampling `500` reads from the pool. The results showed minimal differences, indicating that our sampling—based on a uniform random distribution—preserved consistency between the full and sampled data.

```{code} shell
25/05/2025 21:29:45 logger: ======>After sampling
25/05/2025 21:29:45 logger: =========>Percentage of reads with deletion errors from bead synthesis: 0.096
25/05/2025 21:29:45 logger: =========>Percentage of reads with deletion errors from bead synthesis and errors from PCR amplication: 0.078
```

Additionally, the current PCR error rate (`pcr_error`) was set to `0.0001`. When we increased it to `0.001`, we observed that the number of error-affected reads approximately **doubled**.

Before sampling

```{code} shell
25/05/2025 22:44:42 logger: =========>Percentage of reads with deletion errors from bead synthesis: 0.14802217183169564
25/05/2025 22:44:42 logger: =========>Percentage of reads with deletion errors from bead synthesis and errors from PCR amplication: 0.2352397749223146
```

After sampling

```{code} shell
25/05/2025 22:44:42 logger: =========>Percentage of reads with deletion errors from bead synthesis: 0.266
25/05/2025 22:44:42 logger: =========>Percentage of reads with deletion errors from bead synthesis and errors from PCR amplication: 0.148
```