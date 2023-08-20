import requests
import subprocess
import os
url = 'https://banana-disease.glitch.me/upload'

def capture_image(output_file):
    try:
        # Specify the raspistill command with required options
        cmd = "fswebcam -d /dev/video1 -r 1280x720 --no-banner -p YUYV -S 30 --set sharpness=50 --set brightness=70 --set Contrast=20 --delay 2 -F 2 " + output_file

        # Execute the command using subprocess
        subprocess.check_call(cmd, shell=True)

        print("Image captured and saved to " + output_file)
    except subprocess.CalledProcessError as e:
        print("Error capturing image: " + e)
        
def getserial():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"
  return cpuserial

# Call the function to capture an image and provide the output file path
output_file_path = "image.jpg"
capture_image(output_file_path)

files = {'file': open(output_file_path, 'rb')}
data = {'serial_number': get_serial()}

x = requests.post(url, files=files,  data = data)
print(x.status_code)
os.remove(output_file_path)