# Use an official Python runtime as a parent image

FROM python:3-stretch



# Set the working directory to /app

WORKDIR /app



# Copy the client code into the container at /app

COPY assignment1_pb2.py /app/
COPY assignment1_pb2_grpc.py /app/
COPY requirements.txt /app/
COPY wait-for-it.sh /app/
COPY TweetClient.py /app/


# Install any needed packages specified in requirements.txt

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 50051

# Run greeter_client.py when the container launches

CMD ["python3", "TweetClient.py"]