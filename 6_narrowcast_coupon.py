import os
from dotenv import load_dotenv
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi
from linebot.v3.messaging.models.narrowcast_request import NarrowcastRequest
from linebot.v3.messaging.models.coupon_message import CouponMessage
# Narrowcast targeting เฉพาะผู้หญิง (ใช้ filter)
from linebot.v3.messaging.models.filter import Filter
from linebot.v3.messaging.models.gender_demographic_filter import GenderDemographicFilter
from linebot.v3.messaging.models.gender_demographic import GenderDemographic


load_dotenv(override=True, dotenv_path=".env")

configuration = Configuration(
    access_token=os.getenv("CHANNEL_ACCESS_TOKEN")
)
api_client = ApiClient(configuration)
messaging_api = MessagingApi(api_client)


def narrowcast_coupon(coupon_id: str):
    try:
        # ข้อความที่ต้องการส่ง (Coupon)
        messages = [
            CouponMessage(coupon_id=coupon_id)
        ]


        gender_filter = GenderDemographicFilter(one_of=[GenderDemographic.FEMALE])
        filter_obj = Filter(demographic=gender_filter)

        narrowcast_request = NarrowcastRequest(
            messages=messages,
            filter=filter_obj
        )

        api_response = messaging_api.narrowcast(
            narrowcast_request=narrowcast_request
        )

        print("The response of MessagingApi->narrowcast:\n")
        print(api_response)

    except Exception as e:
        print(f"Exception when calling MessagingApi->narrowcast: {e}")
        raise


if __name__ == "__main__":
    COUPON_ID = "01KHNEBPAP6NG6GA9TB94NEHS5"
    narrowcast_coupon(COUPON_ID)
