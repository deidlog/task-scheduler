import yaml
import os


def load_config(path: str) -> list:
    """
    Loads job configuration from a YAML file.

    Args:
        path (str): Path to the YAML configuration file.

    Returns:
        list: A list of job dictionaries containing 'name', 'command', and 'interval'.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the YAML is invalid or the structure is incorrect.
    """
    
    # Check if the file exists
    if not os.path.exists(path):
        raise FileNotFoundError
    
    # Try to read and parse the YAML file
    with open(path, 'r') as file:
        try:
            config = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            raise ValueError(f'Invalid YAML format: {exc}')
    
    # Validate that the config has a 'jobs' key and it's a list
    if 'jobs' not in config or not isinstance(config['jobs'], list):
        raise ValueError("Config must contain a list of jobs under the 'jobs' key.")
    
    # Validate that each job contains the required keys
    for job in config['jobs']:
        if not all(key in job for key in ('name', 'command', 'interval')):
            raise ValueError(f"Each job must contain 'name', 'command', and 'interval'. Got: {job}")
        
    return config['jobs']
