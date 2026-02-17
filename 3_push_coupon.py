import os
from dotenv import load_dotenv
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi
from linebot.v3.messaging.models.coupon_message import CouponMessage
from linebot.v3.messaging.models.push_message_request import PushMessageRequest

load_dotenv(override=True, dotenv_path=".env")
configuration = Configuration(access_token=os.getenv("CHANNEL_ACCESS_TOKEN"))
api_client = ApiClient(configuration) 
messaging_api = MessagingApi(api_client)

def push_coupon(user_id: str, coupon_id: str):
    try:
        messages = [CouponMessage(coupon_id=coupon_id)]

        request = PushMessageRequest(
            to=user_id,
            messages=messages,
        )

        api_response = messaging_api.push_message(push_message_request=request)
        print("The response of MessagingApi->push_message:\n")
        print(api_response)

    except Exception as e:
        print(f"Exception when calling MessagingApi->push_message: {e}\n")
        raise


if __name__ == "__main__":
    USER_ID = os.getenv("LINE_USER_ID")
    COUPON_ID = "01KHNEBPAP6NG6GA9TB94NEHS5"
    push_coupon(USER_ID, COUPON_ID)