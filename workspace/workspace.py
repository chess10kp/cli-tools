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

browser_path = "/usr/bin/brave"
class Workspace:
    def __init__(self):
        f_web = os.path.dirname(getsourcefile(lambda : 0)) + "/urls.txt"
        f_app = os.path.dirname(getsourcefile(lambda : 0)) + "/apps.txt"
        f_scripts = os.path.dirname(getsourcefile(lambda : 0)) +"/scripts.txt"

    def open_web(self):
        pass


@click.command()
def init_workspace():
    try:
        with open(os.path.dirname(getsourcefile(lambda : 0))+"/urls.txt") as f:
            f = f.read().split()
            browser_obj = webbrowser.get('firefox')
            if len(f)>0:
                for i in f:
                    browser_obj.open_new_tab(i)
            else:
                subprocess.Popen(browser_path)

    except FileNotFoundError:
        click.echo("url file does not exist")

    try:
        with open(os.path.dirname(getsourcefile(lambda: 0))+"/apps.txt") as f:
            f = f.read().split()
            for i in f:
                subprocess.Popen(i)
    except FileNotFoundError:
        click.echo("apps file does not exist")

    try:
        f = open(os.path.dirname(getsourcefile(lambda: 0))+"/scripts.txt")
        fr = f.read()
        for i in fr:
            subprocess.check_output(i)
    except FileNotFoundError:
        click.echo("scripts.txt may have been moved")

    quit()

if __name__ == "__main__":
    init_workspace()