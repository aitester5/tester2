#!/usr/bin/env python3
"""
LLM vulnerability scanner
=========================

This script provides an interactive interface for testing LLM models for vulnerabilities using garak.
It handles model setup with Ollama, conda environment management, and garak execution.

Prerequisites:
- Miniconda/Anaconda installed
- Ollama installed

Usage:
    python garak_prompt_injection.py
"""

import os
import subprocess
import sys
import time
import webbrowser
from pathlib import Path
from typing import List, Optional

class Colors:
    """ANSI color codes for terminal output"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class LLMVulnerabilityScanner:
    def __init__(self):
        self.garak_env = "garak_env"
        self.available_probes = [
            "base",
            "ansiescape",
            "atkgen",
            "audio",
            "av_spam_scanning",
            "continuation",
            "dan",
            "divergence",
            "doctor",
            "donotanswer",
            "encoding",
            "exploitation",
            "fileformats",
            "glitch",
            "goodside",
            "grandma",
            "latentinjection",
            "leakreplay",
            "lmrc",
            "malwaregen",
            "misleading",
            "packagehallucination",
            "phrasing",
            "promptinject",
            "realtoxicityprompts",
            "snowball",
            "suffix",
            "taptest",
            "topic",
            "xss",
            "visual_jailbreak",
            "_tier"
        ]
        
    def print_header(self, text: str):
        """Print a formatted header"""
        print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.ENDC}")
        print(f"{Colors.HEADER}{Colors.BOLD}{text.center(60)}{Colors.ENDC}")
        print(f"{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.ENDC}\n")
        
    def print_success(self, text: str):
        """Print success message"""
        print(f"{Colors.OKGREEN}✓ {text}{Colors.ENDC}")
        
    def print_error(self, text: str):
        """Print error message"""
        print(f"{Colors.FAIL}✗ {text}{Colors.ENDC}")
        
    def print_warning(self, text: str):
        """Print warning message"""
        print(f"{Colors.WARNING}⚠ {text}{Colors.ENDC}")
        
    def print_info(self, text: str):
        """Print info message"""
        print(f"{Colors.OKCYAN}ℹ {text}{Colors.ENDC}")
        
    def run_command(self, command: str, shell: bool = True, capture_output: bool = True) -> tuple:
        """Run a shell command and return result"""
        try:
            if shell:
                result = subprocess.run(command, shell=True, capture_output=capture_output, text=True)
            else:
                result = subprocess.run(command.split(), capture_output=capture_output, text=True)
            return result.returncode == 0, result.stdout, result.stderr
        except Exception as e:
            return False, "", str(e)
            
    def check_prerequisites(self) -> bool:
        """Check if conda and ollama are available"""
        self.print_header("Checking Prerequisites")
        
        # Check conda
        success, _, _ = self.run_command("conda --version")
        if success:
            self.print_success("Conda is installed")
        else:
            self.print_error("Conda is not installed or not in PATH")
            return False
            
        # Check ollama
        success, _, _ = self.run_command("ollama --version")
        if success:
            self.print_success("Ollama is installed")
        else:
            self.print_error("Ollama is not installed or not in PATH")
            return False
            
        return True
        
    def get_user_choice(self, prompt: str, options: List[str]) -> int:
        """Get user choice from a list of options"""
        print(f"\n{Colors.OKCYAN}{prompt}{Colors.ENDC}")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        while True:
            try:
                choice = int(input(f"\n{Colors.BOLD}Enter your choice (1-{len(options)}): {Colors.ENDC}"))
                if 1 <= choice <= len(options):
                    return choice - 1
                else:
                    self.print_error(f"Please enter a number between 1 and {len(options)}")
            except ValueError:
                self.print_error("Please enter a valid number")
                
    def handle_gguf_model(self) -> Optional[str]:
        """Handle .gguf model setup"""
        self.print_header("Setting up .gguf Model")
        
        # Get model file path
        model_path = input(f"{Colors.BOLD}Enter the full path to your .gguf model file: {Colors.ENDC}").strip()
        
        if not os.path.exists(model_path):
            self.print_error(f"Model file not found: {model_path}")
            return None
            
        if not model_path.endswith('.gguf'):
            self.print_error("File must have .gguf extension")
            return None
            
        # Get model name
        model_name = input(f"{Colors.BOLD}Enter a name for your model (will be used with ollama): {Colors.ENDC}").strip()
        if not model_name:
            self.print_error("Model name cannot be empty")
            return None
            
        # Create ModelFile in the same directory as .gguf file
        model_dir = os.path.dirname(model_path)
        model_filename = os.path.basename(model_path)
        modelfile_path = os.path.join(model_dir, "ModelFile")
        
        try:
            with open(modelfile_path, 'w') as f:
                f.write(f"FROM {model_filename}\n")
            self.print_success(f"ModelFile created: {modelfile_path}")
        except Exception as e:
            self.print_error(f"Failed to create ModelFile: {e}")
            return None
            
        # Create ollama model - run from the directory containing the .gguf file
        self.print_info(f"Creating ollama model: {model_name}")
        original_dir = os.getcwd()
        try:
            os.chdir(model_dir)
            success, stdout, stderr = self.run_command(f"ollama create {model_name} -f ModelFile")
            
            if success:
                self.print_success(f"Model '{model_name}' created successfully")
                # List models and ask user to choose
                return self.list_and_choose_model()
            else:
                self.print_error(f"Failed to create model: {stderr}")
                return None
        finally:
            os.chdir(original_dir)
            
    def list_ollama_models(self) -> List[str]:
        """List available ollama models"""
        success, stdout, stderr = self.run_command("ollama list")
        
        if not success:
            self.print_error(f"Failed to list models: {stderr}")
            return []
            
        models = []
        lines = stdout.strip().split('\n')[1:]  # Skip header
        
        for line in lines:
            if line.strip():
                model_name = line.split()[0]
                models.append(model_name)
                
        return models
        
    def list_and_choose_model(self) -> Optional[str]:
        """List available ollama models and ask user to choose"""
        models = self.list_ollama_models()
        if not models:
            self.print_error("No models found in Ollama")
            return None
            
        self.print_info("Available models:")
        for i, model in enumerate(models, 1):
            print(f"{i}. {model}")
            
        while True:
            try:
                model_choice = int(input(f"\n{Colors.BOLD}Select model (1-{len(models)}): {Colors.ENDC}"))
                if 1 <= model_choice <= len(models):
                    return models[model_choice - 1]
                else:
                    self.print_error(f"Please enter a number between 1 and {len(models)}")
            except ValueError:
                self.print_error("Please enter a valid number")
                
    def select_model(self) -> Optional[str]:
        """Select model (either .gguf or existing ollama model)"""
        self.print_header("Step 1: Model Selection")
        
        options = [
            "LLM model in .gguf format",
            "Already pulled model in Ollama"
        ]
        
        choice = self.get_user_choice("Choose your model option:", options)
        
        if choice == 0:
            return self.handle_gguf_model()
        else:
            return self.list_and_choose_model()
            
    def setup_garak_environment(self) -> tuple:
        """Setup conda environment and install garak"""
        self.print_header("Step 2: Garak Environment Setup")
        
        options = [
            "Create an environment and install garak",
            "Already created and garak is installed"
        ]
        
        choice = self.get_user_choice("Choose environment option:", options)
        
        if choice == 0:
            # Create environment
            self.print_info("Creating conda environment...")
            success, stdout, stderr = self.run_command(f"conda create -n {self.garak_env} python=3.12 -y")
            
            if not success:
                self.print_error(f"Failed to create environment: {stderr}")
                return False, self.garak_env
                
            self.print_success("Environment created successfully")
            
            # Install garak
            self.print_info("Installing garak...")
            success, stdout, stderr = self.run_command(f"conda run -n {self.garak_env} pip install garak")
            
            if not success:
                self.print_error(f"Failed to install garak: {stderr}")
                return False, self.garak_env
                
            self.print_success("Garak installed successfully")
            
            # Test garak installation
            self.print_info("Testing garak installation...")
            success, stdout, stderr = self.run_command(f"conda run -n {self.garak_env} garak --help")
            
            if success:
                self.print_success("Garak is working correctly")
                return True, self.garak_env
            else:
                self.print_error(f"Garak test failed: {stderr}")
                return False, self.garak_env
                
        else:
            # Ask for environment name
            env_name = input(f"{Colors.BOLD}Enter the environment name: {Colors.ENDC}").strip()
            if not env_name:
                self.print_error("Environment name cannot be empty")
                return False, ""
                
            # Test garak installation
            self.print_info(f"Testing garak installation in environment: {env_name}")
            success, stdout, stderr = self.run_command(f"conda run -n {env_name} garak --help")
            
            if success:
                self.print_success("Garak is working correctly")
                return True, env_name
            else:
                self.print_error(f"Garak test failed: {stderr}")
                return False, env_name
                
    def select_probes(self) -> List[str]:
        """Select probes for testing"""
        self.print_header("Step 3: Probe Selection")
        
        print(f"{Colors.OKCYAN}Available probes:{Colors.ENDC}")
        for i, probe in enumerate(self.available_probes, 1):
            print(f"{i:2d}. {probe}")
            
        print(f"\n{Colors.WARNING}Enter probe numbers separated by commas (e.g., 1,3,5) or 'all' for all probes:{Colors.ENDC}")
        
        while True:
            selection = input(f"{Colors.BOLD}Your selection: {Colors.ENDC}").strip()
            
            if selection.lower() == 'all':
                return self.available_probes
                
            try:
                indices = [int(x.strip()) for x in selection.split(',')]
                if all(1 <= i <= len(self.available_probes) for i in indices):
                    return [self.available_probes[i-1] for i in indices]
                else:
                    self.print_error(f"Please enter numbers between 1 and {len(self.available_probes)}")
            except ValueError:
                self.print_error("Please enter valid numbers separated by commas")
                
    def run_garak_test(self, model_name: str, probes: List[str], env_name: str) -> Optional[str]:
        """Run garak test with selected model and probes"""
        self.print_header("Step 4: Running Garak Test")
        
        probe_str = ",".join(probes)
        command = f"conda run -n {env_name} python -m garak --model_type ollama --model_name {model_name} --probes {probe_str}"
        
        self.print_info(f"Running command: {command}")
        self.print_warning("Garak is running... This may take several minutes to complete...")
        
        # Run without capturing output so user can see progress
        success, stdout, stderr = self.run_command(command, capture_output=False)
        
        if success:
            self.print_success("Garak test completed successfully!")
            return self.find_latest_report()
        else:
            self.print_error(f"Garak test failed: {stderr}")
            return None
            
    def find_latest_report(self) -> Optional[str]:
        """Find the latest garak report"""
        # First check current directory for reports
        current_dir = Path.cwd()
        html_files = list(current_dir.glob("garak_*_report.html"))
        if html_files:
            latest_file = max(html_files, key=lambda p: p.stat().st_mtime)
            return str(latest_file)
        
        # Check ~/.garak directory
        garak_dir = Path.home() / ".garak"
        if garak_dir.exists():
            html_files = list(garak_dir.glob("*.html"))
            if html_files:
                latest_file = max(html_files, key=lambda p: p.stat().st_mtime)
                return str(latest_file)
        
        # Check for any HTML files in current directory
        html_files = list(current_dir.glob("*.html"))
        if html_files:
            latest_file = max(html_files, key=lambda p: p.stat().st_mtime)
            return str(latest_file)
            
        return None
        
    def open_report(self, report_path: str):
        """Open the report in browser"""
        self.print_header("Step 5: Opening Report")
        
        if report_path:
            self.print_info(f"Report generated: {report_path}")
            try:
                webbrowser.open(f"file://{os.path.abspath(report_path)}")
                self.print_success("Report opened in browser")
            except Exception as e:
                self.print_error(f"Failed to open report: {e}")
                self.print_info(f"Manual path: {os.path.abspath(report_path)}")
        else:
            self.print_warning("No report found. Check current directory and ~/.garak directory manually")
            
    def run(self):
        """Main execution flow"""
        self.print_header("LLM vulnerability scanner")
        
        # Check prerequisites
        if not self.check_prerequisites():
            return
            
        # Step 1: Select model
        model_name = self.select_model()
        if not model_name:
            self.print_error("Failed to select model")
            return
            
        # Step 2: Setup environment
        env_success, env_name = self.setup_garak_environment()
        if not env_success:
            return
            
        # Step 3: Select probes
        probes = self.select_probes()
        
        # Step 4: Run test
        report_path = self.run_garak_test(model_name, probes, env_name)
        
        # Step 5: Open report
        if report_path:
            self.open_report(report_path)
        
        self.print_header("Scan Complete")
        print(f"{Colors.OKGREEN}Thank you for using LLM vulnerability scanner!{Colors.ENDC}")

def main():
    """Main entry point"""
    try:
        scanner = LLMVulnerabilityScanner()
        scanner.run()
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}Scan interrupted by user{Colors.ENDC}")
    except Exception as e:
        print(f"\n{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")

if __name__ == "__main__":
    main()