#!/bin/bash
# Installation script for prerequisites
# This script helps install Miniconda and Ollama if they're not already installed

set -e

echo "🚀 Garak Prompt Injection Testing Tool - Prerequisites Installer"
echo "================================================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ $1${NC}"
}

# Check if running on supported OS
check_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        OS="linux"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
    else
        print_error "Unsupported operating system: $OSTYPE"
        exit 1
    fi
    print_info "Detected OS: $OS"
}

# Check if conda is installed
check_conda() {
    if command -v conda &> /dev/null; then
        print_success "Conda is already installed"
        conda --version
        return 0
    else
        print_warning "Conda is not installed"
        return 1
    fi
}

# Install Miniconda
install_conda() {
    print_info "Installing Miniconda..."
    
    if [[ "$OS" == "linux" ]]; then
        MINICONDA_URL="https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
    elif [[ "$OS" == "macos" ]]; then
        MINICONDA_URL="https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh"
    fi
    
    # Download installer
    print_info "Downloading Miniconda installer..."
    curl -sL "$MINICONDA_URL" -o miniconda.sh
    
    # Run installer
    print_info "Running Miniconda installer..."
    bash miniconda.sh -b -p "$HOME/miniconda3"
    
    # Initialize conda
    print_info "Initializing conda..."
    "$HOME/miniconda3/bin/conda" init
    
    # Source the shell
    if [[ "$OS" == "linux" ]]; then
        source ~/.bashrc
    elif [[ "$OS" == "macos" ]]; then
        source ~/.zshrc
    fi
    
    # Clean up
    rm miniconda.sh
    
    print_success "Miniconda installed successfully"
}

# Check if Ollama is installed
check_ollama() {
    if command -v ollama &> /dev/null; then
        print_success "Ollama is already installed"
        ollama --version
        return 0
    else
        print_warning "Ollama is not installed"
        return 1
    fi
}

# Install Ollama
install_ollama() {
    print_info "Installing Ollama..."
    
    # Download and install Ollama
    curl -fsSL https://ollama.ai/install.sh | sh
    
    # Start Ollama service (if systemd is available)
    if command -v systemctl &> /dev/null; then
        print_info "Starting Ollama service..."
        sudo systemctl start ollama
        sudo systemctl enable ollama
    else
        print_warning "Please start Ollama manually: ollama serve"
    fi
    
    print_success "Ollama installed successfully"
}

# Main installation process
main() {
    print_info "Starting prerequisites installation..."
    
    check_os
    
    # Install conda if not present
    if ! check_conda; then
        read -p "Do you want to install Miniconda? (y/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            install_conda
        else
            print_warning "Skipping Miniconda installation"
        fi
    fi
    
    # Install Ollama if not present
    if ! check_ollama; then
        read -p "Do you want to install Ollama? (y/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            install_ollama
        else
            print_warning "Skipping Ollama installation"
        fi
    fi
    
    echo
    print_success "Prerequisites check complete!"
    print_info "You can now run: python garak_prompt_injection.py"
    
    # Show some example Ollama commands
    echo
    print_info "Example Ollama models you can pull:"
    echo "  ollama pull llama3.1:8b"
    echo "  ollama pull mistral-nemo:latest"
    echo "  ollama pull codellama:7b"
    echo "  ollama pull qwen2:7b"
    
    echo
    print_info "To see available models:"
    echo "  ollama list"
    
    echo
    print_info "To test Ollama:"
    echo "  ollama run llama3.1:8b"
}

# Run main function
main "$@"