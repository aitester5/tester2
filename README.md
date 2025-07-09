# Garak Prompt Injection Testing Tool

A comprehensive Python script for testing LLM models for prompt injection vulnerabilities using [garak](https://github.com/NVIDIA/garak) by NVIDIA.

## Features

- **Interactive Model Setup**: Support for both .gguf files and existing Ollama models
- **Automated Environment Management**: Creates and manages conda environments
- **Comprehensive Probe Selection**: Choose from 33 different security probes
- **Automated Report Generation**: Generates and opens HTML reports in browser
- **User-Friendly Interface**: Color-coded output and step-by-step guidance

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

### 2. Follow the Interactive Prompts

The script will guide you through:

1. **Model Selection**:
   - Option 1: Use a .gguf model file (script will create ModelFile and set up Ollama)
   - Option 2: Use an already pulled Ollama model

2. **Environment Setup**:
   - Option 1: Create new conda environment and install garak
   - Option 2: Use existing environment (if already set up)

3. **Probe Selection**:
   - Choose from 33 available security probes
   - Select individual probes or use all probes

4. **Test Execution**:
   - Automated execution with real-time progress
   - Report generation and browser opening

## Available Probes

The script includes the following security probes:

### Core Probes
- `garak.probes.base` - Base functionality tests
- `garak.probes.promptinject` - **Primary prompt injection tests**
- `garak.probes.dan` - "Do Anything Now" jailbreak attempts
- `garak.probes.encoding` - Encoding-based injection tests

### Advanced Probes
- `garak.probes.latentinjection` - Hidden injection tests
- `garak.probes.exploitation` - Code and template injection
- `garak.probes.malwaregen` - Malware generation attempts
- `garak.probes.xss` - Cross-site scripting tests

### Specialized Probes
- `garak.probes.continuation` - Continuation attacks
- `garak.probes.suffix` - Suffix-based attacks
- `garak.probes.grandma` - Social engineering tests
- `garak.probes.doctor` - Professional role exploitation

[Full list of 33 probes available in the script]

## Example Workflow

### Using a .gguf Model

```bash
$ python garak_prompt_injection.py

============================================================
                 Garak Prompt Injection Testing Tool
============================================================

Choose your model option:
1. LLM model in .gguf format
2. Already pulled model in Ollama

Enter your choice (1-2): 1

Enter the full path to your .gguf model file: /path/to/model.gguf
Enter a name for your model: my-test-model

✓ ModelFile created: /path/to/ModelFile
✓ Model 'my-test-model' created successfully

Choose environment option:
1. Create an environment and install garak
2. Already created and garak is installed

Enter your choice (1-2): 1

ℹ Creating conda environment...
✓ Environment created successfully
ℹ Installing garak...
✓ Garak installed successfully

Available probes:
 1. garak.probes.base
 2. garak.probes.promptinject
 3. garak.probes.dan
 ...

Enter probe numbers separated by commas: 2,3,8

ℹ Running command: conda run -n garak_env python -m garak --model_type ollama --model_name my-test-model --probes garak.probes.promptinject,garak.probes.dan,garak.probes.encoding

⚠ This may take several minutes to complete...
[Garak execution output...]

✓ Garak test completed successfully!
ℹ Opening report: /home/user/.garak/report_20250715_143022.html
✓ Report opened in browser
```

### Using Existing Ollama Model

```bash
$ python garak_prompt_injection.py

Choose your model option:
1. LLM model in .gguf format
2. Already pulled model in Ollama

Enter your choice (1-2): 2

Available models:
1. llama3.1:8b
2. mistral-nemo:latest
3. codellama:7b

Select model (1-3): 1

Choose environment option:
1. Create an environment and install garak
2. Already created and garak is installed

Enter your choice (1-2): 2

✓ Garak is working correctly

Available probes:
...
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

Reports are saved in `~/.garak/` directory with timestamped filenames:
- HTML reports: `report_YYYYMMDD_HHMMSS.html`
- JSON reports: `report_YYYYMMDD_HHMMSS.jsonl`

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

4. **"Garak installation failed"**
   - Check internet connectivity
   - Try manual installation: `pip install garak`

### Environment Issues

```bash
# Reset environment if needed
conda env remove -n garak_env
conda create -n garak_env python=3.12 -y
conda activate garak_env
pip install garak
```

### Report Issues

```bash
# Manually check reports
ls -la ~/.garak/
```

## Security Considerations

- **Test Environment**: Run tests in isolated environments
- **Model Safety**: Be cautious with untrusted models
- **Result Interpretation**: Consult security experts for critical applications
- **Data Privacy**: Ensure test data doesn't contain sensitive information

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