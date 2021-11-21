import click;

@click.command()
@click.argument('name',default="World")
def RunCommand(name):
    click.echo('Hello '+name)

if __name__ == '__main__':
    RunCommand()