from colorama import Fore, Style
import json
from datetime import datetime

def parse_nuclei_output(command_output: str):
    results = []
    
    for line in command_output.splitlines():
        try:
            # Nuclei outputs JSON lines for findings
            data = json.loads(line)
            
            # Extract relevant information
            finding = {
                'timestamp': datetime.fromisoformat(data.get('timestamp', '')).strftime('%Y-%m-%d %H:%M:%S'),
                'template': data.get('template-id', 'N/A'),
                'severity': data.get('info', {}).get('severity', 'N/A'),
                'host': data.get('host', 'N/A'),
                'matched': data.get('matched-at', 'N/A'),
                'type': data.get('type', 'N/A'),
                'matcher_name': data.get('matcher-name', 'N/A')
            }
            
            # Color-code severity
            severity_colors = {
                'critical': Fore.RED,
                'high': Fore.LIGHTRED_EX,
                'medium': Fore.YELLOW,
                'low': Fore.GREEN,
                'info': Fore.BLUE,
                'N/A': Fore.WHITE
            }
            
            # Print formatted output
            print(f"\n{'-'*60}")
            print(f"{Fore.CYAN}[*] Timestamp:{Fore.WHITE} {finding['timestamp']}")
            print(f"{Fore.CYAN}[*] Template:{Fore.WHITE} {finding['template']}")
            print(f"{Fore.CYAN}[*] Severity:{severity_colors[finding['severity'].lower()]} {finding['severity']}{Fore.WHITE}")
            print(f"{Fore.CYAN}[*] Host:{Fore.WHITE} {finding['host']}")
            print(f"{Fore.CYAN}[*] Matched At:{Fore.WHITE} {finding['matched']}")
            print(f"{Fore.CYAN}[*] Type:{Fore.WHITE} {finding['type']}")
            print(f"{Fore.CYAN}[*] Matcher:{Fore.WHITE} {finding['matcher_name']}")
            
            results.append(finding)
            
        except json.JSONDecodeError:
            # Handle non-JSON lines (progress updates, etc.)
            if line.strip():
                print(f"{Fore.WHITE}{line}")
    
    return results