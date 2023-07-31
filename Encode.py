import ffmpeg

def encode_video(input_path, output_path, codec="libx264", crf=23):
    try:
        input_stream = ffmpeg.input(input_path)
        output_stream = ffmpeg.output(input_stream, output_path, codec=codec, crf=crf)
        ffmpeg.run(output_stream)
        print("Video encoding completed successfully.")
    except ffmpeg.Error as e:
        print("Error:", e)

if __name__ == "__main__":
    input_file = "/home/leadsoc/Downloads/Videos/Raindrops_Videvo.mp4"
    output_file = "/home/leadsoc/Downloads/Videos/output_video.mp4"
    encode_video(input_file, output_file)

