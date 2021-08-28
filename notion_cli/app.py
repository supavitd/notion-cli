import os

import click
from notion_client import Client


@click.group()
@click.pass_context
def run(ctx):
    ctx.notion = ctx.with_resource(Client(auth=os.environ["NOTION_TOKEN"]))
