from colorama import Fore, Style
from modules.sub_proc import scan, commands
from nuclei.parser import parse_nuclei_output
from tqdm import tqdm
import os
import requests
import subprocess
import time
from modules.report_generator import ReportGenerator
from packaging import version


banner = fr"""

                      _______         ________      .___
  ____ ___  _________ \   _  \   _____\_____  \   __| _/
_/ __ \\  \/  /\____ \/  /_\  \ /  ___/ _(__  <  / __ | 
\  ___/ >    < |  |_> >  \_/   \\___ \ /       \/ /_/ | 
 \___  >__/\_ \|   __/ \_____  /____  >______  /\____ | 
     \/      \/|__|          \/     \/       \/      \/
                                                {Fore.YELLOW}v1.2

     Author:    c0d3Ninja
     Github:    https://github.com/gotr00t0day
     Instagram: https://www.instagram.com/gotr00t0day

"""

def payloads(prompt: str):
    location = os.path.join(os.path.dirname(__file__), "prompts", f"{prompt}.txt")
    with open(location, "r") as file:
        # Take the first prompt from the file and properly escape it
        payload = file.readline().strip().replace('"', '\\"')
        return f'"{payload}"'

def target_list(file: str):
    try:
        with open(file, "r") as file:
            targets = [x.strip() for x in file.readlines()]
        return targets
    except Exception as e:
        print(Fore.RED + f"Error reading target list file: {str(e)}")
        start()

def run_scan_with_progress(input_file: str, payload: str, scan_type: str):
    print(Fore.CYAN + f"\nStarting {scan_type} scan..." + Style.RESET_ALL)
    
    with tqdm(total=100, 
             desc="Scanning", 
             bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.GREEN, Fore.RESET)) as pbar:
        output = scan(f"nuclei -list {input_file} -ai {payload} -silent")
        
        for i in range(100):
            time.sleep(0.1)
            pbar.update(1)
    
    if output:
        results = parse_nuclei_output(output)
        report_gen = ReportGenerator()
        report_gen.generate_report(results, scan_type, ["html", "json", "csv"])
        return output  # Return output for further use if needed
    return None

def emails():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("emails")
    output = run_scan_with_progress(input_file, payload, "Emails")
    if not output:
        print(Fore.RED + "No results found")

def low_hanging_fruits():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("lowhangingfruits")
    output = run_scan_with_progress(input_file, payload, "Low Hanging Fruits")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)


def sensitive_data_exposure():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("sensitivedataexposure")
    output = run_scan_with_progress(input_file, payload, "Sensitive Data Exposure")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def sql_injection():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("sqli")
    output = run_scan_with_progress(input_file, payload, "SQL Injection")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def cross_site_scripting():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("xss")
    output = run_scan_with_progress(input_file, payload, "Cross Site Scripting")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def server_side_request_forgery():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("ssrf")
    output = run_scan_with_progress(input_file, payload, "Server Side Request Forgery")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def local_and_remote_file_inclusion():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("fileinclusion")
    output = run_scan_with_progress(input_file, payload, "Local and Remote File Inclusion")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def command_injection():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("commandinjection")
    output = run_scan_with_progress(input_file, payload, "Command Injection")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def xxe():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("xxe")
    output = run_scan_with_progress(input_file, payload, "XXE")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def host_header_injection():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("hostheaderinjection")
    output = run_scan_with_progress(input_file, payload, "Host Header Injection")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def cloud_security_issues():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("cloudsecurity")
    output = run_scan_with_progress(input_file, payload, "Cloud Security Issues")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def web_cache_poisoning():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("webcachepoisoning")
    output = run_scan_with_progress(input_file, payload, "Web Cache Poisoning")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def security_misconfigurations():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("securitymisconfig")
    output = run_scan_with_progress(input_file, payload, "Security Misconfigurations")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def hardcoded_credentials():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("hardcodedcredentials")
    output = run_scan_with_progress(input_file, payload, "Hardcoded Credentials")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def check_for_updates():
    try:
        print(Fore.CYAN + "\nChecking for updates..." + Style.RESET_ALL)
        # Get the latest commit information instead of releases
        response = requests.get("https://api.github.com/repos/gotr00t0day/exp0s3d/commits/main")
        if response.status_code == 200:
            latest_commit = response.json()['sha'][:7]  # Get first 7 chars of commit hash
            
            # Check if there are local changes
            local_changes = subprocess.run(
                ["git", "rev-parse", "HEAD"], 
                capture_output=True, 
                text=True
            ).stdout.strip()[:7]
            
            if latest_commit != local_changes:
                print(Fore.YELLOW + f"\nNew updates are available!")
                update = input(Fore.WHITE + "Would you like to update? (y/n): ").lower()
                
                if update == 'y':
                    print(Fore.CYAN + "\nUpdating exp0s3d..." + Style.RESET_ALL)
                    subprocess.run(["git", "pull", "origin", "main"], check=True)
                    print(Fore.GREEN + "\nUpdate successful! Please restart exp0s3d." + Style.RESET_ALL)
                    exit(0)
            else:
                print(Fore.GREEN + "\nYou're running the latest version!" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"\nError checking for updates: {str(e)}" + Style.RESET_ALL)

