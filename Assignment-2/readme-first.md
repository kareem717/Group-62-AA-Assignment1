# Skyseat Service Setup and Run Guide

Welcome to the Skyseat service! Follow the steps below to ensure you have the necessary environment and dependencies set up and to run the application.

## Prerequisites

Make sure you have the following installed:

- Python (3.7 or above)
- Node.js and npm
- `virtualenv` (for Python virtual environments)

## Step-by-Step Setup Guide

### 1. Clone the Repository

First, clone the Skyseat repository to your local machine if you haven’t already:

```bash
git clone https://github.com/kareem717/Group-62-AA-Assignment1.git
cd Group-62-AA-Assignment1
cd app
```

### 2. Set Up the Python Virtual Environment

Create and activate a Python virtual environment:

#### Create the virtual environment:

```bash
python3 -m venv venv
```

#### Activate the virtual environment:

For **macOS/Linux**:

```bash
source venv/bin/activate
```

For **Windows**:

```bash
.env\Scriptsctivate
```

You should now see `(venv)` at the beginning of your terminal prompt, this means that you're in the virtual environment.

### 3. Install Node.js Packages

Make sure all the necessary Node.js packages are installed:

```bash
npm install
```

### 4. Install Python Dependencies

Make sure all the Python dependencies are installed (requirements.txt is in dir 'app'):

```bash
pip install -r app/requirements.txt
```

### 4. Setup Enivroment Variables

Create a `.env` file and populate the variables:

```bash
touch app/.env
cat app/.env.example > app/.env
```

### 5. Running the Application

Once all dependencies are installed, you can start the application by running (app file is in dir 'app'):

```bash
python3 app/app.py
```
