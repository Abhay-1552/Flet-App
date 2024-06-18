# Exploring Flet with Python

Welcome to my Flet Python Learning Repository! This repository documents my journey exploring Flet, a Python library for creating interactive web applications. Here, you'll find my experiments, examples, and notes as I learn how to use Flet.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Getting Started](#getting-started)

## Introduction

Flet is a powerful and easy-to-use Python library for building interactive web applications. As I explore Flet, I aim to document my learning process and share useful examples and insights. This repository serves as a learning resource for anyone interested in mastering Flet along with me.

## Installation

To install Flet, you'll need to have Python installed on your machine. You can install Flet using pip:

```bash
pip install flet
```

## Getting Started

To get started with Flet, follow these simple steps:

1. **Create a new Python file**: Create a new Python file in your project directory, e.g., `app.py`.

2. **Import Flet**: Import the Flet library at the top of your Python file.

3. **Initialize Flet**: Initialize Flet and create a simple web application.

Here's a basic example to get you started:

```python
import flet as ft

def main(page):
    page.title = "Hello, Flet!"
    page.add(ft.Text("Welcome to Flet"))

ft.app(target=main)
```

4. **Run your application**: Run your Python file using the command below:

```bash
python app.py
```