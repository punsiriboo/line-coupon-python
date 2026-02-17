

# จัดการคูปอง LINE โดยใช้ LINE Messaging API
![title](images/title.png)
## การติดตั้ง

1. ติดตั้ง dependencies:
```bash
pip install -r requirements.txt
```

2. ตั้งค่า environment variable:

**วิธีที่ 1: ใช้ไฟล์ .env (แนะนำ)**
```bash
# สร้างไฟล์ .env
echo "CHANNEL_ACCESS_TOKEN=your_channel_access_token_here" > .env
```

**วิธีที่ 2: ตั้งค่า environment variable โดยตรง**
```bash
export CHANNEL_ACCESS_TOKEN="your_channel_access_token_here"
```


## ไฟล์ในโปรเจกต์

### 1. `1_create_coupon.py` - สร้างคูปอง
สร้างคูปอง LINE ใหม่

**การใช้งาน:**
```bash
python 1_create_coupon.py
```

**ฟีเจอร์:**
- สร้างคูปองด้วยข้อมูลที่กำหนดไว้
- แสดง coupon_id ที่สร้างได้

**เอกสารอ้างอิง:**
- [LINE Messaging API - create_coupon](https://github.com/line/line-bot-sdk-python/blob/master/linebot/v3/messaging/docs/MessagingApi.md#create_coupon)

### 2. `2_get_coupon.py` - ดึงข้อมูลคูปอง
ดึงข้อมูลคูปองและรายการคูปองทั้งหมด

**การใช้งาน:**
```bash
python 2_get_coupon.py
```

**ฟีเจอร์:**
- แสดงรายการคูปองทั้งหมด
- ดึงข้อมูลคูปองตาม coupon_id

**เอกสารอ้างอิง:**
- [LINE Messaging API - list_coupon](https://github.com/line/line-bot-sdk-python/blob/master/linebot/v3/messaging/docs/MessagingApi.md#list_coupon)
- [LINE Messaging API - get_coupon_detail](https://github.com/line/line-bot-sdk-python/blob/master/linebot/v3/messaging/docs/MessagingApi.md#get_coupon_detail)

**หมายเหตุ:** แก้ไข `COUPON_ID` ในไฟล์เพื่อดึงข้อมูลคูปองอื่น

### 3. `3_broadcast_coupon.py` - ส่งคูปองผ่าน Broadcast
ส่งคูปองให้ผู้ใช้ทั้งหมดผ่าน Broadcast Message

**การใช้งาน:**
```bash
python 3_broadcast_coupon.py
```

**ฟีเจอร์:**
- ส่งคูปองให้ผู้ใช้ทั้งหมดที่ติดตาม LINE Official Account
- บันทึกเวลาเริ่มต้นและเวลาสิ้นสุด

**เอกสารอ้างอิง:**
- [LINE Messaging API - broadcast](https://github.com/line/line-bot-sdk-python/blob/master/linebot/v3/messaging/docs/MessagingApi.md#broadcast)

**หมายเหตุ:** แก้ไข `COUPON_ID` ในไฟล์ให้ตรงกับ coupon_id ที่ต้องการส่ง

### 4. `4_push_coupon.py` - ส่งคูปองแบบ Push (ส่งหาคนเดียว)
ส่งคูปองให้ผู้ใช้ 1 คน ผ่าน Push Message

**การใช้งาน:**
```bash
python 4_push_coupon.py
```

**ฟีเจอร์:**
- ส่งคูปองให้ผู้ใช้คนเดียวด้วย `USER_ID` และ `COUPON_ID`

**เอกสารอ้างอิง:**
- [LINE Messaging API - push_message](https://github.com/line/line-bot-sdk-python/blob/master/linebot/v3/messaging/docs/MessagingApi.md#push_message)

**หมายเหตุ:** แก้ไข `USER_ID` และ `COUPON_ID` ในไฟล์ให้ตรงกับข้อมูลที่ต้องการส่ง

### 5. `5_close_coupon.py` - ปิดคูปอง
ปิด/ลบคูปองออกจากระบบ

**การใช้งาน:**
```bash
python 5_close_coupon.py
```

**ฟีเจอร์:**
- ปิดคูปองที่ระบุ
- ผู้ใช้จะไม่สามารถใช้คูปองนั้นได้อีก

### 6. `6_narrowcast_coupon.py` - ส่งคูปองแบบ Narrowcast (target เฉพาะผู้หญิง)
ส่งคูปองให้เฉพาะกลุ่มเป้าหมายผู้หญิงผ่าน Narrowcast Message

**การใช้งาน:**
```bash
python 6_narrowcast_coupon.py
```

**ฟีเจอร์:**
- ส่งคูปองให้เฉพาะผู้หญิงที่ติดตาม LINE Official Account (target gender = female)
- ใช้ filter demographic ตามมาตรฐาน LINE Messaging API


**เอกสารอ้างอิง:**
- [LINE Messaging API - close_coupon](https://github.com/line/line-bot-sdk-python/blob/master/linebot/v3/messaging/docs/MessagingApi.md#close_coupon)

**หมายเหตุ:** 
- แก้ไข `COUPON_ID` ในไฟล์เพื่อปิดคูปองอื่น
- ⚠️ **ระวัง:** การปิดคูปองจะลบคูปองออกจากระบบถาวร

## หมายเหตุ

- ต้องมี `CHANNEL_ACCESS_TOKEN` ใน environment variable (BEARER_TOKEN = CHANNEL_ACCESS_TOKEN)
- ต้องกำหนดข้อมูลคูปองใน `CouponCreateRequest` object ก่อนเรียก API
- ไฟล์ `.env` อยู่ใน `.gitignore` แล้ว เพื่อความปลอดภัย
- ทุกไฟล์ใช้โครงสร้างเดียวกัน: สร้าง configuration และ messaging_api ที่ระดับโมดูล
