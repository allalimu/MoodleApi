import click
import Project.DataGathering.getUsersPrivateFilesInfo as getUsersPrivateFilesInfo;
import Project.DataAnalysis.PrivateFilesPerYear as PrivateFilesPerYear;
@click.command()
@click.option('-sd','--skip_getting_data', is_flag=True)
def cli(skip_getting_data):
    """PrivateFilesCommand script."""
    try:
        if not skip_getting_data:
            getUsersPrivateFilesInfo.getUsersPrivateFilesData();
        PrivateFilesPerYear.getPerYearReport();
    except Exception as error:
        click.echo("Error: {0}".format(error));