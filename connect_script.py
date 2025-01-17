#!/usr/bin/env python3

import paramiko
import argparse
import os
import sys

def parse_args():
    parser = argparse.ArgumentParser(description='Remote Data Extraction Tool')
    parser.add_argument('--host', required=True, help='Remote host IP address')
    parser.add_argument('--username', required=True, help='SSH username')
    parser.add_argument('--password', help='SSH password (not recommended, use SSH key instead)')
    parser.add_argument('--key-file', help='Path to SSH private key file')
    parser.add_argument('--remote-path', required=True, help='Remote path for script execution')
    parser.add_argument('--local-script', required=True, help='Local path of execute.py')
    parser.add_argument('--remote-output', required=True, help='Remote path of the output file')
    parser.add_argument('--local-output', required=True, help='Local path to save the output file')
    return parser.parse_args()

def main():
    args = parse_args()

    # establish remote connection
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        if args.key_file:
            # Use SSH key authentication
            ssh.connect(
                hostname=args.host,
                username=args.username,
                key_filename=args.key_file
            )
        elif args.password:
            # Use password authentication
            ssh.connect(
                hostname=args.host,
                username=args.username,
                password=args.password
            )
        else:
            raise ValueError("Either password or key-file must be provided")

        sftp = ssh.open_sftp()

        # Transfer script to the remote computer
        sftp.put(args.local_script, args.remote_path)

        # Run the script
        stdin, stdout, stderr = ssh.exec_command(f"python {args.remote_path}")
        
        # Print any errors or output
        print(stdout.read().decode())
        print(stderr.read().decode(), file=sys.stderr)

        # Get the output file
        sftp.get(args.remote_output, args.local_output)

        # close connection
        sftp.close()
        ssh.close()

    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
