import cv2
import pytesseract

""""

This class is responsible of processing images

    Methods :
    - save a version with defined words
    - save a version with defined text lines
    - save a version with defined main text

"""


class Processor:

    def process(self, image, path, file_format):
        print(">>>", image)
        self.define_words(image, path + "defined_words."+file_format)
        self.define_text_lines(image, path + "defined_text_lines."+file_format)
        self.define_main_text(image, path + "defined_main_text."+file_format)

    @staticmethod
    def define_words(image, path):
        img = cv2.imread(image)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        hImg, wImg, _ = img.shape
        boxes = pytesseract.image_to_data(img)
        for x, b in enumerate(boxes.splitlines()):
            if x != 0:
                b = b.split()
                if len(b) == 12:
                    x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                    cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 1)

        cv2.imwrite(path, img)

    @staticmethod
    def define_text_lines(image, path):
        img = cv2.imread(image)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 3))
        morph = cv2.morphologyEx(thresh, cv2.MORPH_DILATE, kernel)
        cntrs = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cntrs = cntrs[0] if len(cntrs) == 2 else cntrs[1]
        result = img.copy()
        for c in cntrs:
            box = cv2.boundingRect(c)
            x, y, w, h = box
            cv2.rectangle(result, (x, y), (x + w, y + h), (0, 0, 255), 1)

        cv2.imwrite(path, result)

    @staticmethod
    def define_main_text(image, path):
        img = cv2.imread(image)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
        rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
        dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)
        contours, _ = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        im2 = img.copy()
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 0, 255), 1)

        cv2.imwrite(path, im2)



