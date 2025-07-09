#!/usr/bin/env python3
"""
Usage example for garak_prompt_injection.py

This script demonstrates how to use the LLM vulnerability scanner
"""

def print_usage_example():
    """Print a comprehensive usage example"""
    
    print("""
🔍 LLM vulnerability scanner - Usage Example
===========================================

This script helps you test LLM models for security vulnerabilities using NVIDIA's garak tool.

📋 Prerequisites:
================
1. Miniconda or Anaconda installed
2. Ollama installed and running
3. Either a .gguf model file or an existing Ollama model

🔧 Setup Instructions:
====================

1. Install Miniconda (if not already installed):
   wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
   bash Miniconda3-latest-Linux-x86_64.sh

2. Install Ollama (if not already installed):
   curl -fsSL https://ollama.ai/install.sh | sh

3. If using .gguf model, have your model file ready:
   - Example: /path/to/your/model.gguf

4. If using existing Ollama model, pull it first:
   ollama pull llama3.1:8b
   ollama pull mistral-nemo:latest

🎯 Running the Scanner:
=====================
python garak_prompt_injection.py

📊 Available Test Probes (32 total):
===================================
Core Vulnerability Probes:
• promptinject - Primary prompt injection tests
• dan - "Do Anything Now" jailbreak attempts
• encoding - Encoding-based injection tests
• latentinjection - Hidden injection tests

Advanced Security Probes:
• exploitation - Code and template injection
• malwaregen - Malware generation attempts
• xss - Cross-site scripting tests
• visual_jailbreak - Visual-based jailbreak attempts

Specialized Attack Probes:
• continuation - Continuation attacks
• suffix - Suffix-based attacks
• grandma - Social engineering tests
• doctor - Professional role exploitation
• ansiescape - ANSI escape sequence attacks
• taptest - TAP (Tree of Attack Prompts) testing
• ...and 18 more specialized probes

💡 Pro Tips:
============
• Start with 'promptinject' for basic vulnerability testing
• Use 'dan' for jailbreak resistance testing
• Use 'all' to run comprehensive security scanning
• Tests can take several minutes to complete
• Reports are automatically opened in your browser
• Results are saved in current directory or ~/.garak/

🔍 Example Test Scenarios:
==========================

Scenario 1: Testing a downloaded .gguf model
============================================
Step 1: Model Selection
- Choose option 1 (LLM model in .gguf format)
- Provide path to your .gguf file
- Give your model a name

Step 2: Environment Setup
- Choose option 1 to create environment
- Script creates conda environment and installs garak

Step 3: Probe Selection
- Select probes (recommend: promptinject, dan, encoding)

Step 4: Test Execution
- Wait for scanning to complete

Step 5: Report Review
- HTML report opens automatically in browser

Scenario 2: Testing an existing Ollama model
============================================
Step 1: Model Selection
- Choose option 2 (Already pulled model in Ollama)
- Select from available models

Step 2: Environment Setup
- Choose option 2 if environment already exists
- Provide environment name

Step 3: Probe Selection
- Select probes for testing

Step 4: Test Execution
- Monitor live scanning progress

Step 5: Report Review
- Review detailed vulnerability report

Scenario 3: Comprehensive Security Audit
=========================================
Step 1: Model Selection
- Use production-ready model

Step 2: Environment Setup
- Use dedicated security testing environment

Step 3: Probe Selection
- Select 'all' for comprehensive testing

Step 4: Test Execution
- Extended scanning time (30+ minutes)

Step 5: Report Review
- Detailed security audit report

🛡️ Security Best Practices:
===========================
• Run tests in isolated environments
• Don't use production models for testing
• Review results with security experts
• Keep test data non-sensitive
• Regular testing for model updates
• Document vulnerability findings
• Monitor for new attack vectors

📈 Understanding Results:
========================
• Green ✓: Test passed (model is secure)
• Red ✗: Test failed (potential vulnerability)
• Yellow ⚠: Warning or attention needed
• Reports show attack success rates
• HTML reports provide detailed analysis
• JSON reports available for automation

🔄 Typical Workflow:
===================
1. Prerequisites Check → Install missing components
2. Model Selection → Choose .gguf or Ollama model
3. Environment Setup → Create or use existing environment
4. Probe Selection → Choose security tests
5. Test Execution → Wait for completion
6. Report Analysis → Review vulnerability findings
7. Security Remediation → Address identified issues
8. Retest → Verify fixes

🆘 Troubleshooting:
==================
• "Conda not found": Add conda to PATH
• "Ollama not found": Install Ollama service
• "Model creation failed": Check file permissions
• "Garak installation failed": Check internet connection
• "Environment not found": Verify environment name
• "No report generated": Check current directory

🚀 Advanced Usage:
==================
• Custom probe combinations for specific threat models
• Automated testing with CI/CD pipelines
• Batch testing multiple models
• Integration with security monitoring systems
• Custom report generation and analysis

Ready to scan your LLM for vulnerabilities? Run the script and follow the 5-step process!
""")

if __name__ == "__main__":
    print_usage_example()