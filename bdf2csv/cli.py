import click
from bdf2csv.main import main


@click.command()
@click.argument("input")
@click.argument("output")
def run(input, output):
    """Simple program that greets NAME for a total of COUNT times."""
    main(input, output)

if __name__ == '__main__':
    run()