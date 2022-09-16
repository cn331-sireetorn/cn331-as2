# cn331-as2
Project เว็บลงทะเบียน
Member
1.Sireetorn Ontrakul 6310611048
2.Chutirat Kaewchay 6310682643

ความสามารถของระบบ: 

Student:
    หน้าlogin: กรอก username และ password แล้วกดloginเพื่อเข้าสู่ระบบ
    หน้าHome: จะขึ้นแสดงชื่อ Username และ email ของ student โดยหน้านี้ก็จะประกอบไปด้วยปุ่ม Home, Enrollment Result, Course List และ Log out
        โดยจะสามารถ link ไปหน้าอื่นๆได้
    หน้าEnrollment Result: หน้านี้จะใช้แสดงเกี่ยวกับชื่อของ student และรายวิชาที่ได้กดจองไปแล้ว 
    หน้าCourse List: หน้านี้จะใช้แสดงรายชื่อวิชาทั้งหมดโดยจะแสดงในรูปแบบตาราง ประกอบด้วย รายชื่อวิชา(course), รหัสวิชา(code), ภาคการศึกษา(semester), จำนวนโควตา(quota), รายละเอียด(detail) ของแต่ละรายวิชา, สถานะ(status) โดยในส่วนของstatus ถ้าขึ้นว่า empty หมายถึง quota ยังไม่เต็มสามารถสมัครได้ แต่ถ้าหากขึ้นว่า full หมายความว่า quota เต็มไม่สามารถสมัครเพิ่มได้   
    หน้าdetails: หน้านี้จะแสดงชื่อรายวิชา รหัสวิชา และ รายละเอียดของวิชานั้นๆ โดยจะแบ่งเป็น 3 กรณีคือ
        1. โดยหน้านี้ก็จะมีปุ่ม Enrollment อยู่หาก student นี้ยังไม่เคยสมัครในรายวิชานี้ก็จะสามารถกดจองได้ปกติ เมื่อกดจองแล้วก็จะเข้าสู่หน้า Enrollment Result เพื่อดูผลการจอง
        2. ในกรณีที่ student นี้เคยสมัครวิชานี้ไปแล้ว เมื่อกดดูdetailsแล้ว ปุ่มที่เคยเป็น Enrollment จะเปลี่ยนเป็นปุ่ม withdraw สำหรับถอนวิชานี้แทน หากกดปุ่ม withdraw แล้วก็จะเข้าสู่หน้า Enrollment Result แสดงผลว่ารายวิชานี้ได้ถูกถอนออกไปแล้ว
        3. ในกรณีที่ status ขึ้นว่า full ก็ยังสามารถกดเข้ามาดูรายละเอียดวิชาได้ แต่จะไม่สามารถกดปุ่ม enroll ได้
    

Admin:
    หน้าlogin: กดปุ่ม Admin เข้าไปสู่หน้า login ของ Admin กรอก username และ password เพื่อเข้าสู่ระบบของ Admin

ฟังก์ชั่นในหน้า admin

๊Users   : จะแสดง username ,email address,firstname,lastname และ staff status ของผู้ใช้งานระบบ
          admin สามารถเพิ่ม account admin โดยการกด add user แล้วทำการกรอกข้อมูลของadmin

courses : จะแสดง course(รายชื่อวิชา) ,course code(รหัสวิชา), seat quota(จำนวนโควตา) ,detail(รายละเอียด), semester(ภาคการศึกษา) และ 
          status(สถานะ) 
          
          admin สามารถแก้ไข course(ชื่อวิชา) ,course code(รหัสวิชา), seat quota(จำนวนโควตา) ,detail(รายละเอียด), semester(เทอม/ปีการศึกษา) ทั้งการเพิ่ม ลด หรือปรับแก้รายละเอียดต่างๆในแต่ละหัวข้อได้ ในส่วน status(สถานะ) admin จะปรับเปลี่ยนตาม seat quota ของวิชานั้นๆ หากจำนวนโควตาเต็ม จะเปลี่ยน status จาก empty เป็น full 

Enrolls : จะแสดงชื่อของ student ตามด้วยรหัสวิชาที่ student ทำการกด enroll   
          