def deserialization():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("deserialization")
    output = run_scan_with_progress(input_file, payload, "Deserialization")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def idor():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("idor")
    output = run_scan_with_progress(input_file, payload, "IDOR")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def race_condition():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("racecondition")
    output = run_scan_with_progress(input_file, payload, "Race Condition")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def websocket():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("websocket")
    output = run_scan_with_progress(input_file, payload, "WebSocket")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def start():
    while True:
        print(Fore.RED + banner)
        print (Fore.RED + "[" + Fore.CYAN + "*" + Fore.RED + "]" + Fore.WHITE + "  Check for Updates\n")
        print (Fore.RED + "[" + Fore.CYAN + "0" + Fore.RED + "]" + Fore.WHITE + "  Low Hanging Fruits\t\t\t" + Fore.RED + "[" + Fore.CYAN + "11" + Fore.RED + "]" + Fore.WHITE + " Emails")
        print (Fore.RED + "[" + Fore.CYAN + "1" + Fore.RED + "]" + Fore.WHITE + "  Sensitive Data Exposure\t\t" + Fore.RED + "[" + Fore.CYAN + "12" + Fore.RED + "]" + Fore.WHITE + " Security Misconfigurations")
        print (Fore.RED + "[" + Fore.CYAN + "2" + Fore.RED + "]" + Fore.WHITE + "  SQL Injection\t\t\t" + Fore.RED + "[" + Fore.CYAN + "13" + Fore.RED + "]" + Fore.WHITE + " Hardcoded Credentials")
        print (Fore.RED + "[" + Fore.CYAN + "3" + Fore.RED + "]" + Fore.WHITE + "  Cross Site Scripting\t\t" + Fore.RED + "[" + Fore.CYAN + "14" + Fore.RED + "]" + Fore.WHITE + " Deserialization")
        print (Fore.RED + "[" + Fore.CYAN + "4" + Fore.RED + "]" + Fore.WHITE + "  Server Side Request Forgery\t" + Fore.RED + "[" + Fore.CYAN + "15" + Fore.RED + "]" + Fore.WHITE + " WebSocket")
        print (Fore.RED + "[" + Fore.CYAN + "5" + Fore.RED + "]" + Fore.WHITE + "  File Inclusion\t\t\t" + Fore.RED + "[" + Fore.CYAN + "16" + Fore.RED + "]" + Fore.WHITE + " IDOR")
        print (Fore.RED + "[" + Fore.CYAN + "6" + Fore.RED + "]" + Fore.WHITE + "  Command Injection\t\t\t" + Fore.RED + "[" + Fore.CYAN + "17" + Fore.RED + "]" + Fore.WHITE + " Race Condition")
        print (Fore.RED + "[" + Fore.CYAN + "7" + Fore.RED + "]" + Fore.WHITE + "  XML External Entity")
        print (Fore.RED + "[" + Fore.CYAN + "8" + Fore.RED + "]" + Fore.WHITE + "  Host Header Injection")
        print (Fore.RED + "[" + Fore.CYAN + "9" + Fore.RED + "]" + Fore.WHITE + "  Cloud Security Issues")
        print (Fore.RED + "[" + Fore.CYAN + "10" + Fore.RED + "]" + Fore.WHITE + " Web Cache Poisoning")

        print (Fore.RED + "[" + Fore.CYAN + "X" + Fore.RED + "]" + Fore.WHITE + "  Exit")
        print ("\n")

        prompt = input(Fore.WHITE + "exp0s3d~" +  Fore.WHITE + "# ")

        if prompt == "0":
            low_hanging_fruits()
        elif prompt == "1":
            sensitive_data_exposure()
        elif prompt == "2":
            sql_injection()
        elif prompt == "3":
            cross_site_scripting()
        elif prompt == "4":
            server_side_request_forgery()
        elif prompt == "5":
            local_and_remote_file_inclusion()
        elif prompt == "6":
            command_injection()
        elif prompt == "7":
            xxe()
        elif prompt == "8":
            host_header_injection()
        elif prompt == "9":
            cloud_security_issues()
        elif prompt == "10":
            web_cache_poisoning()
        elif prompt == "11":
            emails()
        elif prompt == "12":
            security_misconfigurations()
        elif prompt == "13":
            hardcoded_credentials()
        elif prompt == "14":
            deserialization()
        elif prompt == "15":
            idor()
        elif prompt == "16":
            race_condition()
        elif prompt == "17":
            websocket()
        elif prompt == "*":
            check_for_updates()
        elif prompt == "X" or prompt == "x" or prompt == "exit" or prompt == "quit":
            break
        else:
            print(Fore.RED + "Invalid option")

if __name__ == "__main__":
    start()
        
        
