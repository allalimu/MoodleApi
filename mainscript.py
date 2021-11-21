import click,sys;
from CommandsList import packages; 

@click.group()
@click.option('--debug/--no-debug', default=False)
def main(debug):
    #click.echo(f"Debug mode is {'on' if debug else 'off'}")
    pass

#####################################
##  Add Command Scripts Here
#####################################
for key,package in packages.items():
    __import__(package["package"]);
    cmd_str=str(package["package"]+"."+package["function"]);
    method_to_call=getattr(sys.modules[package["package"]],package["function"]);    
    main.add_command(method_to_call,key);
