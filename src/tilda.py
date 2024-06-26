# src/tilda.py

import argparse
import sys
import logging

from src.config import commands

def configure_parser():
    """Configure and return the main argument parser with subparsers for commands."""
    parser = argparse.ArgumentParser(description="~tilda - The AI CLI")
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument('--careless', action='store_true', help="Execute the command without explicit approval.")
    
    # Subparser setup
    subparsers = parser.add_subparsers(dest='subcommand', required=True, help='Sub-command help')

    for cmd, cmd_opts in commands.items():
        sub_parser = subparsers.add_parser(cmd, parents=[parent_parser], help=cmd_opts['help'])
        # Add command-specific arguments
        for arg, arg_opts in cmd_opts.get('args', {}).items():
            sub_parser.add_argument(arg, help=arg_opts['help'])

    return parser

def main():
    parser = configure_parser()
    args = parser.parse_args()

    # Call the corresponding function based on the subcommand
    if args.subcommand:
        commands[args.subcommand]['function'](args)
    else:
        logging.error("Unknown command")
        sys.exit(1)

if __name__ == '__main__':
    main()