"""
LINE Coupon Broadcast Script
ส่งคูปองให้ผู้ใช้ทั้งหมดผ่าน Broadcast Message
"""
import os
import time
from datetime import datetime
from dotenv import load_dotenv
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi
from linebot.v3.messaging.models.broadcast_request import BroadcastRequest
from linebot.v3.messaging.models.coupon_message import CouponMessage

load_dotenv()


def broadcast_coupon(coupon_id: str):
    """
    ส่งคูปองให้ผู้ใช้ทั้งหมดผ่าน Broadcast Message
    
    Args:
        coupon_id (str): ID ของคูปองที่ต้องการส่ง
    
    Returns:
        BroadcastResponse: ผลลัพธ์การส่ง broadcast
    """
    if not coupon_id or not str(coupon_id).strip():
        raise ValueError("coupon_id is empty")

    print(f"กำลังส่งคูปอง ID: {coupon_id} ผ่าน Broadcast Message")
    start_time = time.time()
    start_datetime = datetime.fromtimestamp(start_time)
    print(f"เริ่มส่งเวลา: {start_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
    
    CHANNEL_ACCESS_TOKEN = os.environ.get("CHANNEL_ACCESS_TOKEN")
    if not CHANNEL_ACCESS_TOKEN:
        raise ValueError("CHANNEL_ACCESS_TOKEN environment variable is not set")
    
    # Configure Bearer authorization
    configuration = Configuration(access_token=CHANNEL_ACCESS_TOKEN)
    api_client = ApiClient(configuration)
    messaging_api = MessagingApi(api_client)
    
    try:
        # สร้าง Coupon Message (ใช้ model ของ SDK เพื่อ serialize ให้ถูกต้อง)
        messages = [CouponMessage(coupon_id=coupon_id)]
        
        # สร้าง Broadcast Request
        broadcast_request = BroadcastRequest(messages=messages)
        
        # ส่ง Broadcast Message
        api_response = messaging_api.broadcast(
            broadcast_request=broadcast_request
        )
        
        print("The response of MessagingApi->broadcast:\n")
        print(api_response)
        
        # บันทึกเวลาที่ส่งเสร็จ
        completion_time = time.time()
        completion_datetime = datetime.fromtimestamp(completion_time)
        elapsed_time = completion_time - start_time
        print(f"\nส่งคูปองเสร็จเวลา: {completion_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"ใช้เวลาทั้งหมด: {elapsed_time:.2f} วินาที")
        
        return api_response
        
    except Exception as e:
        print(f"Exception when calling MessagingApi->broadcast: {e}")
        raise


if __name__ == "__main__":
    COUPON_ID = "01KFNS2Y3EB5S79S9Z86MQHGTH"
    
    try:
        response = broadcast_coupon(COUPON_ID)
        print("\nส่งคูปองสำเร็จ!")
    except Exception as e:
        print(f"\nเกิดข้อผิดพลาด: {e}")
        exit(1)
