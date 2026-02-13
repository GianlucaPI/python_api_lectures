# Flask API Examples & Pokemon Fetcher

This repository contains examples of using Flask to create API endpoints and scripts to fetch data from external APIs.

## Project Structure

*   **[0_fetch_api_pokèdex](0_fetch_api_pokèdex)**: Contains Python scripts demonstrating how to fetch data from the PokéAPI using the `requests` library.
*   **[1_endpoint_get](1_endpoint_get)**: A simple Flask application demonstrating how to create and handle GET requests. Includes client examples.
*   **[2_endpoint_post](2_endpoint_post)**: A Flask application demonstrating how to create and handle POST requests. Includes client examples.

## Setup & Installation

### 1. Create a Virtual Environment

It is recommended to use a virtual environment to manage dependencies for this project separately from your system Python.

```bash
# Windows
python -m venv venv

# macOS/Linux
python3 -m venv venv
```

### 2. Activate the Virtual Environment

**Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate
```

*Note: If you run into permission errors, you might need to run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`.*

**Windows (Command Prompt):**

```cmd
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 3. Install Requirements

Dependencies are managed either globally or within specific folders.

For the **Flask API examples** (`1_endpoint_get` and `2_endpoint_post`), navigate to the folder and install from `requirements.txt`:

```bash
pip install -r 1_endpoint_get/requirements.txt
```

For the **Pokemon Fetcher** (`0_fetch_api_pokèdex`), you primarily need the `requests` library:

```bash
pip install requests
```

Alternatively, you can install the common packages used across the project:

```bash
pip install flask requests
```

## Running the Examples

Navigate to the specific folder and run the script or app.

**Example for fetching pokemon info:**

```bash
cd 0_fetch_api_pokèdex
python v2_fetch_pokemon_info.py
```

**Example for running the GET endpoint:**

```bash
cd 1_endpoint_get
python app.py
```
