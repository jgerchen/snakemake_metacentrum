# snakemake_metacentrum

This is the updated cluster module for running Snakemake on the MetaCentrum computing environment for Snakemake versions 8 and greater, which does not use the cluster command anymore, but cluster executer plugins. For older Snakemake versions, please go back to commit 437b8d9. 
This script is relatively simple, but it allows tracking jobs, which have been moved between across queues, which MetaCentrum does all the time.

## Installation

You first have to install the [cluster-generic executer plugin](https://snakemake.github.io/snakemake-plugin-catalog/plugins/executor/cluster-generic.html)

In general, you can install it via pip using 
```
pip install snakemake-executor-plugin-cluster-generic
```

If you installed Snakemake via conda, you can install the executer plugin in your Snakemake environment using
```
conda install -c bioconda snakemake-executor-plugin-cluster-generic
```

The standard directory for cluster profiles is $HOME/.config/snakemake. If it doesn't exist create it, change your directory there (cd $HOME/.config/snakemake) and clone the cluster profile using 
```
git clone https://github.com/jgerchen/snakemake_metacentrum
```

## Use

You can use the cluster profile by adding **--profile snakemake_metacentrum** to your snakemake command, or the full path to the profile directory if you put it somewhere else then $HOME/.config/snakemake

Before running your snakemake command you now have to set the environmental variable **XDG_CACHE_HOME** to some writable folder, otherwise your job will crash.
So if you submit your Snakemake command on MetaCentrum in a job script, you'll have to add something like the following line in the beginning:
```
XDG_CACHE_HOME="/storage/brno12-cerit/home/your_user_id/source_cache" 
```
Where your_user_id is your user id on Metacentrum and source_cache is the location of a writable folder in your home directory.
