import os
from dotenv import load_dotenv
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi
from linebot.v3.messaging.models.coupon_message import CouponMessage
from linebot.v3.messaging.models.push_message_request import PushMessageRequest

load_dotenv()

CHANNEL_ACCESS_TOKEN = os.environ.get("CHANNEL_ACCESS_TOKEN")
if not CHANNEL_ACCESS_TOKEN:
    raise ValueError("CHANNEL_ACCESS_TOKEN environment variable is not set")

# Configure Bearer authorization
configuration = Configuration(access_token=CHANNEL_ACCESS_TOKEN)
api_client = ApiClient(configuration)
messaging_api = MessagingApi(api_client)


def push_coupon(user_id: str, coupon_id: str):
    if not user_id or not str(user_id).strip():
        raise ValueError("user_id is empty")
    if not coupon_id or not str(coupon_id).strip():
        raise ValueError("coupon_id is empty")

    try:
        messages = [CouponMessage(coupon_id=coupon_id)]

        request = PushMessageRequest(
            to=user_id,
            messages=messages,
        )

        api_response = messaging_api.push_message(push_message_request=request)
        print("The response of MessagingApi->push_message:\n")
        print(api_response)

        return api_response
    except Exception as e:
        print(f"Exception when calling MessagingApi->push_message: {e}\n")
        raise


if __name__ == "__main__":
    USER_ID = "Uxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    COUPON_ID = "01KFNS2Y3EB5S79S9Z86MQHGTH"
    push_coupon(USER_ID, COUPON_ID)