import pika, json
from bson.Ojectid import ObjecyID
import moviepy.editor

def start(message, fs_videos, fs_mp3s, channel):
    pass

def start(message, fs_videos, fs_mp3, channer):
    message = json.loads(message)

    #empy tem file
    tf=tempfile.NamedTemporaryFile()

    #video contens
    out = fs_videos.get(ObjecId(message["video_fid"]))

    #add video contenst to empty file

    tf.write(out.read())

    audio = moviepy.editor.VideoFileClip(tf.name). audio 
    tf.close()
