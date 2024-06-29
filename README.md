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

### Projects
Here are the projects included in this portfolio:

1. **Todo App**
    - **Description**: A distraction-free web app to help you focus on creating and completing tasks.
    - **Source Code**: [GitHub](https://github.com/AVRSANAND/Web_Simple_Todo)
    - **Live Demo**: [Demo](https://avrsanand-web-simple-todo.streamlit.app/)

2. **Portfolio Website**
    - **Description**: A website built entirely in Python to showcase python projects and apps.
    - **Source Code**: [GitHub](https://github.com/AVRSANAND/Python_Portfolio)
    - **Live Demo**: [Demo](https://avrsanand-python-portfolio-home.streamlit.app/)

3. **PDF Templates**
    - **Description**: A script that generates PDF templates of multiple pages given some predefined guidelines.
    - **Source Code**: [GitHub](https://github.com/AVRSANAND/PDF_Generator)
    - **Live Demo**: No Live Demo

4. **PDF Invoices**
    - **Description**: A script that reads invoice records from Excel files and automatically generates PDF invoices.
    - **Source Code**: [GitHub](https://github.com/AVRSANAND/PDF_Invoices)
    - **Live Demo**: No Live Demo

5. **News Articles to Mail**
    - **Description**: A script that utilizes newsapi.org's api to send news articles over a specified topic to requested email.
    - **Source Code**: [GitHub](https://github.com/AVRSANAND/News_to_Mail)
    - **Live Demo**: No Live Demo

6. **Weather API**
    - **Description**: A REST API built with Python and Flask to serve historical weather data for various cities.
    - **Source Code**: [GitHub](https://github.com/AVRSANAND/Weather_API)
    - **Live Demo**: No Live Demo

7. **Weather Forecast Website**
    - **Description**: A website built to forecast weather data such as temperature and sky conditions.
    - **Source Code**: [GitHub](https://github.com/AVRSANAND/Weather_Forecast_WebApp)
    - **Live Demo**: [Demo](https://avrsanand-weather-forecast-webapp.streamlit.app/)


