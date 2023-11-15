#!/usr/bin/env python3
import sys
import re
import subprocess
import math
from snakemake.utils import read_job_properties

jobscript=sys.argv[1]

job_probs=read_job_properties(jobscript)
#add_conda=subprocess.run("sed -i '1s/^/\/storage\/brno2\/home\/gerchenj\/mambaforge-pypy3\/bin\/activate\n/' "+jobscript, check=True, shell=True)

#def line_prepender(filename, line):
#	with open(filename, 'r+') as f:
#		content = f.read()
#		f.seek(0, 0)
#		f.write(line.rstrip('\r\n') + '\n' + content)

#line_prepender(jobscript, "/storage/brno2/home/gerchenj/mambaforge-pypy3/bin/activate")

def get_runtime(runtime_min):
	runtime_h=math.floor(int(runtime_min)/60)
	remaining_min=str(int(runtime_min%60))
	if len(remaining_min)==1:
		remaining_min="0"+remaining_min
	return "%s:%s:00" % (runtime_h, remaining_min)



submit_command="qsub -V -l select=1:ncpus=%s:mem=%smb:scratch_local=%smb -l walltime=%s -m n -o %s.cluster.o -e %s.cluster.e %s" % (job_probs["threads"], job_probs["resources"]["mem_mb"], job_probs["resources"]["disk_mb"], get_runtime(job_probs["resources"]["runtime"]), job_probs["log"][0], job_probs["log"][0], jobscript)
submit_response=subprocess.run(submit_command, check=True, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
#get job id from output using RE
job_id=re.findall("^[0-9]+", submit_response)[0]
#change the name of error and output files job was submitted and we have a jobid
#qalter -o ${path}.o{$jobid} -e ${path}.e${jobid} 
change_output_response=subprocess.run("qalter -o %s.o%s -e %s.e%s %s" % (job_probs["log"][0], job_id, job_probs["log"][0], job_id, job_id), check=True, shell=True)

print(job_id)

