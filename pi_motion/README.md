# Introduction 
Pi Motion Stuff for camera project
https://www.instructables.com/Raspberry-Pi-Motion-Detection-Security-Camera/
https://magpi.raspberrypi.org/articles/anpr-car-spy-raspberry-pi
    sudo cp -a /usr/share/openalpr/runtime_data/ocr/tessdata/*.traineddata /usr/share/openalpr/runtime_data/ocr/
     sudo ln -s /home/pi/.local/bin/pushover  /usr/bin/pushover
      pip install numpy




# Getting Started
TODO: Guide users through getting your code up and running on their own system. In this section you can talk about:
1.	Installation process
    # install git
        sudo apt-get install git
    # change default python
        sudo rm /usr/bin/python
        sudo ln -s /usr/bin/python3 /usr/bin/python
        ls -l /usr/bin/python
    -- Output lrwxrwxrwx 1 root root 16 Jan 18 11:04 /usr/bin/python -> /usr/bin/python3.
    # Check Version
    python -V
    -- Output Python 3.7.3.

2.	run camera\setup.sh
3.	edit /etc/rc.local add before exit statement
    /home/pi/daemon/on_boot.sh &

4.	sudo apt-get install motion
    Settings /etc/motion

    daemon on
    stream_localhost off
    webcontrol_localhost off
    ffmpeg_output_movies on
    target_dir /var/lib/motion

    stream_maxrate 100 #This will allow for real-time streaming but requires more bandwidth & resources
    framerate 60 #This will allow for 60 frames to be captured per second #the higher this gets, the slower the video processing
    width 640 #This changes the width of the image displayed
    height 480 #This changes the height of the image displayed

    on_event_start python /home/pi/background/motionalert.py %f
    on_movie_end python /home/pi/background/motionvid.py %f

    output_pictures locate_motion_style
    start_motion_daemon=yes


5 create motion alert python script
    sudo nano /home/pi/background/motionalert.py

6 Email video on motion
sudo nano /home/pi/background/motionvid.py
