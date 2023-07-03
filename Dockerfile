FROM public.ecr.aws/lambda/python:3.10

COPY requirements.txt ${LAMBDA_TASK_ROOT}

COPY slack_lambda.py ${LAMBDA_TASK_ROOT}

COPY auth.json ${LAMBDA_TASK_ROOT}

RUN pip install -r requirements.txt

CMD [ "slack_lambda.lambda_handler" ]
