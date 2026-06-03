import uvicorn
import yaml
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def load_config():
    config_path = Path(__file__).parent / "config" / "app_config.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def main():
    config = load_config()
    logger.info(f"Starting {config['app']['name']} v{config['app']['version']}")
    
    from api import create_app
    app = create_app(config)
    
    uvicorn.run(
        app,
        host=config["server"]["host"],
        port=config["server"]["port"]
    )

if __name__ == "__main__":
    main()