from imutils.video import VideoStream
import imagezmq
import argparse
import socket
import time
import cv2

def init():
	# construct the argument parser and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-u", "--url", required=True, help="streaming url of the camera to which the application will connect")
	ap.add_argument("-v", "--video", help="the video to stream")

	args = vars(ap.parse_args())
	# initialize the ImageSender object with the socket address of the server
	sender = imagezmq.ImageSender(connect_to=f"tcp://{args['url']}")

	src = args['video'] if args['video'] != None else 0

	camera_name = socket.gethostname()
	vs = VideoStream(src=src).start()

	print(f"[*] Camera is streaming on url: {args['url']}")
	return vs, sender, camera_name, src


if __name__=="__main__":
	vs, sender, camera_name, src = init()

	while True:
		# read the frame from the camera and send it to the server
		frame = vs.read()
		if frame is None:
			vs = VideoStream(src=src).start()
			frame = vs.read()
		sender.send_image(camera_name, frame)
