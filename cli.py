import os
from tkinter import filedialog

import click
from rich.console import Console

from mayana import phone, ip

console: Console = Console()
COLUMN, LINES = os.get_terminal_size()


@click.group()
@click.option('--export', default=False, is_flag=True)
def main(export):
    console.print('Welcome to Mayana'.center(COLUMN, '-'), style="bold cyan")
    if export:
        file_path = filedialog.asksaveasfile(mode='w', title='fake.csv')


@main.command()
@click.option('--size', default=1, help='', type=click.types.INT)
@click.option('--phone_no', is_flag=True, default=False, type=click.types.BOOL)
@click.option('--ip_address', is_flag=True, default=False, type=click.types.BOOL)
def build(size, phone_no: bool, ip_address: bool) -> None:
    if phone_no:
        console.print(phone(count=size))
    if ip_address:
        console.print(ip(count=size))


@main.command()
def delete() -> None:
    ...


def help() -> None:
    console.print('Welcome to Mayana'.center(COLUMN, '-'), style="bold cyan")


if __name__ == '__main__':
    main()
