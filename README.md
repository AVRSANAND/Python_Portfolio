# Python Portfolio Project

## Overview
This project is a personal portfolio showcasing various Python projects developed by AVRS Anand. The portfolio is built using Streamlit and includes detailed descriptions, images, source code links, and live demos of each project.

## Features
- **Project Showcase**: Displays a list of Python projects with descriptions, images, source code links, and live demo links.
- **Contact Information**: Provides information on how to reach out for questions or collaborations.

## Project Structure
```
python-portfolio/
│
├── images/                  # Folder containing images for the portfolio
│   ├── 1.png       
│   └── ...                  # Additional project images
│
├── Home.py                  # Main application script for the portfolio
├── send_email.py            # Script for sending emails
├── current_data.csv         # CSV file containing project data
├── requirements.txt         # Project dependencies
└── README.md                # Project README file
```

## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/AVRSANAND/Python_Portfolio.git
    cd Python_Portfolio
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    streamlit run Home.py
    ```

## Usage
Once the application is running, you can explore the following features:

### Project Showcase
- **Description**: Displays a list of projects with their titles, descriptions, images, source code links, and live demo links.
- **Data Source**: The project data is read from `current_data.csv`, which contains the following columns:
  - `title`: The title of the project.
  - `description`: A brief description of the project.
  - `image`: The filename of the image representing the project.
  - `git_url`: The URL to the source code repository.
  - `live_url`: The URL to the live demo of the project.


### Contact Information
Feel free to reach out through the Contact Page or connect with me on LinkedIn. Cheers!

## Dependencies
- streamlit
- pandas
- requests
- smtplib
- ssl
