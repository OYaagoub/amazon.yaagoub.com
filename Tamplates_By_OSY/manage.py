import argparse
import subprocess

# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Add a command argument
parser.add_argument('command', choices=['server-pug', 'server-sass', 'init'], help='Command to execute')

# Add an argument for the project name (used in 'init' command)
parser.add_argument('name_project', help='Name to save as a project name', nargs='?')

# Parse the command-line arguments
args = parser.parse_args()

# Specify the command you want to run
command = [
    'pug ./Packages/pug/pages -o ./Packages/dist/pages -w -P',
    'pug ./Packages/pug/main.pug -w -P',
    'code --install-extension glenn2223.live-sass',
    'git clone --depth 1 --filter=blob:none https://github.com/OYaagoub/OSY.git {0}'
]

# Check the command and execute corresponding actions
if args.command == 'server-sass':
    try:
        # Run the command and capture the output
        subprocess.check_output(command[2], shell=True, encoding='utf-8')
        print("""\n\t--------------------------------------------------------------------
                 \n=>\t Command executed successfully {0} installed .
                 \n=>\t please check the bar bottom and press {0} .
                 \n\t--------------------------------------------------------------------
                 """.format("\'Watch sass\'"))
    except Exception as e:
        print("""\n\t--------------------------------------------------------------------
                 \n=>\t You have a problem on {0}  .
                 \n=>\t please resolve it and start again .
                 \n\t--------------------------------------------------------------------
                 """.format(e))
elif args.command == 'server-pug':
    try:
        # Run the command and capture the output
        print("Don't close this window or stop it")
        print("Running ......")
        subprocess.Popen(command[0], shell=True, encoding='utf-8')
        subprocess.Popen(command[1], shell=True, encoding='utf-8').wait()
    except Exception as e:
        print("""\n\t--------------------------------------------------------------------
                 \n=>\t You have a problem on {0}  .
                 \n=>\t please resolve it and start again .
                 \n\t--------------------------------------------------------------------
                 """.format(e))
elif args.command == 'init':
    try:
        # Run the command and capture the output
        print("Don't close this window or stop it")
        print("Running ......")
        name_project = args.name_project
        subprocess.Popen(command[3].format(name_project), shell=True, encoding='utf-8')
    except Exception as e:
        print("""\n\t--------------------------------------------------------------------
                 \n=>\t You have a problem on {0}  .
                 \n=>\t please resolve it and start again .
                 \n\t--------------------------------------------------------------------
                 """.format(e))

else:
    print("Invalid command.")
