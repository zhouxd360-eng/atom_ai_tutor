from paddleocr import PaddleOCR

class OCRProcessor:
    def __init__(self):
        self.ocr = PaddleOCR(use_angle_cls=True, lang='ch')
    
    def recognize(self, image_path):
        result = self.ocr.ocr(image_path, cls=True)
        texts = []
        if result:
            # 处理不同可能的结果结构
            for item in result:
                if not item:
                    continue
                # 处理可能的嵌套结构
                if isinstance(item, list):
                    for sub_item in item:
                        self._extract_text(sub_item, texts)
                else:
                    self._extract_text(item, texts)
        return "\n".join(texts)
    
    def _extract_text(self, item, texts):
        """从 OCR 结果项中提取文本"""
        try:
            if not item:
                return
            # 常见格式: [bbox, [text, confidence]]
            if isinstance(item, list) and len(item) >= 2:
                text_part = item[1]
                if text_part:
                    if isinstance(text_part, list) and len(text_part) >= 1:
                        text = text_part[0]
                        if isinstance(text, str):
                            texts.append(text)
                    elif isinstance(text_part, str):
                        texts.append(text_part)
        except (IndexError, TypeError):
            # 忽略解析错误的项
            pass

if __name__ == "__main__":
    processor = OCRProcessor()
    print(processor.recognize("test.jpg"))