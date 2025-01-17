# Remote Data Extraction Tool

A Python-based tool for securely connecting to remote servers, transferring files, and executing scripts remotely using SSH/SFTP.

## Features

- Secure SSH connection to remote servers
- SFTP file transfer capabilities
- Remote script execution
- Automated file retrieval
- Command-line interface for easy automation

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

The script can be run from the command line with the following arguments:

```bash
python connect_script.py \
    --host REMOTE_HOST \
    --username SSH_USERNAME \
    [--password SSH_PASSWORD | --key-file PATH_TO_SSH_KEY] \
    --remote-path REMOTE_SCRIPT_PATH \
    --local-script PATH_TO_LOCAL_SCRIPT \
    --remote-output REMOTE_OUTPUT_PATH \
    --local-output LOCAL_OUTPUT_PATH
```

### Required Arguments:
- `--host`: Remote host IP address
- `--username`: SSH username
- `--remote-path`: Remote path where the script will be transferred
- `--local-script`: Local path of execute.py
- `--remote-output`: Remote path of the output file to retrieve
- `--local-output`: Local path to save the retrieved output file

### Authentication (one required):
- `--password`: SSH password (not recommended for security)
- `--key-file`: Path to SSH private key file (recommended)

### Example:
```bash
python connect_script.py \
    --host 192.168.1.100 \
    --username admin \
    --key-file ~/.ssh/id_rsa \
    --remote-path /tmp/execute.py \
    --local-script ./execute.py \
    --remote-output /tmp/output.txt \
    --local-output ./output.txt
```

## Security Note

- It's strongly recommended to use SSH keys instead of passwords
- Never commit sensitive credentials to version control
- Consider using environment variables for sensitive information
- Avoid using the --password flag in production environments

## Requirements

- Python 3.x
- Paramiko library (for SSH/SFTP functionality)
