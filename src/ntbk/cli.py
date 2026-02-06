import click

from ntbk.utils.constants import HEADERS, NTBK_HOME, PAGE_MAX_NOTES, SEPARATOR
from ntbk.utils.utils import build_ntbk_path, is_page_blank, is_within_char_limit

from ntbk.crud.bookmark import ensure_bookmark, read_bookmark, write_bookmark
from ntbk.crud.home import ensure_ntbk_home
from ntbk.crud.notes import (
    is_within_id_limit, 
    write_note, 
    get_last_note_id,
    format_content
)
from ntbk.crud.pages import ensure_ntbk_page, read_page

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
    ntbk new page:  creates a new page
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
@click.option("--page", help="name of the page on which to write the note, if empty will use bookmarked page")
def note(ctx: click.Context, page):
    """
    ntbk new note:                   creates a note in the bookmarked page
    ntbk new note --page <dummy>:    creates a note in the dummy page
    """

    bmk = ctx.obj["bookmark"]
    
    if not(page or bmk):
        click.secho("no page found\n", bold=True, fg="red")
        raise click.UsageError("must create at least one page before creating notes!") 
    
    if page:
         fpage = build_ntbk_path(page)
         write_bookmark(page)
    else:
        fpage = build_ntbk_path(bmk)

    note_id = 0 if is_page_blank(fpage) else get_last_note_id(fpage, SEPARATOR) + 1

    if not is_within_id_limit(note_id,max_notes_on_page=PAGE_MAX_NOTES):
        click.secho(f"max number of notes reached!")
        raise click.ClickException(f"page {page} reached max number of {PAGE_MAX_NOTES} notes!")

    click.echo("Press ENTER to save note\n")

    content = click.prompt("",prompt_suffix=">> ")
    if not is_within_char_limit(content):
        click.secho("144 character limit exceeded!\n", bold=True, fg="red")
        raise click.UsageError(f"current note has {len(content)} characters, limit is 144")

    note = format_content(
        content=content,
        note_id=note_id,
        sep=SEPARATOR,
    )

    write_note(
        note=note,
        overwrite=is_page_blank(fpage),
        fpage=fpage,
    )

@ntbk.command
@click.pass_context
@click.option("--page", help="name of the page to read, if empty will use bookmarked page")
def read(ctx: click.Context, page):
    """read all notes in the specified page, uses bookmark if no page is provided"""
    
    bmk = ctx.obj["bookmark"]
    if page:
        fpage = build_ntbk_path(page)
    else:
        fpage = build_ntbk_path(bmk)
        page = read_bookmark()

    if not(is_page_blank(fpage)):
        read_page(
            fpage=fpage,
            page_name=page,
            headers=HEADERS,
        )
        return
    
    click.secho(f"\nwhoops, {page} is a blank page",fg="yellow",bold="True")

