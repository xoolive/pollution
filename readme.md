## Étude de cas

Pour récupérer le projet (sous Windows voir plus bas):

```
git clone --recurse-submodules https://github.com/poitou/ETE
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

// seulement si sous Windows et avant le git clone ...
conda install git         

jupyter notebook
```

