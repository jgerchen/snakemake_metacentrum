#!/usr/bin/env python3
import subprocess
import sys
import re
jobid = sys.argv[1]

job_status_cmd="qstat -xf %s" % jobid
job_status_reply=subprocess.run(job_status_cmd, check=True, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
run_status=re.findall("job_state = (.)", job_status_reply)[0]
if run_status=="M":
	moved_queue=re.findall("queue = .+@(.+)", job_status_reply)[0]
	job_status_cmd_mvd="qstat -xf %s@%s" % (jobid, moved_queue)
	job_status_reply=subprocess.run(job_status_cmd_mvd, check=True, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
	run_status=re.findall("job_state = (.)", job_status_reply)[0]
if run_status=="R" or run_status=="Q":
	print("running")
elif run_status=="F":
	exit_status=re.findall("Exit_status = (.+)", job_status_reply)[0]
	if exit_status=="0":
		print("success")
	else:
		print("failed")
else:
	print("Error: unable to get job status for job %s" % jobid)
