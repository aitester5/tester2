# LLM vulnerability scanner

A comprehensive Python script for testing LLM models for vulnerabilities using [garak](https://github.com/NVIDIA/garak) by NVIDIA.

## Features

- **Interactive Model Setup**: Support for both .gguf files and existing Ollama models
- **Automated Environment Management**: Creates and manages conda environments
- **Comprehensive Probe Selection**: Choose from 32 different security probes
- **Automated Report Generation**: Generates and opens HTML reports in browser
- **User-Friendly Interface**: Color-coded output and step-by-step guidance
- **Flexible Environment Support**: Works with new or existing conda environments

## Prerequisites

Before running the script, ensure you have:

1. **Miniconda or Anaconda** installed on your system
2. **Ollama** installed and running
3. **Python 3.10-3.12** (automatically handled by conda environment)

### Installing Prerequisites

#### 1. Install Miniconda
```bash
# Download and install Miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

# Or visit: https://docs.conda.io/en/latest/miniconda.html
```

#### 2. Install Ollama
```bash
# Linux/macOS
curl -fsSL https://ollama.ai/install.sh | sh

# Or visit: https://ollama.ai/download
```

## Usage

### 1. Run the Script
```bash
python garak_prompt_injection.py
```

### 2. Follow the Interactive Steps

The script follows a 5-step process:

#### **Step 1: Model Selection**
- Option 1: Use a .gguf model file (script will create ModelFile and set up Ollama)
- Option 2: Use an already pulled Ollama model

#### **Step 2: Environment Setup**
- Option 1: Create new conda environment and install garak
- Option 2: Use existing environment (you'll specify the environment name)

#### **Step 3: Probe Selection**
- Choose from 32 available security probes
- Select individual probes or use all probes

#### **Step 4: Test Execution**
- Automated execution with real-time progress
- Live status updates during scanning

#### **Step 5: Report Generation**
- Automatic report generation and browser opening
- Report location displayed on interface

## Available Probes

The script includes 32 security probes (without the "garak.probes." prefix):

### Core Vulnerability Probes
- `promptinject` - **Primary prompt injection tests**
- `dan` - "Do Anything Now" jailbreak attempts
- `encoding` - Encoding-based injection tests
- `latentinjection` - Hidden injection tests

### Advanced Security Probes
- `exploitation` - Code and template injection
- `malwaregen` - Malware generation attempts
- `xss` - Cross-site scripting tests
- `visual_jailbreak` - Visual-based jailbreak attempts

### Specialized Attack Probes
- `continuation` - Continuation attacks
- `suffix` - Suffix-based attacks
- `grandma` - Social engineering tests
- `doctor` - Professional role exploitation
- `ansiescape` - ANSI escape sequence attacks
- `atkgen` - Attack generation tests

### Content and Behavior Probes
- `realtoxicityprompts` - Real toxicity prompt tests
- `misleading` - Misleading information tests
- `packagehallucination` - Package hallucination tests
- `donotanswer` - Refusal testing

### Technical Probes
- `fileformats` - File format exploitation
- `glitch` - Glitch-based attacks
- `snowball` - Snowball effect attacks
- `taptest` - TAP (Tree of Attack Prompts) testing
- `_tier` - Tier-based testing

[Complete list of 32 probes available in the script]

## Example Workflow

### Using a .gguf Model

```bash
$ python garak_prompt_injection.py

============================================================
                 LLM vulnerability scanner                  
============================================================

Step 1: Model Selection
Choose your model option:
1. LLM model in .gguf format
2. Already pulled model in Ollama

Enter your choice (1-2): 1

Enter the full path to your .gguf model file: /path/to/model.gguf
Enter a name for your model: my-test-model

✓ ModelFile created: /path/to/ModelFile
✓ Model 'my-test-model' created successfully

Available models:
1. my-test-model
2. llama3.1:8b

Select model (1-2): 1

Step 2: Garak Environment Setup
Choose environment option:
1. Create an environment and install garak
2. Already created and garak is installed

Enter your choice (1-2): 1

✓ Environment created successfully
✓ Garak installed successfully
✓ Garak is working correctly

Step 3: Probe Selection
Available probes:
 1. base
 2. promptinject
 3. dan
 ...

Enter probe numbers separated by commas: 2,3,8

Step 4: Running Garak Test
Running command: conda run -n garak_env python -m garak --model_type ollama --model_name my-test-model --probes promptinject,dan,encoding

Garak is running... This may take several minutes to complete...
[Live garak output...]

✓ Garak test completed successfully!

Step 5: Opening Report
Report generated: /current/directory/garak_report.html
✓ Report opened in browser
```

### Using Existing Ollama Model with Custom Environment

```bash
$ python garak_prompt_injection.py

Step 1: Model Selection
Choose your model option:
1. LLM model in .gguf format
2. Already pulled model in Ollama

Enter your choice (1-2): 2

Available models:
1. llama3.1:8b
2. mistral-nemo:latest

Select model (1-2): 1

Step 2: Garak Environment Setup
Choose environment option:
1. Create an environment and install garak
2. Already created and garak is installed

Enter your choice (1-2): 2

Enter the environment name: my_garak_env

✓ Garak is working correctly

Step 3: Probe Selection
Enter probe numbers separated by commas (e.g., 1,3,5) or 'all' for all probes: all

[Test execution...]
```

## Understanding Results

After the test completes, garak generates a comprehensive report showing:

- **Vulnerability Summary**: Overview of detected vulnerabilities
- **Probe Results**: Detailed results for each probe
- **Attack Success Rates**: Percentage of successful attacks
- **Recommendations**: Security improvements suggestions

### Report Location

Reports are automatically generated and opened in your browser. They can be found in:
- Current working directory (priority)
- `~/.garak/` directory (fallback)
- Report path is displayed in the interface

## Troubleshooting

### Common Issues

1. **"Conda not found"**
   - Ensure conda is installed and in PATH
   - Try `conda --version` to verify

2. **"Ollama not found"**
   - Install Ollama from https://ollama.ai/
   - Ensure Ollama service is running

3. **"Model creation failed"**
   - Check .gguf file path and permissions
   - Ensure sufficient disk space
   - Verify .gguf file is valid

4. **"Garak installation failed"**
   - Check internet connectivity
   - Try manual installation: `pip install garak`

5. **"Environment not found"**
   - Check environment name spelling
   - List environments: `conda env list`

### Environment Management

```bash
# List existing environments
conda env list

# Create new environment manually
conda create -n garak_env python=3.12 -y
conda activate garak_env
pip install garak

# Remove environment if needed
conda env remove -n garak_env
```

### Report Issues

```bash
# Manually check reports in current directory
ls -la *.html

# Check ~/.garak directory
ls -la ~/.garak/
```

## Security Considerations

- **Test Environment**: Run tests in isolated environments
- **Model Safety**: Be cautious with untrusted models
- **Result Interpretation**: Consult security experts for critical applications
- **Data Privacy**: Ensure test data doesn't contain sensitive information
- **Resource Usage**: Some probes may consume significant resources

## Advanced Usage

### Command Line Options

For advanced users, garak supports additional options:

```bash
# Custom output directory
python -m garak --model_type ollama --model_name model --probes promptinject --output_dir /custom/path

# Specific configuration
python -m garak --model_type ollama --model_name model --probes promptinject --config /path/to/config.yaml

# Verbose output
python -m garak --model_type ollama --model_name model --probes promptinject --verbose
```

### Probe Categories

The 32 probes are organized into categories:

1. **Injection Attacks**: promptinject, latentinjection, encoding
2. **Jailbreak Attempts**: dan, visual_jailbreak, grandma
3. **Social Engineering**: doctor, grandma, misleading
4. **Technical Exploits**: exploitation, xss, fileformats
5. **Content Generation**: malwaregen, realtoxicityprompts
6. **Behavioral Tests**: continuation, suffix, snowball

## Contributing

To contribute to this tool:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This script is provided under the MIT License. See LICENSE file for details.

## Support

For issues and questions:
- GitHub Issues: [Create an issue](https://github.com/your-repo/issues)
- Garak Documentation: [docs.garak.ai](https://docs.garak.ai)
- Ollama Documentation: [ollama.ai/docs](https://ollama.ai/docs)

## Acknowledgments

- **NVIDIA** for developing garak
- **Ollama** team for the local LLM platform
- **Anaconda** for conda environment management