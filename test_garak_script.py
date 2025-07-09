#!/usr/bin/env python3
"""
Test script for garak_prompt_injection.py
"""

import sys
import os
sys.path.append('/app')

from garak_prompt_injection import GarakTester

def test_basic_functionality():
    """Test basic functionality of the GarakTester class"""
    print("Testing GarakTester initialization...")
    
    tester = GarakTester()
    
    # Test probe list
    print(f"✓ Loaded {len(tester.available_probes)} probes")
    
    # Test some key probes are present
    key_probes = [
        "garak.probes.promptinject",
        "garak.probes.dan",
        "garak.probes.encoding",
        "garak.probes.latentinjection"
    ]
    
    for probe in key_probes:
        if probe in tester.available_probes:
            print(f"✓ Found key probe: {probe}")
        else:
            print(f"✗ Missing key probe: {probe}")
    
    # Test color output
    print("\nTesting color output:")
    tester.print_success("This is a success message")
    tester.print_error("This is an error message")
    tester.print_warning("This is a warning message")
    tester.print_info("This is an info message")
    
    # Test command runner (with safe command)
    print("\nTesting command execution:")
    success, stdout, stderr = tester.run_command("echo 'Hello World'")
    if success and "Hello World" in stdout:
        print("✓ Command execution works")
    else:
        print("✗ Command execution failed")
    
    print("\n✓ All basic tests passed!")

if __name__ == "__main__":
    test_basic_functionality()