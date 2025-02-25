from colorama import Fore, Style
import subprocess

def scan(command: str):
    try:
        # Split the command but preserve the quoted payload
        parts = []
        in_quotes = False
        current_part = ''
        
        for char in command:
            if char == '"':
                in_quotes = not in_quotes
                current_part += char
            elif char.isspace() and not in_quotes:
                if current_part:
                    parts.append(current_part)
                current_part = ''
            else:
                current_part += char
        
        if current_part:
            parts.append(current_part)
            
        # Run the command with the properly split arguments
        process = subprocess.run(
            parts,
            capture_output=True,
            text=True
        )
        return process.stdout
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error executing command: {e.output}{Style.RESET_ALL}")
        return ""

def commands(cmd):
    try:
        subprocess.check_call(cmd, shell=True)
    except:
        pass