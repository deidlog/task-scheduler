from src.config_loader import load_config


def test_load_config():
    jobs = load_config('config/confgi.yaml')
    assert isinstance(jobs, list)
    assert len(jobs) > 0
    assert all('name' in job and 'command' in job and 'interval' in job for job in jobs)
    
test_load_config()