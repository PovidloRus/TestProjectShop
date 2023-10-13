import os
from pathlib import Path
from src.shared.settings.utils import get_config

SETTINGS_DIR = Path(__file__).parent
BASE_DIR = SETTINGS_DIR.parent

config_key = os.environ.get('CONFIG', 'dev')

configs_dir = SETTINGS_DIR / 'config'
config_path = configs_dir / f'config_{config_key}.yaml'
config = get_config(config_path)

postgres_db = {
    'host': config['connections']['postgres']['host'],
    'port': config['connections']['postgres']['port'],
    'username': config['connections']['postgres']['username'],
    'db': config['connections']['postgres']['db'],
    'schema': config['connections']['postgres']['schema'],
    'password':config['connections']['postgres']['password']
}
