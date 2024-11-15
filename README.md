In the project directory, a "data" folder is created to store the input files. For this example, two files (`shuf.a.bed.gz` and `shuf.b.bed.gz`) were downloaded from [figshare](https://figshare.com/s/2d3d4d60a82de9cc3cc6) using the `curl -JLO` command and stored in the "data" folder. These files were then unzipped using the `gunzip` command (Note: the files are too large to upload here). Additionally, a reference file is also placed in the "data" directory, as the data needs to be rescaled according to this reference.

Two more files were created in the "data" directory: `sample.tsv` and `run_metadata.tsv`. The `sample.tsv` contains sample and run information, while `run_metadata.tsv` provides details about the runs and their respective file paths.

A "scripts" directory was created in the main project folder, containing scripts for frequency calculation, line extraction, and plotting graphs.

In the main directory, a Snakemake file (`rescale_to_reference.smk`) was created to incorporate the necessary scripts and rules. After activating the Snakemake environment, you can run the pipeline with the following command:

```bash
snakemake --snakefile rescale_to_reference.smk generated_demo/comparison_graph_demo.png -j1
```

In this example, "demo" is the sample name, which can be replaced with any sample name as needed.# rescale_to_reference
