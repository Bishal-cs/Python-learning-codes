from pytube import YouTube

YouTube("https://youtube.com/clip/Ugkx0LQWdWUG77ctwQsAN3P49HDer9mtiGn3?si=-_ZOleo70CyfV1zx").streams.first().download()
