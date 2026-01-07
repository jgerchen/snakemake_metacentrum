#!/usr/bin/env python3
import subprocess
import sys
import time
import re
jobid = sys.argv[1]

job_status_cmd="qstat -xf %s" % jobid
while True:
	try:
		job_status_reply=subprocess.run(job_status_cmd, check=True, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
		break
	except:	
		time.sleep(60)
		pass
run_status=re.findall("job_state = (.)", job_status_reply)[0]
if run_status=="M":
	moved_queue=re.findall("queue = .+@(.+)", job_status_reply)[0]
	job_status_cmd_mvd="qstat -xf %s@%s" % (jobid, moved_queue)
	while True:
		try:
			job_status_reply=subprocess.run(job_status_cmd_mvd, check=True, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
			break
		except:
			time.sleep(60)
			pass
	run_status=re.findall("job_state = (.)", job_status_reply)[0]
if run_status=="R" or run_status=="Q" or run_status=="E" or run_status=="T":
	print("running")
elif run_status=="F":
	exit_status=re.findall("Exit_status = (.+)", job_status_reply)[0]
	if exit_status=="0":
		print("success")
	else:
		print("failed")
else:
	print("Error: unable to get job status for job %s, inferred run status: %s, complete job status reply %s" % (jobid, run_status,job_status_reply))
