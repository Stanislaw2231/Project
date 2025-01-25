"""
This module contains the function to run the Streamlit application.
"""

import os
import subprocess


def streamlit_run(dummy_input):
    """
    Runs the Streamlit application found in the same directory.

    This function checks for the existence of 'streamlit.py' in the same directory,
    then launches it using the 'streamlit' command. If the file is missing, a
    FileNotFoundError is raised.

    Raises:
        FileNotFoundError: If 'streamlit.py' does not exist in the directory.
    """
    
    # Create and run command
    streamlit_file = os.path.join(os.path.dirname(__file__), "streamlit.py")
    if not os.path.exists(streamlit_file):
        raise FileNotFoundError(f"File Not Found: {streamlit_file}")
    subprocess.run(["streamlit", "run", streamlit_file], check=True)
