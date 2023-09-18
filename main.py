import webbrowser
from time import sleep
import os
import subprocess

R = '\033[1;31m'  # Red 
B = '\033[2;36m'  # Blue 
G = "\033[1;32m"  # Green 
Y = "\033[1;33m"  # Yellow 
DB = "\033[1;34m"  # Dark Blue 
P = "\033[1;35m"  # Purple 
W = "\033[1;37m"  # White 

count = 0
sheep = 0
def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def visit_website(num_times):
    global count, sheep
    for _ in range(num_times):
        open_readme_in_browser()
        count += 1
        xd(count, sheep)
        
        if count % 25 == 0:
            close_browser()
            sheep += 1
            xd(count, sheep)
            sleep(5)
            
        sleep(2)
    else:
        print("Visited the website specified number of times.")

def xd(count, sheep): 
    os.system('cls') 
    print(f"{DB}──────────────────") 
    print(f"{Y}Visits : {G}{count}")
    print(f"{Y}Cycles : {P}{sheep}") 
    print(f"{DB}──────────────────") 

def open_readme_in_browser():
    url = "https://github.com/sankalpkarn/sankalpkarn/blob/main/README.md"
    webbrowser.open(url)

def close_browser():
    if os.name == 'nt':
        try:
            # Use the PowerShell command to close Edge browser
            subprocess.run(["powershell", "Stop-Process -Name msedge -Force"])
        except Exception as e:
            print("Error while closing the browser:", e)
    else:
        print("Closing browser feature is currently supported only on Windows.")

try:
    num_times = int(input("Enter the number of times to visit the website: "))
    visit_website(num_times)
except ValueError:
    print("Invalid input. Please enter a valid number.")
