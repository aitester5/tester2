#!/usr/bin/env python3
"""
Usage example for garak_prompt_injection.py

This script demonstrates how to use the Garak Prompt Injection Testing Tool
"""

def print_usage_example():
    """Print a comprehensive usage example"""
    
    print("""
🚀 Garak Prompt Injection Testing Tool - Usage Example
=====================================================

This script helps you test LLM models for prompt injection vulnerabilities using NVIDIA's garak tool.

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

🎯 Running the Tool:
==================
python garak_prompt_injection.py

📊 Available Test Probes:
========================
• garak.probes.promptinject - Primary prompt injection tests
• garak.probes.dan - "Do Anything Now" jailbreak attempts
• garak.probes.encoding - Encoding-based injection tests
• garak.probes.latentinjection - Hidden injection tests
• garak.probes.exploitation - Code and template injection
• garak.probes.malwaregen - Malware generation attempts
• garak.probes.xss - Cross-site scripting tests
• garak.probes.grandma - Social engineering tests
• garak.probes.doctor - Professional role exploitation
• ...and 24 more specialized probes

💡 Pro Tips:
============
• Start with 'garak.probes.promptinject' for basic testing
• Use 'all' to run comprehensive security testing
• Tests can take several minutes to complete
• Reports are automatically opened in your browser
• Results are saved in ~/.garak/ directory

🔍 Example Test Scenarios:
==========================

Scenario 1: Testing a downloaded .gguf model
1. Choose option 1 (LLM model in .gguf format)
2. Provide path to your .gguf file
3. Give your model a name
4. Choose option 1 to create environment
5. Select probes (recommend: promptinject, dan, encoding)
6. Wait for results

Scenario 2: Testing an existing Ollama model
1. Choose option 2 (Already pulled model in Ollama)
2. Select from available models
3. Choose option 2 if environment already exists
4. Select probes for testing
5. Review results

🛡️ Security Best Practices:
===========================
• Run tests in isolated environments
• Don't use production models for testing
• Review results with security experts
• Keep test data non-sensitive
• Regular testing for model updates

📈 Understanding Results:
========================
• Green ✓: Test passed (model is secure)
• Red ✗: Test failed (potential vulnerability)
• Yellow ⚠: Warning or attention needed
• Reports show attack success rates
• HTML reports provide detailed analysis

🆘 Troubleshooting:
==================
• "Conda not found": Add conda to PATH
• "Ollama not found": Install Ollama
• "Model creation failed": Check file permissions
• "Garak installation failed": Check internet connection

Ready to test your LLM's security? Run the script and follow the prompts!
""")

if __name__ == "__main__":
    print_usage_example()