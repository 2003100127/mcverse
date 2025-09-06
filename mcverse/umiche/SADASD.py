import umiche as uc

bam = uc.io.read_bam(
    bam_fpn="/mnt/d/Document/Programming/Python/mcverse/mcverse/data/umiche/spike-in/Smartseq3.TTACCTGCCAGATTCG.bam",
    verbose=True,
)

print(bam)
print(bam.todf()['read'].iloc[0])
print(bam.todf(tags=['UX']))
print(bam.todf().columns)
