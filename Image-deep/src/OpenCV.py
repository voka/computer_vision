import matplotlib.pyplot as plt
from PIL import Image
from skimage import io
import cv2
from IPython.display import clear_output, Image, display, Video, HTML
Video('./data/video/Night_Day_Chase.mp4')
import time

class PIL_image():
    def __init__(self):
        # PIL은 oepn()으로 image file을 읽어서 ImageFile객체로 생성. 
        print("PIL")
        pil_image = Image.open("./data/image/beatles01.jpg")
        print('image type:', type(pil_image))
        plt.figure(figsize=(10, 10))
        plt.imshow(pil_image)
        plt.show()

class skimage_image():
    def __init__(self):
        #skimage(사이킷이미지)로 이미지 로드 하기
        #skimage는 imread()를 이용하여 RGB 원본 이미지를 RGB 형태의 넘파이 배열로 반환함.
        #skimage는 imread()를 이용하여 image를 numpy 배열로 반환함. 
        sk_image = io.imread("./data/image/beatles01.jpg")
        print('sk_image type:', type(sk_image), ' sk_image shape:', sk_image.shape)

        plt.figure(figsize=(10, 10))
        plt.imshow(sk_image)
        plt.show()

class OpenCV_image():
    def __init__(self):
        #OpenCV로 이미지 로드하기
        #OpenCV는 imread()를 이용하여 원본 RGB 이미지를 BGR 형태의 넘파이 배열로 반환함.
        #OpenCV의 imwrite()를 이용한다면 BGR 형태의 이미지 배열을 파일에 기록할 때 다시 RGB형태로 변환하므로 사용자는 RGB->BGR->RGB 변환에 신경쓰지 않아도 됨.
        cv2_image = cv2.imread("./data/image/beatles01.jpg")
        cv2.imwrite("./data/image//output/beatles02_cv.jpg", cv2_image)
        print('cv_image type:', type(cv2_image), ' cv_image shape:', cv2_image.shape)

        plt.figure(figsize=(10, 10))
        img = plt.imread("./data/image/output/beatles02_cv.jpg")
        plt.imshow(img)
        plt.show()

        
        #OpenCV의 imread()로 반환된 BGR 이미지 넘파이 배열을 그대로 시각화 하기
        #OpenCV의 imread()는 RGB를 BGR로 변환하므로 원하지 않는 이미지가 출력됨

        cv2_image = cv2.imread("./data/image/beatles01.jpg")

        plt.figure(figsize=(10, 10))
        plt.imshow(cv2_image)
        plt.show()

        sk_image = io.imread("./data/image/beatles01.jpg")
        print(sk_image.shape)
        sk_image[:, :, 0]
        cv2_image = cv2.imread("./data/image/beatles01.jpg")
        print(type(cv2_image))
        print(cv2_image.shape)
        cv2_image[:, :, 0]
        cv2_image[:, :, 2]
        cv2_image = cv2.imread("./data/image/beatles01.jpg")
        draw_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)

        plt.figure(figsize=(10, 10))
        plt.imshow(draw_image)
        plt.show() 


# 동영상에 초록색 사각형 씌우는 예제 일 뿐임.
class OpenCV_video():

    
    #OpenCV 영상처리
    #OpenCV는 간편하게 비디오 영상처리를 할 수 있는 API를 제공
    #VideoCapture 객체는 Video Streaming을 Frame 별로 Capture하여 처리할 수 있는 기능 제공
    #VideoWriter 객체는 VideoCapture로 읽어들인 Frame을 동영상으로 Write하는 기능 제공
    def __init__(self):
        video_input_path = './data/video/Night_Day_Chase.mp4'
        # linux에서 video output의 확장자는 반드시 avi 로 설정 필요. 
        video_output_path = './data/video/output/Night_Day_Chase_output.avi'

        cap = cv2.VideoCapture(video_input_path)
        # Codec은 *'XVID'로 설정. 
        codec = cv2.VideoWriter_fourcc(*'XVID')

        vid_size = (round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))) #(200, 400)
        vid_fps = cap.get(cv2.CAP_PROP_FPS )
            
        vid_writer = cv2.VideoWriter(video_output_path, codec, vid_fps, vid_size) 

        frame_cnt = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print('총 Frame 갯수:', frame_cnt, 'FPS:', round(vid_fps), 'Frame 크기:', vid_size)

        green_color=(0, 255, 0)
        red_color=(0, 0, 255)

        start = time.time()
        index=0
        while True:
            hasFrame, img_frame = cap.read()
            if not hasFrame:
                print('더 이상 처리할 frame이 없습니다.')
                break
            index += 1
            print('frame :', index, '처리 완료')
            cv2.rectangle(img_frame, (300, 100, 800, 400), color=green_color, thickness=2) 
            caption = "frame:{}".format(index)
            cv2.putText(img_frame, caption, (300, 95), cv2.FONT_HERSHEY_SIMPLEX, 0.7, red_color, 1)
            
            vid_writer.write(img_frame)

        print('write 완료 시간:', round(time.time()-start,4))
        vid_writer.release()
        cap.release()