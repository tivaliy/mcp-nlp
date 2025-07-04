# mcp-nlp

MCP-NLP is a FastMCP application designed to provide NLP (Natural Language Processing) capabilities using the Model Context Protocol (MCP).

- **[FastMCP Framework v2](https://github.com/jlowin/fastmcp)**: A modern framework for fast, Pythonic way to build MCP servers.
- **[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction)**: A protocol that allows for the management and control of LLM contexts.
- **NLP-modules**
  - `textdistance`: A module for calculating text distance metrics

## Prerequisites

Before you begin, ensure you have the following installed:

- [Python 3.12](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/tivaliy/mcp-nlp.git
   cd mcp-nlp
   ```

2. Install dependencies (using `uv`):
   ```bash
   uv sync
   ```

## Configuration

### Authentication Modes

The MCP-NLP server supports two authentication modes:

1. **Unauthenticated Mode** (default):
   - No API key required to access the server
   - Set `API_KEY_ENABLED=False` in your `.env` file

2. **API Key Authentication**:
   - Requires a valid API key in the request header
   - Set `API_KEY_ENABLED=True` and `API_KEY=your-secret-key` in your `.env` file
   - By default, the header name is `X-API-Key` (can be customized with `API_KEY_NAME`)

Example `.env` file:
```bash
# Authentication configuration
API_KEY_ENABLED=True
API_KEY=not-a-secret
# API_KEY_NAME=X-API-Key  # Optional: customize header name

# Logging level (20=INFO, 10=DEBUG)
LOGGING_LEVEL=20
```

## Available Tools

The MCP-NLP server currently provides the following MCP tools:

### Text Distance Module

Calculate similarity/distance between text sequences using various algorithms:

- **`#textdistance_measure`**:
  - **Purpose**: Measures text distance between two sequences of strings
  - **Parameters**:
    - `source` (required): The source text string
    - `reference` (required): The reference text string to compare against
    - `algorithm` (optional): The algorithm to use (default: `levenshtein`)
    - `metric` (optional): The metric to use (default: `normalized_similarity`)
  - **Returns**: A float value representing the calculated distance/similarity

- **`#textdistance_list_metrics`**:
  - **Purpose**: Lists all supported metrics for text distance algorithms
  - **Parameters**: None
  - **Returns**: A list of available metrics: `distance`, `similarity`, `normalized_distance`, `normalized_similarity`, `maximum`

- **Supported Metrics**:
  - `distance`: Raw distance score
  - `similarity`: Raw similarity score
  - `normalized_distance`: Distance normalized to a 0-1 scale
  - `normalized_similarity`: Similarity normalized to a 0-1 scale (default)
  - `maximum`: Maximum possible value for the algorithm

- **Default Algorithm**: `Levenshtein`

## Usage

### Local Running

To run the application locally:

Create a `.env` file in the root directory (see `.env.example` as an example).

1. Start the FastMCP application:
   ```bash
   uvicorn app.main:http_app --reload
   ```

2. Access the MCP server endpoint at `http://127.0.0.1:8000/mcp/` (in case of `streamable-http` transport)

### Run MCP Server Using Docker

To run the MCP server in a Docker container:

1. Build the Docker image:
   ```bash
   docker build -t mcp-nlp .
   ```

2. Run the Docker container:
   ```bash
   docker run --rm -p 8000:8000 mcp-nlp
    ```

3. Access the MCP server endpoint at `http://127.0.1:8000/mcp/` (in case of `streamable-http` transport)

## VS Code Integration

To use the MCP-NLP server with VS Code:

1. Make sure your MCP-NLP server is running

2. Add the server configuration to your VS Code `settings.json`:
   ```json
   "mcp": {
     "servers": {
       "mcp-nlp": {
         "url": "http://0.0.0.0:8000/mcp/",
         "type": "http",
         "headers": {
           "X-API-Key": "not-a-secret"  // Only needed if API_KEY_ENABLED=True
         }
       }
     }
   }
   ```

3. Enable MCP in VS Code:
   ```json
   "chat.mcp.enabled": true,
   "github.copilot.advanced": {
     "mcp.enabled": true
   }
   ```

4. You can now use the MCP-NLP tools directly in VS Code through GitHub Copilot

`MCP` | `Model Context Protocol` | `FastMCP` | `NLP`
