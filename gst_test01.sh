gst-launch-1.0 v4l2src device=/dev/video0 ! videoscale ! video/x-raw, width=2592, height=600 ! autovideosink -v
