from ultralytics import YOLO


def main() -> None:
    model = YOLO("grpc://localhost:8001/yolov8n-mug", task='detect')

    result = model("man-holding-mug.jpg")
    result[0].save("man-holding-mug-yolov8n-mug.jpg")


if __name__ == "__main__":
    main()
