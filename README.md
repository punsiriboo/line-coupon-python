# line-coupon-python

โปรเจกต์สำหรับสร้างคูปอง LINE โดยใช้ LINE Messaging API

## การติดตั้ง

1. ติดตั้ง dependencies:
```bash
pip install -r requirements.txt
```

2. ตั้งค่า environment variable:
```bash
export CHANNEL_ACCESS_TOKEN="your_channel_access_token_here"
```
## การใช้งาน

รันสคริปต์เพื่อสร้างคูปอง:
```bash
python create_coupon.py
```

## หมายเหตุ

- ต้องมี `CHANNEL_ACCESS_TOKEN` ใน environment variable (BEARER_TOKEN = CHANNEL_ACCESS_TOKEN)
- ต้องกำหนดข้อมูลคูปองใน `CouponCreateRequest` object ก่อนเรียก API
- สคริปต์จะบันทึกเวลาเริ่มต้นและเวลาสิ้นสุดของการสร้างคูปอง
