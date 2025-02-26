from jinja2 import Template
import json
import csv
from datetime import datetime
import os
from colorama import Fore, Style

class ReportGenerator:
    def __init__(self):
        self.output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports")
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_report(self, scan_results, scan_type, output_formats=["html", "json"]):
        """
        Generate scan reports in multiple formats
        Args:
            scan_results: The results from the scan
            scan_type: Type of scan performed
            output_formats: List of desired output formats (html, json, csv)
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_filename = f"{scan_type}_{timestamp}"
        
        for format in output_formats:
            if format.lower() == "html":
                self.generate_html_report(scan_results, scan_type, base_filename)
            elif format.lower() == "json":
                self.generate_json_report(scan_results, base_filename)
            elif format.lower() == "csv":
                self.generate_csv_report(scan_results, base_filename)
        
        print(Fore.GREEN + f"\nReports generated in {self.output_dir}" + Style.RESET_ALL)

    def generate_html_report(self, results, scan_type, filename):
        """Generate a detailed HTML report"""
        # Process results if they're in string format
        if isinstance(results, str):
            results = [
                {
                    "title": line.split("] [")[0].split("[")[-1],
                    "severity": line.split("] [")[1],
                    "url": line.split("] ")[-1].split(" [")[0],
                    "description": line.split("] ")[-1].split(" [")[-1].strip('[""]'),
                    "remediation": ""  # Add remediation if available
                }
                for line in results.strip().split("\n")
                if line.strip()
            ]
        
        # Count findings by severity
        severity_counts = {
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0,
            "info": 0
        }
        
        for result in results:
            severity = result.get("severity", "info").lower()
            if severity in severity_counts:
                severity_counts[severity] += 1

        template = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>exp0s3d Scan Report</title>
            <style>
                body { 
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 20px;
                    background: #f5f5f5;
                }
                .container {
                    max-width: 1200px;
                    margin: 0 auto;
                    background: white;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                }
                .header {
                    text-align: center;
                    padding: 20px;
                    background: #1a1a1a;
                    color: white;
                    border-radius: 5px;
                    margin-bottom: 20px;
                }
                .vulnerability {
                    margin: 20px 0;
                    padding: 15px;
                    border-radius: 5px;
                    border: 1px solid #ddd;
                }
                .critical { border-left: 5px solid #dc3545; }
                .high { border-left: 5px solid #ff4444; }
                .medium { border-left: 5px solid #ffbb33; }
                .low { border-left: 5px solid #00C851; }
                .info { border-left: 5px solid #33b5e5; }
                .summary {
                    background: #f8f9fa;
                    padding: 15px;
                    border-radius: 5px;
                    margin: 20px 0;
                }
                .stats {
                    display: flex;
                    justify-content: space-around;
                    margin: 20px 0;
                }
                .stat-box {
                    text-align: center;
                    padding: 10px;
                    border-radius: 5px;
                    min-width: 100px;
                }
                .stat-critical { background-color: #dc3545; color: white; }
                .stat-high { background-color: #ff4444; color: white; }
                .stat-medium { background-color: #ffbb33; color: black; }
                .stat-low { background-color: #00C851; color: white; }
                .stat-info { background-color: #33b5e5; color: white; }
                table {
                    width: 100%;
                    border-collapse: collapse;
                    margin: 10px 0;
                }
                th, td {
                    padding: 8px;
                    border: 1px solid #ddd;
                    text-align: left;
                }
                th {
                    background-color: #f8f9fa;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>exp0s3d Scan Report</h1>
                    <p>Scan Type: {{ scan_type }}</p>
                    <p>Generated: {{ date }}</p>
                </div>
                
                <div class="summary">
                    <h2>Summary</h2>
                    <div class="stats">
                        <div class="stat-box stat-critical">
                            <h3>Critical</h3>
                            <p>{{ severity_counts.critical }}</p>
                        </div>
                        <div class="stat-box stat-high">
                            <h3>High</h3>
                            <p>{{ severity_counts.high }}</p>
                        </div>
                        <div class="stat-box stat-medium">
                            <h3>Medium</h3>
                            <p>{{ severity_counts.medium }}</p>
                        </div>
                        <div class="stat-box stat-low">
                            <h3>Low</h3>
                            <p>{{ severity_counts.low }}</p>
                        </div>
                        <div class="stat-box stat-info">
                            <h3>Info</h3>
                            <p>{{ severity_counts.info }}</p>
                        </div>
                    </div>
                    <p>Total Findings: {{ results|length }}</p>
                    <p>Scan Duration: {{ duration }}</p>
                </div>

                <h2>Detailed Findings</h2>
                {% for result in results %}
                <div class="vulnerability {{ result.severity|lower }}">
                    <h3>{{ result.title }}</h3>
                    <table>
                        <tr>
                            <th>Severity</th>
                            <td>{{ result.severity }}</td>
                        </tr>
                        <tr>
                            <th>URL</th>
                            <td>{{ result.url }}</td>
                        </tr>
                        <tr>
                            <th>Description</th>
                            <td>{{ result.description }}</td>
                        </tr>
                        {% if result.remediation %}
                        <tr>
                            <th>Remediation</th>
                            <td>{{ result.remediation }}</td>
                        </tr>
                        {% endif %}
                    </table>
                </div>
                {% endfor %}
            </div>
        </body>
        </html>
        """
        
        report = Template(template).render(
            date=datetime.now().strftime("%Y-%m-%d %H:%M"),
            results=results,
            scan_type=scan_type,
            duration="N/A",  # You can add actual duration if you track it
            severity_counts=severity_counts
        )
        
        output_file = os.path.join(self.output_dir, f"{filename}.html")
        with open(output_file, "w") as f:
            f.write(report)

    def generate_json_report(self, results, filename):
        """Generate a JSON report"""
        output_file = os.path.join(self.output_dir, f"{filename}.json")
        report_data = {
            "timestamp": datetime.now().isoformat(),
            "results": results
        }
        with open(output_file, "w") as f:
            json.dump(report_data, f, indent=4)

    def generate_csv_report(self, results, filename):
        """Generate a CSV report"""
        output_file = os.path.join(self.output_dir, f"{filename}.csv")
        with open(output_file, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Title", "Severity", "URL", "Description", "Remediation"])
            for result in results:
                writer.writerow([
                    result.get("title", ""),
                    result.get("severity", ""),
                    result.get("url", ""),
                    result.get("description", ""),
                    result.get("remediation", "")
                ])