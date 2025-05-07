# django_charge_summarizer

[![Static Badge](https://img.shields.io/badge/GitHub-jcivitell-green?logo=github)](https://github.com/jcivitel/django_charge_summarizer)
[![GitHub Repo stars](https://img.shields.io/github/stars/jcivitel/django_charge_summarizer)](https://github.com/jcivitel/django_charge_summarizer)
[![Docker Pulls](https://img.shields.io/docker/pulls/jcivitell/django_charge_summarizer?logo=docker)](https://hub.docker.com/r/jcivitell/django_charge_summarizer)
[![Docker Stars](https://img.shields.io/docker/stars/jcivitell/django_charge_summarizer?logo=docker)](https://hub.docker.com/r/jcivitell/django_charge_summarizer)
[![Docker Image Size](https://img.shields.io/docker/image-size/jcivitell/django_charge_summarizer/latest?logo=docker)](https://hub.docker.com/r/jcivitell/django_charge_summarizer)

## Overview

`django_charge_summarizer` is a Django-based project for managing and analyzing charge invoices. It allows uploading invoice files, aggregating charge information, and visualizing the data in charts.

## Features

- **File Upload**: Supports uploading ZIP and PDF files.
- **Data Aggregation**: Aggregates `total_kwh` per customer.
- **Visualization**: Displays aggregated data in bar and pie charts.
- **User Management**: Authentication and authorization of users.

## Installation

### Prerequisites

- Python 3.x
- Django
- Docker (optional)

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/jcivitel/django_charge_summarizer.git
    cd django_charge_summarizer
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the migrations:
    ```bash
    python manage.py migrate
    ```

5. Start the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

### Uploading Files

1. Log in to the dashboard.
2. Navigate to the upload page.
3. Select and upload the files.

### Viewing Aggregated Data

1. Select the desired month and year on the dashboard.
2. The charts will automatically update to show the aggregated `total_kwh` per customer.

## Docker

To start the project with Docker, run the following commands:

1. Build the Docker image:
    ```bash
    docker build -t django_charge_summarizer .
    ```

2. Start the container:
    ```bash
    docker run -p 8000:8000 django_charge_summarizer
    ```

## License

This project is licensed under the BSD 3-Clause License. See the `LICENSE` file for more details.

## Contributors

[![Contributors Display](https://badges.pufler.dev/contributors/jcivitel/django_charge_summarizer?size=50&padding=5&bots=false)](https://github.com/jcivitel/django_charge_summarizer/graphs/contributors)
