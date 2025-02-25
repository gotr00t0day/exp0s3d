from colorama import Fore, Style
from modules.sub_proc import scan, commands
from nuclei.parser import parse_nuclei_output
from tqdm import tqdm
import os
import requests
import subprocess
import time


banner = fr"""

                      _______         ________      .___
  ____ ___  _________ \   _  \   _____\_____  \   __| _/
_/ __ \\  \/  /\____ \/  /_\  \ /  ___/ _(__  <  / __ | 
\  ___/ >    < |  |_> >  \_/   \\___ \ /       \/ /_/ | 
 \___  >__/\_ \|   __/ \_____  /____  >______  /\____ | 
     \/      \/|__|          \/     \/       \/      \/

     Author:    c0d3Ninja
     Github:    https://github.com/gotr00t0day
     Instagram: https://www.instagram.com/gotr00t0day

"""

def payloads(prompt: str):
    location = os.path.join(os.path.dirname(__file__), "prompts", f"{prompt}.txt")
    with open(location, "r") as file:
        # Join all lines with newlines and escape quotes
        payload = file.read().strip().replace('"', '\\"')
        # Wrap the entire payload in quotes to pass as a single argument
        return f'"{payload}"'

def target_list(file: str):
    with open(file, "r") as file:
        targets = [x.strip() for x in file.readlines()]
    return targets

def run_scan_with_progress(input_file: str, payload: str, scan_type: str):
    print(Fore.CYAN + f"\nStarting {scan_type} scan..." + Style.RESET_ALL)
    
    # Create a progress bar
    with tqdm(total=100, 
             desc="Scanning", 
             bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.GREEN, Fore.RESET)) as pbar:
        # Start the scan
        output = scan(f"nuclei -list {input_file} -ai {payload}")
        
        # Update progress bar (simulated progress)
        for i in range(100):
            time.sleep(0.1)  # Adjust this value to match your actual scan time
            pbar.update(1)
            
    return output

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

while True:
    print(Fore.RED + banner)
    print (Fore.RED + "[" + Fore.CYAN + "0" + Fore.RED + "]" + Fore.WHITE + "  Low Hanging Fruits")
    print (Fore.RED + "[" + Fore.CYAN + "1" + Fore.RED + "]" + Fore.WHITE + "  Sensitive Data Exposure")
    print (Fore.RED + "[" + Fore.CYAN + "2" + Fore.RED + "]" + Fore.WHITE + "  SQL Injection")
    print (Fore.RED + "[" + Fore.CYAN + "3" + Fore.RED + "]" + Fore.WHITE + "  Cross Site Scripting")
    print (Fore.RED + "[" + Fore.CYAN + "4" + Fore.RED + "]" + Fore.WHITE + "  Server Side Request Forgery")
    print (Fore.RED + "[" + Fore.CYAN + "5" + Fore.RED + "]" + Fore.WHITE + "  Local and Remote File Inclusion")
    print (Fore.RED + "[" + Fore.CYAN + "6" + Fore.RED + "]" + Fore.WHITE + "  Command Injection")
    print (Fore.RED + "[" + Fore.CYAN + "7" + Fore.RED + "]" + Fore.WHITE + "  XXE")
    print (Fore.RED + "[" + Fore.CYAN + "8" + Fore.RED + "]" + Fore.WHITE + "  Host Header Injection")
    print (Fore.RED + "[" + Fore.CYAN + "9" + Fore.RED + "]" + Fore.WHITE + "  Cloud Security Issues")
    print (Fore.RED + "[" + Fore.CYAN + "10" + Fore.RED + "]" + Fore.WHITE + " Web Cache Poisoning")
    print (Fore.RED + "[" + Fore.CYAN + "X" + Fore.RED + "]" + Fore.WHITE + "  Exit")
    print ("\n")

    prompt = input(Fore.WHITE + "exp0s3d~" +  Fore.WHITE + "# ")

    if prompt == "0":
        print(Fore.WHITE + "Running Low Hanging Fruits.. \n")
        low_hanging_fruits()
    elif prompt == "1":
        print(Fore.WHITE + "Running Sensitive Data Exposure.. \n")
        sensitive_data_exposure()
    elif prompt == "2":
        print(Fore.WHITE + "Running SQL Injection.. \n")
        sql_injection()
    elif prompt == "3":
        print(Fore.WHITE + "Running Cross Site Scripting.. \n")
        cross_site_scripting()
    elif prompt == "4":
        print(Fore.WHITE + "Running Server Side Request Forgery.. \n")
        server_side_request_forgery()
    elif prompt == "5":
        print(Fore.WHITE + "Running Local and Remote File Inclusion.. \n")
        local_and_remote_file_inclusion()
    elif prompt == "6":
        print(Fore.WHITE + "Running Command Injection.. \n")
        command_injection()
    elif prompt == "7":
        print(Fore.WHITE + "Running XXE.. \n")
        xxe()
    elif prompt == "8":
        print(Fore.WHITE + "Running Host Header Injection.. \n")
        host_header_injection()
    elif prompt == "9":
        print(Fore.WHITE + "Running Cloud Security Issues.. \n")
        cloud_security_issues()
    elif prompt == "10":
        print(Fore.WHITE + "Running Web Cache Poisoning.. \n")
        web_cache_poisoning()
    elif prompt == "X" or prompt == "x" or prompt == "exit" or prompt == "quit":
        break
    else:
        print(Fore.RED + "Invalid option")
        
        