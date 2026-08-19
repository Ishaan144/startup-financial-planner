# Startup Financial Planner

An AI-powered application that helps early-stage businesses receive relevant financial optimization advice without needing to write complex AI prompts.

## Overview

Small-business owners may know what they want to improve but may not know how to provide an AI system with enough context to receive useful recommendations.

Startup Financial Planner solves this problem through a structured input process. The application collects important information about the business and automatically organizes it into a detailed prompt for Google Gemini. Gemini then uses that information to generate a personalized financial optimization plan.

The project’s main purpose is to make AI prompting faster, more consistent, and more accessible for small businesses looking to improve their financial operations.

## How It Works

1. The user enters information about their business.
2. The application organizes the information into a structured AI prompt.
3. The prompt is sent to Google Gemini.
4. Gemini generates a personalized financial optimization plan.
5. The recommendations are displayed through the Streamlit interface.

## Information Collected

The application considers information such as:

- Type of startup
- Years in business
- Product or service
- Area the business wants to optimize
- Monthly revenue
- Number of employees
- Employee wages
- Production costs
- Marketing expenses
- Monthly sales
- Non-essential expenses
- Funding received
- Remaining funding

## Key Goals

- Remove the need for users to write complicated AI prompts
- Collect the business information required for relevant recommendations
- Turn structured user inputs into a detailed AI request
- Produce more personalized and actionable optimization plans
- Make AI-based financial planning easier for early-stage businesses

## Features

- Guided text and number inputs
- Interactive Streamlit interface
- Automatic structured prompt creation
- Personalized AI-generated recommendations
- Financial and operational optimization suggestions
- Input completion indicators

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- Git
- GitHub

## Run the Application Locally

### 1. Clone the repository

```bash
git clone https://github.com/Ishaan144/startup-financial-planner.git
```

### 2. Enter the project folder

```bash
cd startup-financial-planner
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Set your Gemini API key

On macOS or Linux:

```bash
export GEMINI_API_KEY="your_api_key"
```

### 5. Start the Streamlit application

```bash
python3 -m streamlit run my_app.py
```


## Live Demo

[Open the Startup Financial Planner](https://startup-financial-planner-8kxxotf5nvwnnucxzfpjt7.streamlit.app/)

## Future Improvements

- Add downloadable financial plans
- Include charts and financial visualizations
- Improve input validation and error handling
- Add more detailed financial calculations
- Allow users to select different optimization goals
- Improve the design for mobile devices

## Project Status

The first functional version of Startup Financial Planner is complete. The application is currently being prepared for public deployment.

## Disclaimer

This application was created as an educational project. Its AI-generated recommendations should not be considered professional financial advice.