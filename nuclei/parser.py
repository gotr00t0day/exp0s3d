from colorama import Fore, Style
import json
from datetime import datetime

def parse_nuclei_output(command_output: str):
    results = []
    
    for line in command_output.splitlines():
        try:
            # Handle both JSON and non-JSON outputs
            if line.startswith("["):
                # Parse non-JSON format (e.g., [extract-emails-webpages] [http] [info])
                parts = line.split("] [")
                if len(parts) >= 2:
                    template_id = parts[0].strip("[")
                    severity = "info"  # Default severity
                    for part in parts:
                        if part.lower() in ["critical", "high", "medium", "low", "info"]:
                            severity = part.lower()
                    
                    url = line.split("] ")[-1].split(" [")[0]
                    description = line.split("] ")[-1].split(" [")[-1].strip('[""]')
                    
                    finding = {
                        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        "template": template_id,
                        "severity": severity,
                        "host": url,
                        "matched": url,
                        "type": parts[1].strip("]") if len(parts) > 1 else "unknown",
                        "matcher_name": "pattern_match",
                        "title": template_id,
                        "url": url,
                        "description": description,
                        "remediation": ""  # Can be populated based on template_id
                    }
                    results.append(finding)
                    
                    # Print formatted output
                    severity_colors = {
                        'critical': Fore.RED,
                        'high': Fore.LIGHTRED_EX,
                        'medium': Fore.YELLOW,
                        'low': Fore.GREEN,
                        'info': Fore.BLUE,
                        'unknown': Fore.WHITE
                    }
                    
                    print(f"\n{'-'*60}")
                    print(f"{Fore.CYAN}[*] Timestamp:{Fore.WHITE} {finding['timestamp']}")
                    print(f"{Fore.CYAN}[*] Template:{Fore.WHITE} {finding['template']}")
                    print(f"{Fore.CYAN}[*] Severity:{severity_colors[finding['severity'].lower()]} {finding['severity']}{Fore.WHITE}")
                    print(f"{Fore.CYAN}[*] Host:{Fore.WHITE} {finding['host']}")
                    print(f"{Fore.CYAN}[*] Matched At:{Fore.WHITE} {finding['matched']}")
                    print(f"{Fore.CYAN}[*] Type:{Fore.WHITE} {finding['type']}")
                    print(f"{Fore.CYAN}[*] Description:{Fore.WHITE} {finding['description']}")
            
            else:
                try:
                    # Try to parse as JSON
                    data = json.loads(line)
                    finding = {
                        'timestamp': datetime.fromisoformat(data.get('timestamp', '')).strftime('%Y-%m-%d %H:%M:%S'),
                        'template': data.get('template-id', 'N/A'),
                        'severity': data.get('info', {}).get('severity', 'N/A'),
                        'host': data.get('host', 'N/A'),
                        'matched': data.get('matched-at', 'N/A'),
                        'type': data.get('type', 'N/A'),
                        'matcher_name': data.get('matcher-name', 'N/A'),
                        'title': data.get('info', {}).get('name', data.get('template-id', 'N/A')),
                        'url': data.get('host', 'N/A'),
                        'description': data.get('info', {}).get('description', 'N/A'),
                        'remediation': data.get('info', {}).get('remediation', '')
                    }
                    results.append(finding)
                    
                    # Print formatted output
                    severity_colors = {
                        'critical': Fore.RED,
                        'high': Fore.LIGHTRED_EX,
                        'medium': Fore.YELLOW,
                        'low': Fore.GREEN,
                        'info': Fore.BLUE,
                        'N/A': Fore.WHITE
                    }
                    
                    print(f"\n{'-'*60}")
                    print(f"{Fore.CYAN}[*] Timestamp:{Fore.WHITE} {finding['timestamp']}")
                    print(f"{Fore.CYAN}[*] Template:{Fore.WHITE} {finding['template']}")
                    print(f"{Fore.CYAN}[*] Severity:{severity_colors[finding['severity'].lower()]} {finding['severity']}{Fore.WHITE}")
                    print(f"{Fore.CYAN}[*] Host:{Fore.WHITE} {finding['host']}")
                    print(f"{Fore.CYAN}[*] Matched At:{Fore.WHITE} {finding['matched']}")
                    print(f"{Fore.CYAN}[*] Type:{Fore.WHITE} {finding['type']}")
                    if finding['description'] != 'N/A':
                        print(f"{Fore.CYAN}[*] Description:{Fore.WHITE} {finding['description']}")
                
                except json.JSONDecodeError:
                    # Handle non-JSON lines (progress updates, etc.)
                    if line.strip():
                        print(f"{Fore.WHITE}{line}")
                        
        except Exception as e:
            print(f"{Fore.RED}Error parsing line: {e}{Style.RESET_ALL}")
            continue
    
    return results
