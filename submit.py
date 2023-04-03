#!/usr/bin/env python3
import sys
import re
import subprocess
from snakemake.utils import read_job_properties

jobscript=sys.argv[1]
job_probs=read_job_properties(jobscript)
submit_command="qsub %s -l select=1:ncpus=%s:mem=%smb:scratch_local=%smb -l walltime=%s -m n -o %s.cluster.o -e %s.cluster.e" % (jobscript, job_probs["threads"], job_probs["resources"]["mem_mb"], job_probs["resources"]["disk_mb"], job_probs["resources"]["runtime"], job_probs["log"][0], job_probs["log"][0])
submit.response=subprocess.run(submit_command, check=True, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
#TODO: get job id from output using RE
job_id=^[0-9]+\.
#TODO: change the name of error and output files job was submitted and we have a jobid
#qalter -o ${path}.o{$jobid} -e ${path}.e${jobid} 
change_output_response=subprocess.run("qalter -o %s.o%s -e %s.e%s %s" % (job_probs["log"][0], job_id, job_probs["log"][0], job_id, job_id), check=True, shell=True)

print(job_id)

