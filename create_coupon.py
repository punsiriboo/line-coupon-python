import os
import time
from datetime import datetime
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi
from linebot.v3.messaging.models.coupon_create_request import CouponCreateRequest
from linebot.v3.messaging.models.coupon_create_response import CouponCreateResponse


def create_coupon():
    CHANNEL_ACCESS_TOKEN = os.environ.get("CHANNEL_ACCESS_TOKEN")
    if not CHANNEL_ACCESS_TOKEN:
        raise ValueError("CHANNEL_ACCESS_TOKEN environment variable is not set")
    
    # Configure Bearer authorization
    configuration = Configuration(access_token=CHANNEL_ACCESS_TOKEN)
    api_client = ApiClient(configuration)
    messaging_api = MessagingApi(api_client)
    
    # สร้าง CouponCreateRequest object
    # CouponCreateRequest ต้องระบุ fields ต่อไปนี้:
    # - title (str, required): ชื่อคูปอง
    # - description (str, required): รายละเอียดคูปอง
    # - valid_from (str, required): วันที่เริ่มต้นใช้งาน (รูปแบบ ISO 8601: YYYY-MM-DDTHH:mm:ssZ)
    # - valid_until (str, required): วันที่หมดอายุ (รูปแบบ ISO 8601: YYYY-MM-DDTHH:mm:ssZ)
    # - discount_type (str, optional): ประเภทส่วนลด (เช่น "PERCENTAGE", "AMOUNT")
    # - discount_amount (int, optional): จำนวนส่วนลด
    # - discount_percentage (int, optional): เปอร์เซ็นต์ส่วนลด
    # - max_redemption_count (int, optional): จำนวนครั้งที่ใช้คูปองได้สูงสุด
    # - min_purchase_amount (int, optional): จำนวนเงินซื้อขั้นต่ำ
    coupon_create_request = CouponCreateRequest(
        title="คูปองส่วนลด",
        description="รายละเอียดคูปอง",
        valid_from="2026-01-01T00:00:00Z",
        valid_until="2026-03-31T23:59:59Z",
        discount_type="AMOUNT",
        discount_amount=10,
        max_redemption_count=100,
        min_purchase_amount=100,
    )    
    try:
        api_response = messaging_api.create_coupon(
            coupon_create_request=coupon_create_request
        )
        print("The response of MessagingApi->create_coupon:\n")
        print(api_response)

   
    except Exception as e:
        print(f"Exception when calling MessagingApi->create_coupon: {e}\n")
        raise

if __name__ == "__main__":
    try:
        response = create_coupon()
        print("\nสร้างคูปองสำเร็จ!")
    except Exception as e:
        print(f"\nเกิดข้อผิดพลาด: {e}")
        exit(1)
