import click
import Project.DataGathering.getUsers as MoodleUsers;
import Project.DataAnalysis.UsersReport as UsersReport;

@click.command()
@click.option('-sd','--skip_getting_data', is_flag=True)
def cli(skip_getting_data):
    """OldUsersCommand script."""
    #click.echo('Old users script is starting!')
    try:
        if not skip_getting_data:
            MoodleUsers.getUsers();
        UsersReport.getOldUsersReport();
    except Exception as error:
        click.echo("Error: {0}".format(error));