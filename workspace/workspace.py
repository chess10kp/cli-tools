try:
    import click
    from inspect import getsourcefile
    import webbrowser
    import os
    import subprocess
except ModuleNotFoundError:
    click.echo("type:")
    click.echo("pip install click sqlite3 sys webbrowser")
    quit()


@click.command()
def hello():
    try:
        with open(os.path.dirname(getsourcefile(lambda : 0))+"/urls.txt") as f:
            f = f.read().split()
            for i in f:
                try:
                    webbrowser.get('/usr/bin/firefox').open(i)
                except webbrowser.Error:
                    webbrowser.open(i)
    except FileNotFoundError:
        click.echo("url file does not exist")

    try:
        with open(os.path.dirname(getsourcefile(lambda :0))+"/apps.txt") as f:
            f = f.read().split()
            for i in f:
                subprocess.Popen(i)
    except FileNotFoundError:
        click.echo("apps file does not exist")

    try:
        with open(os.path.dirname(getsourcefile(lambda :0))+"/scripts.txt") as f:
            f = f.read().split()
            for i in f:
                subprocess.Popen(i)
    except FileNotFoundError:
        click.echo("Scripts.txt may have been moved")

    quit()

if __name__ == "__main__":
    hello()