import click
import os
import subprocess

@click.group()
def cli():
    pass

@cli.command()
@click.argument('project_name')
@click.argument('version')
def add_project(project_name, version):
    try:
        os.makedirs(project_name)

        # Create main.c file
        with open(os.path.join(project_name, 'main.c'), 'w') as f:
            f.write('#include <stdio.h>\n\nint main() {\n    printf("Hello, World!\\n");\n    return 0;\n}\n')

        # Create CMakeLists.txt file
        with open(os.path.join(project_name, 'CMakeLists.txt'), 'w') as f:
            f.write(f'''cmake_minimum_required(VERSION {version})
project({project_name} C)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
add_executable({project_name} main.c)''')

        # Run PowerShell command
        ps_command = (
            'powershell.exe -NoExit -Command "&{{Import-Module '
            '\\"C:\\Program Files (x86)\\Microsoft Visual Studio\\2022\\BuildTools\\Common7\\Tools\\Microsoft.VisualStudio.DevShell.dll\\"; '
            'Enter-VsDevShell 99728ae9 -SkipAutomaticLocation -DevCmdArguments \'-arch=x64 -host_arch=x64\'; '
            'cd {project_dir}; cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=1 . -G \\"Ninja\\"}}"'
        ).format(project_dir=os.path.abspath(project_name))

        subprocess.run(ps_command, shell=True, check=True)

        click.echo(f"Project '{project_name}' created successfully with main.c and CMakeLists.txt, and cmake command executed.")
    except FileExistsError:
        click.echo(f"Project '{project_name}' already exists.")
    except Exception as e:
        click.echo(f"An error occurred: {e}")