#!/usr/bin/env python3

import sys
import re
import subprocess
import io


IGNORED_FUNCTIONS = [
    'sys_port_backtrace',
    'sys_backtrace',
    'print_backtrace',
    'print_assert_backtrace',
    'print_read_backtrace',
    'print_write_backtrace',
    'mock_entry_create_write_backtrace',
    'mock_entry_print_write_backtrace',
    'create_mock_entry',
    'read_mock_entry',
    'harness_mock_assert',
    'harness_mock_read',
    'harness_mock_write',
    'harness_mock_mwrite',
    'harness_mock_cwrite',
    'harness_mock_write_notify',
    'harness_mock_read_wait',
    '??',
    '_start'
]

RE_BACKTRACE_ADDRESS = re.compile(r'^(: )(0x[0-9a-f]+)')
RE_BACKTRACE_HEADER = re.compile(
    r'^(Backtrace|Mock \w+ backtrace) \(most recent call first\):')


def print_backtrace_lines(backtrace_lines):
    depth = 0

    for backtrace_line in backtrace_lines:
        function = backtrace_line.split(' ')[1]

        if function not in IGNORED_FUNCTIONS:
            print('[{}]{}'.format(depth, backtrace_line), end='')
            depth += 1


def main():
    program_name = sys.argv[1]
    cross_compile = sys.argv[2]

    backtrace_lines = None
    stdin = io.TextIOWrapper(sys.stdin.buffer,
                             encoding='utf-8',
                             errors='ignore')

    for line in stdin:
        if backtrace_lines is None:
            # Look for a backtrace header.
            mo = RE_BACKTRACE_HEADER.match(line)

            if mo:
                backtrace_lines = []

            print(line, end='')
        else:
            # Look for a backtrace address.
            mo = RE_BACKTRACE_ADDRESS.match(line)

            if mo:
                line = mo.group(1)
                address = mo.group(2)
                command = [
                    cross_compile + 'addr2line',
                    '-f',
                    '-p',
                    '-e', program_name,
                    address
                ]
                line += subprocess.check_output(command).decode('utf-8')
                backtrace_lines.append(line)
            else:
                print_backtrace_lines(backtrace_lines)
                print(line, end='')
                backtrace_lines = None

    if backtrace_lines is not None:
        print_backtrace_lines(backtrace_lines)


if __name__ == '__main__':
    main()
