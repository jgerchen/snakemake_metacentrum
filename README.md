# snakemake_metacentrum

This is a cluster profile for running Snakemake on the MetaCentrum computing environment. It is relatively simple, but it allows tracking jobs, which have been moved between across queues, which MetaCentrum does all the time.

## Installation

The standard directory for cluster profiles is $HOME/.config/snakemake. If it doesn't exist create it, change your directory there and clone the cluster profile using 
```
git clone https://github.com/jgerchen/snakemake_metacentrum
```

## Use

You can use the cluster profile by adding **--profile snakemake_metacentrum** to your snakemake command, or the full path to the profile directory if you put it somewhere else then $HOME/.config/snakemake

## Issues

Snakemake tends to crash after a few few hours of run time, because MetaCentrum looses connection and access privileges. Decreasing the frequency by which MetaCentrum checks the job status appears to improve/solve these issues. This can be done by changing the value using the **--max-status-checks-per-second** option in snakemake. Standard value is 10, I had success with 0.5, but will have a further look at this and update this site.
