# OctoStreamer

These scripts stream the webcam feed to mjpg. This format is used by OctoPrint/
OctoPi. Its unique feature is, that is switches on a GPIO before sending the
stream or a snapshot. The pin is switched off, when no one is watching.

## Features

- Provide stream and snapshot of your camera
- Automatically switch on and off your LED lights when someone is watching
  stream
- Manually switch on/off leds wie webinterface

## Instructions

- Activate server:
  Uncomment the las lines in app.py (and set the port!)

      # if __name__ == '__main__':
      #     app.run(host='0.0.0.0', threaded=True, port=3000)
  Note: The original author says, this should not be used for production.
  I do not know enough about flask what would be correct. Please tell me.
- Change the pin number in config.json (BCM notation)
- Install requirements.txt

### v4l2

I recommend usage of the v4l2 camera. It showed best performance on raspi.
For this you need to install python-v4l2capture. I installed it from [source](https://github.com/jnohlgard/python-v4l2capture).

Run the program with:

    CAMERA=v4l2 python3 app.py

If you get an error message

    OSError: [Errno 16] Device or resource busy

you are probably already running a stream. If you are on OctoPi with
you can stop the preinstalled mjpg-streamer.
    
    sudo systemctl stop webcamd

### Test

- Go to http://localhost:<port> in your browser. In Config, it should show your
  pin from config.json. LES state should be 0.
- Click on /led_on. State should switch to 1.
- Click on /led_off. State should switch to 0.
- Open /snapshot in new browser window. State should switch to 1 in first window
  and switch back after ~10s.
- Open /video_feed in new browser window. State should switch to 1 in first
  window. It will switch back 10s after you close the stream window.
- If your LED is not turned on in you snapshot, your LED is to slow. Increase
  shapshot_delay in config.json, restart and try again.
## Orginal code by

[Flask Video Streaming Revisited](http://blog.miguelgrinberg.com/post/flask-video-streaming-revisited).
