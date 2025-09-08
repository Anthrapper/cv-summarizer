# CV Summarizer

A Streamlit-based web application that processes uploaded PDF and DOCX files and generates summaries using local AI models via Ollama.

## Quick Start

### Prerequisites

- Python 3.8+
- Ollama installed and running

### Installation

1. **Install UV package manager**:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. **Setup the project**:

```bash
cd cv-summarizer
uv sync
```

3. **Start Ollama service**:

```bash
ollama serve
```

4. **Run the application**:

```bash
streamlit run app.py
```

## Configuration

Configure summarization parameters by editing `settings.json`:

```json
{
  "summary_settings": {
    "min_length": 430,
    "max_length": 500
  },
  "model_settings": {
    "temperature": 0.2,
    "max_tokens": 600,
    "chunk_size": 3000
  },
  "ollama_settings": {
    "base_url": "http://localhost:11434",
    "timeout": 60
  },
  "prompt": "You are an experienced HR professional..."
}
```

### Settings Options

- **min_length/max_length**: Summary character limits
- **temperature**: Controls creativity (0.0 = focused, 1.0 = creative)
- **max_tokens**: Maximum response length
- **chunk_size**: Text chunk size for large documents
- **base_url**: Ollama server endpoint (defaults to <http://localhost:11434>)
- **timeout**: Request timeout in seconds (default: 60)
- **prompt**: Custom prompt template (use `{document_text}`, `{min_length}`, `{max_length}` placeholders)

### Remote Ollama Server

To use a remote Ollama server, update the `base_url` in `ollama_settings`:

```json
{
  "ollama_settings": {
    "base_url": "http://192.168.1.100:11434",
    "timeout": 60
  }
}
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
