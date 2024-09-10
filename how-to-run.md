## How to run the starter project

1. Make sure you are in the root directory of the project.
2. In the root directory, create a virtual environment by running the following command:

    ```bash
    python3 -m venv venv
    ```
    Here the second `venv` is the name of the virtual environment. You can use any name you want.

3. Activate the virtual environment by running the following command:

    ```bash
    source venv/bin/activate 
    ```
    If you are using Windows, you can activate the virtual environment by running the following command:

    ```bash
    venv\Scripts\activate
    ```
4. Install the required packages by running the following command:

    ```bash
    pip install -r requirements.txt
    ```
5. Run the following command to start the server:

    ```bash
    python app.py
    ```
