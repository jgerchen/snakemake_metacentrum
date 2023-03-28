import sys
from snakemake.utils import read_job_properties

jobscript=sys.argv[1]
#gets information from standard jobscript from Snakemake
snakemake.utils.read_job_properties(jobscript)

#Next, create jobscript

#submit it

#finally, get and return jobid
