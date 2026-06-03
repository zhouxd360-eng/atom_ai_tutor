import cv2
import os

class VideoProcessor:
    def extract_frames(self, video_path, output_dir, interval=10):
        os.makedirs(output_dir, exist_ok=True)
        cap = cv2.VideoCapture(video_path)
        frame_count = 0
        saved_count = 0
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            if frame_count % interval == 0:
                cv2.imwrite(f"{output_dir}/frame_{saved_count:04d}.jpg", frame)
                saved_count += 1
            frame_count += 1
        
        cap.release()
        return saved_count
    
    def get_metadata(self, video_path):
        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count / fps
        cap.release()
        return {"fps": fps, "frame_count": frame_count, "duration": duration}

if __name__ == "__main__":
    processor = VideoProcessor()
    print(processor.get_metadata("test.mp4"))