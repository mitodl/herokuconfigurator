import typer
import heroku3
from os import getenv

app = typer.Typer()

@app.command()
def set(app: str, var: str, value: str):
    heroku_conn = heroku3.from_key(getenv("HEROKU_API_KEY"))
    current_app = heroku_conn.apps()[app]
    config = current_app.config()
    config[var] = value
    

if __name__ == "__main__":
   typer.run(set) 
