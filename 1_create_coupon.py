import os
from dotenv import load_dotenv
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi
from linebot.v3.messaging.models.coupon_create_request import CouponCreateRequest

load_dotenv()

CHANNEL_ACCESS_TOKEN = os.environ.get("CHANNEL_ACCESS_TOKEN")
if not CHANNEL_ACCESS_TOKEN:
    raise ValueError("CHANNEL_ACCESS_TOKEN environment variable is not set")

# Configure Bearer authorization
configuration = Configuration(access_token=CHANNEL_ACCESS_TOKEN)
api_client = ApiClient(configuration)
messaging_api = MessagingApi(api_client)

def create_coupon():    
    # สร้าง CouponCreateRequest object จากข้อมูลที่กำหนด
    coupon_create_request = CouponCreateRequest(
        title="Friends-only coupon - 2",
        description="- To use this coupon, please show this screen to the staff.\n- Used coupons cannot be used again. If you accidentally mark it as \"used\", it will also become unavailable.\n- This coupon may be changed or terminated without notice regardless of the validity period.",
        reward={
            "type": "discount",
            "priceInfo": {
                "type": "fixed",
                "fixedAmount": 100
            }
        },
        acquisitionCondition={
            "type": "normal"
        },
        startTimestamp=0,
        endTimestamp=1924959599,
        imageUrl="https://developers.line.biz/media/messaging-api/coupon/sample-coupon-image-100-yen-off.jpg",
        timezone="ASIA_TOKYO",
        visibility="UNLISTED",
        maxUseCountPerTicket=1,
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
