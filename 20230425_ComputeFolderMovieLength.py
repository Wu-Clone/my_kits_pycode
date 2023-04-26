import os
from moviepy.video.io.VideoFileClip import VideoFileClip

# 文件夹路径
folder_path = input("请输入文件夹路径：")
# 遍历文件夹中的所有文件
total_duration = 0
for filename in os.listdir(folder_path):
    # 检查文件是否为视频文件
    if filename.endswith(".mp4") or filename.endswith(".avi") or filename.endswith(".mkv"):
        # 使用moviepy库获取视频时长
        video_path = os.path.join(folder_path, filename)
        clip = VideoFileClip(video_path)
        duration = clip.duration
        clip.close()
        total_duration += duration
        print(video_path + "\t" + str(duration))
# 将总时长转换为小时、分钟、秒钟
hours, remainder = divmod(total_duration, 3600)
minutes, seconds = divmod(remainder, 60)
# 打印总时长
print(f"Total duration: {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds")
