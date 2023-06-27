import heroku3  # type: ignore
from os import getenv
from yaml import safe_load
import logging


def set_config(heroku_app: str, var: str, value: str):
    logging.debug(f"Setting Heroku app {heroku_app=} config variable {var=}")
    heroku_conn = heroku3.from_key(getenv("HEROKU_API_KEY"))
    current_app = heroku_conn.apps()[heroku_app]
    config = current_app.config()
    config[var] = value


def configure_heroku_from_yaml(yaml_file: str):
    with open(yaml_file, "r") as yf:
        configurator: dict = safe_load(yf)

    # Heroku application to configure
    heroku_app = configurator["heroku_application"]

    configurables = configurator["configurables"]
    for configurable_name in configurables.keys():
        set_config(heroku_app, configurable_name, configurables[configurable_name])
