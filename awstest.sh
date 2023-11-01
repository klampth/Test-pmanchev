gst-launch-1.0 autovideosrc device=/dev/video0 ! videoconvert ! video/x-raw,format=I420,width=640,height=480,framerate=30/1 ! 
                x264enc bframes=0 key-int-max=45 bitrate=500 ! video/x-h264,stream-format=avc,alignment=au,profile=baseline ! 
                kvssink stream-name="kvs_example_camera_stream" storage-size=512 access-key="AKIAUONSTLJCCIJMNTWR" secret-key="g2EDY5fNp1qc1mL0Y1bTVObU0XdHOuAi9oaiL4WX" aws-region="a-central-1"
