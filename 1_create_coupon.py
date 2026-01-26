import os
from dotenv import load_dotenv
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi
from linebot.v3.messaging.models.coupon_create_request import CouponCreateRequest

load_dotenv(override=True, dotenv_path=".env")
configuration = Configuration(access_token=os.getenv("CHANNEL_ACCESS_TOKEN"))
api_client = ApiClient(configuration) 
messaging_api = MessagingApi(api_client)

def create_coupon():    
    try:
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

        api_response = messaging_api.create_coupon(
            coupon_create_request=coupon_create_request
        )
        print("The response of MessagingApi->create_coupon: {}\n".format(api_response))
   
    except Exception as e:
        print(f"Exception when calling MessagingApi->create_coupon: {e}\n")
        raise

if __name__ == "__main__":
    create_coupon()
