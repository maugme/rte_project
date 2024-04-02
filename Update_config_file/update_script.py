import sys
import multiprocessing
import yaml
from pathlib import Path

def update_config_2_14(config):
    # get launcher parameter since it is the only parameter that must be updated
    launcher = config["launcher"]

    # add enable_nb_cores_detection parameter
    launcher["local"].update({
        "enable_nb_cores_detection": True
    })

    # remove default_n_cpu parameter
    launcher["slurm"].pop("default_n_cpu")

    launcher["slurm"].update({
        "enable_nb_cores_detection": False
    })

    # add nb_cores parameter
    nb_cores_value = {
        "min": 1,
        "default": multiprocessing.cpu_count() - 2,
        "max": multiprocessing.cpu_count()
    }

    # Handle error in case nb_cores values are not valid
    # TODO: whom number of cores should we consider here ?
    error_messages = ''
    if nb_cores_value["min"] != 1:
        error_messages += f"Value of nb_cores_value['min'] must be 1, not {nb_cores_value["min"]}.\n"
    if nb_cores_value["max"] != multiprocessing.cpu_count():
        error_messages += f"Value of nb_cores_value['max'] must be {multiprocessing.cpu_count()}, not {nb_cores_value["max"]}.\n"
    if nb_cores_value["default"] != nb_cores_value["max"] - 2:
        error_messages += f"Value of nb_cores_value['default'] must be {multiprocessing.cpu_count() - 2}, not {nb_cores_value['default']}.\n"
    
    if error_messages:
        # if there is an error detected, error_messages is not empty
        raise ValueError(error_messages)
    
    # finally update launcher.slurm.nb_cores
    # and add 'enable_nb_cores_detection: False' to it
    launcher["slurm"].update({
        "nb_cores": nb_cores_value,
        "enable_nb_cores_detection": False
        
    })

    return config
    

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

def main(file_name1="application-2.14.yaml", file_name2="application-2.15_test.yaml"):
    # project root
    root = Path('.').resolve().joinpath('Update_config_file/')
    source = root.joinpath(Path(file_name1))
    target = root.joinpath(Path(file_name2))
    # change configuration file version
    update_local_config(source, target, "2.14")


if __name__ == "__main__":
    # wait for 2 file name
    if len(sys.argv) < 3:
        print("Usage : python ./Update_config_file/update_script.py application-2.14.yaml application-X.XX.yaml")
        exit(0)
    main(sys.argv[1], sys.argv[2])