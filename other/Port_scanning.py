import subprocess

def run_nmap_scan(target, options="-sV"):
    try:
        # Construct the Nmap command
        nmap_command = f"nmap {options} {target}"

        # Run the Nmap scan and capture the output
        scan_result = subprocess.check_output(nmap_command, shell=True, text=True)

        # Print the scan result
        print(scan_result)
    
    except subprocess.CalledProcessError as e:
        print(f"Error running Nmap: {e}")

if __name__ == "__main__":
    target = "your_target_ip_or_hostname"
    options = "-p 1-65535 -T4 -A -v --script vuln -Pn"  # Customize the Nmap options as needed

    run_nmap_scan(target, options)
