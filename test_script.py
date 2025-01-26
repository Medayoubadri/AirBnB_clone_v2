#!/usr/bin/python3
"""
Test script for 100-clean_web_static.py
"""

import os
import shutil
from fabric.api import local, settings, hide
import time

def create_test_archives(count, prefix='web_static_'):
    """Create test archives"""
    test_dir = './versions'
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    for i in range(count):
        filename = f"{prefix}{int(time.time())}.tgz"
        with open(os.path.join(test_dir, filename), 'w') as f:
            f.write('test content')
        time.sleep(0.1)  # Ensure unique timestamps

def count_archives(prefix='web_static_'):
    """Count archives"""
    test_dir = './versions'
    return len([f for f in os.listdir(test_dir) if f.startswith(prefix) and f.endswith('.tgz')])

def run_test(number, initial_count):
    """Run a single test"""
    print(f"Testing: number = {number}, {initial_count} archives")
    create_test_archives(initial_count)
    
    with settings(warn_only=True), hide('everything'):
        local(f"python3 100-clean_web_static.py {number}")
    
    remaining_count = count_archives()
    expected_count = min(number if number > 0 else 1, initial_count)
    
    print(f"Remaining archives: {remaining_count}")
    print(f"Expected remaining: {expected_count}")
    print("PASS" if remaining_count == expected_count else "FAIL")
    print("---")

    # Clean up
    shutil.rmtree('./versions')

# Run test cases
run_test(0, 1)  # number = 0, 1 archive
run_test(0, 2)  # number = 0, 2 archives
run_test(4, 5)  # number = 4, 5 archives
run_test(3, 5)  # number = 3, 5 archives
run_test(4, 2)  # number = 4, 2 archives
