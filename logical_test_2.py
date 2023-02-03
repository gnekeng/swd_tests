
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

roman_number_map = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M',
}


def convert_to_roman_number(str_number):
    result = ""
    str_number = str_number[::-1]
    len_num = len(str_number)
    for i in range(len_num-1, -1, -1):
        if str_number[i] == '0':
            continue
        
        num = int(str_number[i])
        digit_num = str_number[i] + ('0'*i)
        digit_num = int(digit_num)
        
        if digit_num in roman_number_map:
            result += roman_number_map[digit_num]
        else:
            if num <= 3:
                base_num = int('1' + ('0'*i))
                result += (digit_num // base_num) * roman_number_map[base_num]
            elif num == 4:
                left_base_num = int('1' + ('0'*i))
                right_base_num = int('5' + ('0'*i))
                result += roman_number_map[left_base_num] + roman_number_map[right_base_num]
            elif num > 5 and num <= 8:
                left_base_num = int('5' + ('0'*i))
                right_base_num = int('1' + ('0'*i))
                amount_of_right_num = (digit_num - left_base_num) // right_base_num
                result += roman_number_map[left_base_num]
                result += amount_of_right_num * roman_number_map[right_base_num]
            else:
                left_base_num = int('1' + ('0'*i))
                right_base_num = int('1' + ('0'*(i+1)))
                result += roman_number_map[left_base_num] + roman_number_map[right_base_num]
            
    return result


if __name__ == '__main__':
    number = input("Enter Number: ")
    print("Convert ", number, " to ", convert_to_roman_number(number))