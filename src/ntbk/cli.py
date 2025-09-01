import click

from ntbk.crud.home import ensure_ntbk_home
from ntbk.crud.pages import ensure_ntbk_page

@click.group()
@click.pass_context
def ntbk(ctx):
    """Your terminal based personal notebook application"""
    ensure_ntbk_home()
    ctx.ensure_object(dict)

@ntbk.group
@click.pass_context
def new(ctx):
    """
    ntbk new page --> creates a new PAGE\n
    ntbk new note --> creates a new NOTE
    """
    pass

@new.command
@click.pass_context
@click.argument("page_name")
def page(ctx, page_name):
    """ntbk new page <page_name> --> creates new page with name <page_name>"""
    ensure_ntbk_page(page_name)
    click.secho(f'page "{page_name}" successfully created', fg="green", bold=True)

@new.command
@click.pass_context
def note(ctx):
    pass


