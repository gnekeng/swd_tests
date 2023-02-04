# swd_tests

หมายเหตุ 
**** 
- เกือบทุกฟังก์ชันผมจะให้ส่ง error NOT FOUND แทนที่จะส่ง list ว่างๆกลับไป ถ้าหา objects ที่ต้องการหรือ objects ที่จำเป็นนำไปใช้ query ต่อไม่เจอ เนื่องจากผมไม่แน่ใจว่า front-end จะจัดการกับการไม่พบข้อมูลอย่างไร และเนื่องจาก front-end อาจจะงงได้ถ้าส่ง list ว่างไปเฉยๆโดยไม่มีข้อความอธิบาย ซึ่งผมมองว่าขึ้นอยู่ว่าเราคุยกันยังไง
- ไฟล์ test_api.py มีการเปลี่ยนเปลี่ยนแปลงเนื่องจากมีการเทสและเปลี่ยนวิธีการ request ในบางฟังก์ชันแต่ผมได้เก็บของต้นฉบับไว้ในไฟล์ชื่อ test_api_back_up.py

****
หัวข้อ "StudentSubjectsScoreAPIView"
- (post) ผมได้เปลี่ยน models ของ Personnel สามารถเข้าไปอ่านคำอธิบายได้ที่ไฟล์ models.py

****
หัวข้อ "StudentSubjectsScoreDetailsAPIView"
- (get) ผมได้สร้างฟังก์ชันใหม่ชื่อ get_grade ขึ้นมาใหม่เพื่อลด duplicate code ทำให้ต้องเปลี่ยนฟังก์ชัน get ให้ไม่เป็น staticmethod เพื่อที่จะให้สามารถใช้ self สำหรับเรียกใช้ฟังก์ชัน get_grade ได้

****
หัวข้อ "PersonnelDetailsAPIView"
- (get) ผมได้เปลี่ยนวิธีการ request ในไฟล์ test_api.py จากใส่ชื่อโรงเรียนไปตรงๆเป็นใช้ตัวแปรชื่อ school_title เพื่อให้เหมาะสม

****
หัวข้อ "SchoolHierarchyAPIView"
- (get) ผมได้เปลี่ยนวิธีการ request ในไฟล์ test_api.py จากใส่ชื่อโรงเรียนไปตรงๆเป็นใช้ตัวแปรชื่อ school_title เพื่อให้เหมาะสม