import click

from ntbk.crud.home import ensure_ntbk_home
from ntbk.crud.pages import ensure_ntbk_page

@click.group()
@click.pass_context
def ntbk(ctx):
    """Your terminal based personal notebook application"""
    ensure_ntbk_home()
    ctx.ensure_object(dict)


@ntbk.command()
@click.pass_context
@click.option("--page", type=str , help="Create a new notebook page",)
@click.option("--note", type=str, help="Create a new note in the notebook page")
def new(ctx, page, note):
    """Create a new notebook page or note"""
    
    if not (page or note):
        click.secho("You must specify either a page or a note.", fg="red", bold=True)
        return
    
    if page:
        ensure_ntbk_page(page)


