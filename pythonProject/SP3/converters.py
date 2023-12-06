import os

# ----------------------------------------------------------------------------------------------------------------------

class SP3:
    def resize(input_name, output_name, w, h):
        # Changes the resolution of the input video.
        command = f'ffmpeg -i ' + input_name + '.mp4 -vf scale=' + str(w) + ':' + str(h) + ' -crf 18 -preset ' \
                  f'faster -c:a copy ' + output_name + '.mp4'
        os.system(command)

    def resize_BBB(name):
        # Resizes the input video
        SP3.resize(name, name + '_160', 160, 120)
        SP3.resize(name, name + '_360', 360, 240)
        SP3.resize(name, name + '_480', 640, 480)
        SP3.resize(name, name + '_720', 1280, 720)

    def convert(name, format):
        match format:
            case "vp8":
                command = "ffmpeg -i " + name + ".mp4 -c:v libvpx -crf 10 -b:v 1M -c:a libvorbis " + name + "_vp8.webm"
            case "vp9":
                command = "ffmpeg -i " + name + ".mp4 -c:v libvpx-vp9 -b:v 1M " + name + "_vp9.webm"
            case "h265":
                command = "ffmpeg -i " + name + ".mp4 -c:v libx265 -crf 26 -preset" \
                         f" fast -c:a aac -b:a 128k " + name + "_h265.mp4"
            case "av1":
                command = "ffmpeg -i " + name + ".mp4 -c:v libaom-av1 -crf 30 -b:v 2000k " + name + "_av1.mkv"
            case _:
                print("Invalid format")
                return

        os.system(command)

    def task1(name):
        SP3.resize_BBB(name)
        SP3.convert(name + '_720', "vp8")
        SP3.convert(name + '_720', "vp9")

    def find(name):
        path1 = os.getcwd()
        for root, dirs, files in os.walk(path1):
            if name in files:
                return 1
        return -1

    def video_check(name):
        """
        Checks if the video exists. If not, it creates it
        :return: 1 if successful
        """

        # Checks if the video is already exists
        if SP3.find(name) == 1:
            return 1

        # Separate the name into the name of the video, the resolution and the codec
        whole_name = name.split("_")
        res = whole_name[1]
        codec = whole_name[2].split('.')
        codec.pop()

        resized_name = whole_name[0] + "_" + whole_name[1] #for convenience

        # Checks if the resized video exists, if not, we create it
        if SP3.find(whole_name[0] + "_" + whole_name[1] + ".mp4") == -1:
            SP3.resize_BBB(whole_name[0])

        # Convert the resized video into the desired codec
        SP3.convert(resized_name, codec[0])
        return 1

    def task2(name1, name2):
        SP3.video_check(name1)
        SP3.video_check(name2)

        command = "ffmpeg -i " + name1 + " -i " + name2 + " -filter_complex hstack output.mp4"
        os.system(command)

#SP3.task2("BBB_720_vp8.webm", "BBB_720_vp9.webm")
#SP3.task1('BBB')