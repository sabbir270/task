# Django Project Task

This repository contains the code for a Django project that includes integration with Plotly for data visualization and CRUD operation.


live link: https://mytasksite.pythonanywhere.com/

## Overview

In this project, I developed a web application using Django, a popular web framework for Python. The application load data from a dataset, CRUD operations and visualizes it using various charts, including line charts and bar charts, using the Plotly library.

## Project Structure

- **task_project/**: Contains the Django project settings and configuration files.
- **task/**: Contains the Django app with views, models, templates and utils.py file to load json data.
- **requirements.txt**: Lists all Python dependencies required for the project.
- **README.md**: This file provides an overview of the project and its components.

## Installation

To run this project locally, follow these steps:

1. Clone this repository to your local machine.
2. Install Python and Django if you haven't already.
3. Create a virtual environment for the project.
4. Install the required Python dependencies using `pip install -r requirements.txt`.
5. Set up the database and migrate the Django models.
6. Run the Django development server using `python manage.py runserver`.

## Usage

Once the project is set up, you can access the web application by visiting http://localhost:8000/ in your web browser. The application allows you to view stock data, perform CRUD operations and visualize it using various charts generated with Plotly.


## Challenges Faced

- Integrating Plotly for data visualization required learning new concepts.
- Configuring Plotly charts to work seamlessly within the Django framework took some trial and error.

## Lessons Learned

- Plotly provides powerful and flexible tools for creating interactive visualizations in web applications.
- Django's templating system can be used effectively with external libraries like Plotly for dynamic content generation.
- Documentation and examples are crucial when integrating new libraries or technologies into a project.

