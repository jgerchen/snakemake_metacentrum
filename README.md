# snakemake_metacentrum
## About
This is a very basic cluster profile for running the [Snakemake workflow system](https://snakemake.readthedocs.io/en/stable/) on the [MetaCentrum distributed computing infrastructure](https://metavo.metacentrum.cz/en/index.html).

## Installation
The standard directory for snakemake cluster profiles is located in `$HOME/.config/snakemake`. Create it if it doesn't exist and enter the directory using

```cd $HOME/.config/snakemake```

The clone the git repository using

```git clone https://github.com/jgerchen/snakemake_metacentrum/```

## Use
This snakemake profile can be used by adding 
```--profile snakemake_metacentrum -j 50```
to your Snakemake command, the -j option defines the maximum number of jobs simultaniously added to MetaCentrum. In addition you can set the following resources in the resources directives of your rules:

*mem_mb* - Memory in mb

*disk_mb* - local scratch space in mb

*runtime* - Walltime, format: HH:MM:SS

In addition you can set the number of cores with the *threads* directive.

Also you have to set the *log* directive, Metacentrum will create additional log files in the same folder with the ending .e and .o as well as .e.jobid and .o.jobid.
