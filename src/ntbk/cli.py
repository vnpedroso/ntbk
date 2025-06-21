import click

from ntbk.crud.home import ensure_ntbk_home
from ntbk.crud.pages import ensure_ntbk_page

@click.group()
@click.pass_context
def ntbk(ctx):
    ensure_ntbk_home()
    ctx.ensure_object(dict)


@ntbk.command()
@click.pass_context
@click.option("--page", is_flag=True, type=str , help="Create a new notebook page",)
@click.option("--note", is_flag=True, type=str, help="Create a new note in the notebook page")
@click.argument("name", required=True)
def new(ctx, page, note, name):
    if page and note:
        click.secho("You must specify either a page or a note, not both.", fg="yellow", bold=True)
        return
    if not (page and note):
        click.secho("You must specify either a page or a note.", fg="yellow", bold=True)
        return
    
    if page:
        ensure_ntbk_page(name)

