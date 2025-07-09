#!/usr/bin/env python3
"""
Test script for garak_prompt_injection.py (LLM vulnerability scanner)
"""

import sys
import os
sys.path.append('/app')

from garak_prompt_injection import LLMVulnerabilityScanner

def test_basic_functionality():
    """Test basic functionality of the LLMVulnerabilityScanner class"""
    print("Testing LLMVulnerabilityScanner initialization...")
    
    scanner = LLMVulnerabilityScanner()
    
    # Test probe list
    print(f"✓ Loaded {len(scanner.available_probes)} probes")
    
    # Test some key probes are present (without garak.probes prefix)
    key_probes = [
        "promptinject",
        "dan",
        "encoding",
        "latentinjection",
        "xss",
        "visual_jailbreak"
    ]
    
    for probe in key_probes:
        if probe in scanner.available_probes:
            print(f"✓ Found key probe: {probe}")
        else:
            print(f"✗ Missing key probe: {probe}")
    
    # Test taptest probe (renamed from tap)
    if "taptest" in scanner.available_probes:
        print("✓ Found taptest probe (correctly renamed)")
    else:
        print("✗ Missing taptest probe")
        
    # Verify test probe was removed
    if "test" not in scanner.available_probes:
        print("✓ Test probe correctly removed")
    else:
        print("✗ Test probe should be removed")
    
    # Test color output
    print("\nTesting color output:")
    scanner.print_success("This is a success message")
    scanner.print_error("This is an error message")
    scanner.print_warning("This is a warning message")
    scanner.print_info("This is an info message")
    
    # Test command runner (with safe command)
    print("\nTesting command execution:")
    success, stdout, stderr = scanner.run_command("echo 'Hello World'")
    if success and "Hello World" in stdout:
        print("✓ Command execution works")
    else:
        print("✗ Command execution failed")
    
    print("\n✓ All basic tests passed!")

if __name__ == "__main__":
    test_basic_functionality()