import click

from lit.keygen import generate_matching_address


@click.group(invoke_without_command=True)
def lit():
    pass


@lit.command()
@click.argument('prefix')
@click.option('--cores', '-c', default='all')
def gen(prefix, cores):
    click.echo(generate_matching_address(prefix, cores))
