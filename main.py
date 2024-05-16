from ultralytics import YOLO


def main() -> None:
    model = YOLO("yolov8n.pt", task='detect')

    result = model("man-holding-mug.jpg")
    result[0].save("result.jpg")


if __name__ == "__main__":
    main()
