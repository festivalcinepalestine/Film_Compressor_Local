from moviepy import VideoFileClip

def convert_mov_to_mp4(input_path, output_path):
    # Load the .mov file
    video_clip = VideoFileClip(input_path)
    
    # Write the video file to .mp4 format with audio, using a faster preset
    video_clip.write_videofile(
        output_path,
        codec='libx264',
        audio_codec='aac',
        ffmpeg_params=['-preset', 'fast', '-crf', '32', '-threads', '4']
    )

# Example usage

input_path = "C:\\Users\\maya\\Desktop\\Bureau DEll\\Perso\\FCP2026\\COTRcleanmaster.mov"
output_path = "C:\\Users\\maya\\Desktop\\Bureau DEll\\Perso\\FCP2026\\COTRcleanmasterVF.mp4"

convert_mov_to_mp4(input_path, output_path)