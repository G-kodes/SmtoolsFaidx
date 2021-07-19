__author__ = "Graeme Ford"
__copyright__ = "Copyright 2021, Graeme Ford"
__email__ = "graeme.ford@tuks.co.za"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

extra = snakemake.params.get("extra", "")
preloader = snakemake.params.get("preloader", "")

shell(
    "{preloader} "
    "samtools "
    "faidx "
    "{extra} "
    "{snakemake.input} "
    "> {snakemake.input} "
)
