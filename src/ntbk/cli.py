import click

from ntbk.utils.constants import NTBK_HOME
from ntbk.utils.utils import build_ntbk_path

from ntbk.crud.bookmark import ensure_bookmark, read_bookmark, write_bookmark
from ntbk.crud.home import ensure_ntbk_home
from ntbk.crud.notes import is_within_char_limit, write_note
from ntbk.crud.pages import ensure_ntbk_page, is_page_blank

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
    """
    ntbk new note:                   creates a note in the bookmarked page
    ntbk new note --page <dummy>:    creates a note in the dummy page
    """

    bmk = ctx.obj["bookmark"]
    
    if not(page or bmk):
        click.secho("no page found\n", bold=True, fg="red")
        raise click.UsageError("must create at least one page before creating notes!") 
    
    fpage = build_ntbk_path(page) if page else build_ntbk_path(bmk) 

    click.echo("Press ENTER to save note\n")

    note = click.prompt("",prompt_suffix=">> ")
    if not is_within_char_limit(note):
        click.secho("144 character limit exceeded!\n", bold=True, fg="red")
        raise click.UsageError(f"current note has {len(note)} characters, limit is 144")

    write_note(
        note=note,
        append=is_page_blank(fpage),
        fpage=fpage
    )
        