## Étude de cas

Pour récupérer le projet:

```
git clone --recurse-submodules  https://github.com/poitou/ETE
```

Pour charger un environnement convenable, **sur les machines du centre info**:

```
module load python/3.7
source activate ~x.olive/students
jupyter notebook
```

Pour charger un environnement convenable, **sur vos machines perso**:

 1. Installer Anaconda pour votre OS, puis 

 2. dans un "Anaconda Prompt" lancez les commandes suivantes :

```
conda env create -f optim.yml
conda activate isae
jupyter notebook
```

