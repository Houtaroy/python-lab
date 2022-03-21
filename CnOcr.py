from PIL import Image
from cnstd import CnStd
from cnocr import CnOcr

if __name__ == '__main__':
    std = CnStd()
    cn_ocr = CnOcr()

    img = Image.open('D:/Download/test.jpg')
    box_infos = std.detect(img)

    for box_info in box_infos['detected_texts']:
        cropped_img = box_info['cropped_img']
        ocr_res = cn_ocr.ocr_for_single_line(cropped_img)
        print('ocr result: %s' % str(ocr_res))
