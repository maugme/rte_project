# Exercice - MàJ fichier de configuration

## Contexte

Dans le cadre de l'installation d'une application, il est nécessaire de mettre à jour un fichier de configuration
lorsque la version de l'application change.

Par exemple, si l'application passe de la version 2.14.4 à la version 2.15.0, on peut avoir besoin de mettre à jour
un fichier de configuration `application.yaml` pour ajouter, modifier ou supprimer des paramètres.

## Objectif

L'objectif de cet exercice est de mettre à jour un fichier de configuration `application.yaml` en fonction de la version
de l'application. Nous allons nous placer dans le scénario à l'on souhaite mettre à jour le fichier de configuration
e la version 2.14 à la version 2.15.

Nous allons partir de la fonction `update_config` suivante :

```python
import yaml
from pathlib import Path


def update_local_config(source_path: Path, target_path: Path, version: str) -> None:
    """
    Update the configuration file to the given version
    """
    with source_path.open(mode="r") as f:
        config = yaml.safe_load(f)

    version_info = tuple(map(int, version.split(".")))
    if version_info < (2, 15):
        config = update_config_2_14(config)

    with target_path.open(mode="w") as f:
        yaml.dump(config, f)
```

Cette fonction permet de lire un fichier de configuration `source_path` au format YAML,
de mettre à jour le contenu de ce fichier en fonction de la version `version` de l'application,
puis d'écrire le résultat dans un fichier de configuration `target_path` au format YAML.

## Exercice

Update configuration from version 2.14.x to version 2.15

Add the following parameter in `launcher.local`:

```yaml
launcher:
local:
enable_nb_cores_detection: True
```

Remove the following parameter from `launcher.slurm`:

```yaml
launcher:
slurm:
default_n_cpu: 20
```

Add the following parameter in `launcher.slurm`:

```yaml
launcher:
slurm:
enable_nb_cores_detection: False
nb_cores:
  min: 1
  default: 20
  max: 24
```

> NOTE: `launcher.slurm.default_n_cpu` is replaced by `launcher.slurm.nb_cores.default` parameters.

In any case, we must ensure that `min` <= `default` <= `max`, with the following calculated values:

- The default value for `min` is 1.
- The default value for `max` is the number of cores available on the machine.
- The default value for `default` is `max` - 2.
