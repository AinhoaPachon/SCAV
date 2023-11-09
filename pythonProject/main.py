import os

class BBB:
    def video_info(name):
        parameters = " -vf 'split[original],codecview=mv=pf+bf+bb[vectors],[vectors][original]blend=all_mode=difference128,eq=contrast=7:brightness=-0.3'"
        command = "ffplay -flags2 +export_mvs -i " + name + parameters
        os.system(command)

    def exercise2(name, outputName):
        command = "ffmpeg -i " + name + " -ss 00:00:00 -t 00:00:50 -c:v copy -an " + outputName + ".mp4"
        os.system(command)
        command = "ffmpeg -i " + name + " -ss 00:00:00 -t 00:00:50 -q:a 0 -map a " + outputName + ".mp3"
        os.system(command)

BBB.exercise2("BBB.mp4", "BBB50")