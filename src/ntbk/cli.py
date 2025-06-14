import click

from ntbk.crud.home import ensure_ntbk_home

@click.command()
@click.pass_context
def ntbk(ctx):
    ensure_ntbk_home()
    ctx.ensure_object(dict)