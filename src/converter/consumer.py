import pika, sys, os, time
from pumongo import MongoClient
import gridfs 
from convert import to_mp3
def main():
    client = MongoClient("host.minikube.internal", 27017)
    db_videos = client.videos
    db_mp3s = Cliente.db_mp3
    #gridfs
    fs_videos = gridfs.GridFS(db_videos)
    fs_mp3s = gridfs.GridFS(db_mp3s)

    #rabbimq connection
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq')
    )
    channel = connection.channel()