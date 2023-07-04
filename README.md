# Slack-Messages-App

Slack-Messages-App is a Slack integration that automatically saves new messages from a Slack channel and updates a corresponding excel sheet using a Lambda function.

## Installation

Use a virtual environment to install the required packages in the requirements.txt file. 

## Setup

1. Build and upload a Docker image to AWS ECR.
2. Create a Lambda function using the Docker image.
3. Create a new Slack app and add it to the workspace you'd like to pull messages from.
4. Add the SLACK_BOT_TOKEN env variable to the Lambda function.
5. Using API Gateway, link the lambda function to the Slack app.
6. Create a Google Sheet and add the SPREADSHEET_ID and SHEET_ID env variables.
7. Create a service account in the GCP console and download the credentials JSON. Rename it to auth.json
8. Update the GOOGLE_APPLICATION_CREDENTIALS env variable with the relative path to the auth.json