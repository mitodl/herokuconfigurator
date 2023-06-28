import heroku3  # type: ignore
from os import getenv
from yaml import safe_load


def configure_heroku_from_yaml(yaml_file: str):
    with open(yaml_file, "r") as yf:
        configurator: dict = safe_load(yf)

    # Heroku application to configure
    heroku_app = configurator["heroku_application"]
    heroku_conn = heroku3.from_key(getenv("HEROKU_API_KEY"))

    configurables = configurator["configurables"]
    print(f"Updating {heroku_app=} with config vars {configurables.keys()=}")
    heroku_conn.update_appconfig(heroku_app, configurables)
