import pika, json
def upload(f, fs, channel, access):
    try: 
        fid = fs.put(t)
    except Exception as err:
        return "internal server error", 400
    message = {
        "video_fid": str(fid),
        "mp3_fid": None,
        "username": access ["username"],
    }

    try:
        channel.basic_publish(
            exchange = "",
            routhing_key="video",
            body=json.dups(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        ) 
    except:
        fs.delete(fid)
        return "internal server error", 500