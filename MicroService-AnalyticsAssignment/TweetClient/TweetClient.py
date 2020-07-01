from __future__ import print_function
import logging

import grpc

import os

import random
import time
import redis
import datetime

import assignment1_pb2_grpc
import assignment1_pb2


def run():
    count = 0
    wordCount = 0
    while True:
        with grpc.insecure_channel('tweet-server:50055') as channel:
            stub = assignment1_pb2_grpc.TweetSenderStub(channel)

            for response in stub.SendTweet(assignment1_pb2.SizeRequest(size="reddit.csv")):
                count += 1
                print(response.message, flush=True)
                time.sleep(random.randint(1, 3))

                for j in range(len(response.message.split())):
                    wordCount += 1

                try:
                    conn = redis.StrictRedis(host='redis', port=6379)
                    conn.set("log.Data." , str(datetime.datetime.now()),
                             ("Data",response.message) , ("Total",str(count)) , (" Total Word Count: = " ,str(wordCount)))

                except Exception as ex:
                    print('Error:', ex)


if __name__ == '__main__':
    logging.basicConfig()
    run()
