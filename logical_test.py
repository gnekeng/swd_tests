
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

thai_units = {
    1: "สิบ",
    2: "ร้อย",
    3: "พัน",
    4: "หมื่น",
    5: "แสน",
    6: "ล้าน",
}

thai_texts = {
    '1': "หนึ่ง",
    '2': "สอง",
    '3': "สาม",
    '4': "สี่",
    '5': "ห้า",
    '6': "หก",
    '7': "เจ็ด",
    '8': "แปด",
    '9': "เก้า",
}

ten_digit_thai_texts = {
    '2': "ยี่",
    '3': "สาม",
    '4': "สี่",
    '5': "ห้า",
    '6': "หก",
    '7': "เจ็ด",
    '8': "แปด",
    '9': "เก้า",
}

def convert_to_thai_text(str_number):
    if str_number == '0':
        return "ศูนย์"
    
    result = ""
    str_number = str_number[::-1] #inverse for ten digit is always index 1.
    len_num = len(str_number)
    
    for index in range( len_num-1, -1, -1):
        if str_number[index] == '0':
            continue
        
        if index == 1:
            if str_number[index] in ten_digit_thai_texts:
                result += ten_digit_thai_texts[str_number[index]]
            if index in thai_units:
                result += thai_units[index]
        elif index == 0 and str_number[index] == '1' and len_num > 1:
            result += "เอ็ด"
        elif str_number[index] in thai_texts:
            result += thai_texts[str_number[index]]
            if index in thai_units:
                result += thai_units[index]
        
    return result

if __name__ == '__main__':
    number = input("Enter Number: ")
    print("Convert ", number, " to ", convert_to_thai_text(number))