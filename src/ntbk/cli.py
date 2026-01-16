import click

from ntbk.utils.constants import NTBK_HOME

from ntbk.crud.bookmark import ensure_bookmark, read_bookmark, write_bookmark
from ntbk.crud.home import ensure_ntbk_home
from ntbk.crud.pages import ensure_ntbk_page

@click.group()
@click.pass_context
def ntbk(ctx: click.Context):
    """Your terminal based personal notebook application"""
    ensure_ntbk_home()
    ensure_bookmark()
    ctx.ensure_object(dict)
    ctx.obj["bookmark"] = read_bookmark()

@ntbk.group
@click.pass_context
def new(ctx: click.Context):
    """
    ntbk new page:  creates a new page\n
    ntbk new note:  creates a new note
    """
    return

@new.command
@click.pass_context
@click.argument("page_name")
def page(ctx: click.Context, page_name):
    """ntbk new page <dummy>:   creates a new page named <dummy>"""

    ensure_ntbk_page(page_name)
    write_bookmark(page_name)
    click.secho(f'page "{page_name}" successfully created', fg="green", bold=True)

@new.command
@click.pass_context
@click.option("--page", help="name of the page on which to the note")
def note(ctx: click.Context, page):

    bmk = ctx.obj["bookmark"]
    
    if not(page and bmk):
        click.secho("must create at least one page before creating notes!\n", bold=True, fg="red")
        raise click.UsageError("No page found")
    
    if not page:
        return
    
    