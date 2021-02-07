from src.OpenCV import * # ui 폴더의 ui파일의 모든 클래스를 다 가져 오겠다.

class Main():
    def __init__(self):
        print("실행할 메인 클래스")
        OpenCV_video()

if __name__=='__main__': #MAIN 만이 실행할 파일이다. ㅇㅇ 아니면 헷갈리기 떄문에
    Main()