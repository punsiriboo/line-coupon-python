"""
LINE Coupon Broadcast Script
ส่งคูปองให้ผู้ใช้ทั้งหมดผ่าน Broadcast Message
"""
import os
from dotenv import load_dotenv
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi
from linebot.v3.messaging.models.broadcast_request import BroadcastRequest
from linebot.v3.messaging.models.coupon_message import CouponMessage

load_dotenv(override=True, dotenv_path=".env")
configuration = Configuration(access_token=os.getenv("CHANNEL_ACCESS_TOKEN"))
api_client = ApiClient(configuration) 
messaging_api = MessagingApi(api_client)

def broadcast_coupon(coupon_id: str):
    
    if not coupon_id or not str(coupon_id).strip():
        raise ValueError("coupon_id is empty")

    try:
        messages = [CouponMessage(coupon_id=coupon_id)]
        broadcast_request = BroadcastRequest(messages=messages)
        
        api_response = messaging_api.broadcast(
            broadcast_request=broadcast_request
        )
        
        print("The response of MessagingApi->broadcast:\n")
        print(api_response)
        
    except Exception as e:
        print(f"Exception when calling MessagingApi->broadcast: {e}")
        raise


if __name__ == "__main__":
    COUPON_ID = "01KFNS2Y3EB5S79S9Z86MQHGTH"
    broadcast_coupon(COUPON_ID)