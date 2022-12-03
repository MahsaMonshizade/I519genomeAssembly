# I519genomeAssembly

1. Clone the repository using the following comman
```
git clone https://github.com/MahsaMonshizade/I519genomeAssembly.git
```
2. singularity setup: 

2.1. If you are using carbonate, follow the following link to setup the singularity

https://blogs.iu.edu/ncgas/2021/04/29/a-quick-intro-to-singularity-containers/

then run:
```
module load singularity
singularity build --remote genomeAssembly.sif genomeAssembly.def
```
2.2. If you are using the local machine, use the folloing link to install singularity:
https://singularity-tutorial.github.io/01-installation/

then run:
```
singularity build genomeAssembly.sif genomeAssembly.def
```

3. Now you have to run the bash script using the following comand:

```
singularity exec -e genomeAssembly.sif bash FinalProject
```



