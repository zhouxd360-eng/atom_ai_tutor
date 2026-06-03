from paddleocr import PaddleOCR

class OCRProcessor:
    def __init__(self):
        self.ocr = PaddleOCR(use_angle_cls=True, lang='ch')
    
    def recognize(self, image_path):
        result = self.ocr.ocr(image_path, cls=True)
        texts = []
        for line in result:
            for word in line:
                texts.append(word[1][0])
        return "\n".join(texts)

if __name__ == "__main__":
    processor = OCRProcessor()
    print(processor.recognize("test.jpg"))