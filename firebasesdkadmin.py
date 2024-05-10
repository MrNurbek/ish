import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

cred = credentials.Certificate('firebase-sdk.json')  # Maxfiy kalit faylining yo'li
firebase_admin.initialize_app(cred)


def send_firebase_message(firebase_token, firebase_token_front, title, body):
    # Xabar tuzilishi

    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        token=firebase_token,
        android=messaging.AndroidConfig(
            ttl=datetime.timedelta(seconds=3600),
            priority='high',
            notification=messaging.AndroidNotification(
                icon='stock_ticker_update',
                color='#f45342'
            ),
        ),
        apns=messaging.APNSConfig(
            payload=messaging.APNSPayload(
                aps=messaging.Aps(badge=42),
            ),
        ),
    )

    # Xabar yuborish
    response = messaging.send(message)
    return response


def send_firebase_message1(firebase_token_front, title, body):
    # Xabar tuzilishi

    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        token=firebase_token_front,
        android=messaging.AndroidConfig(
            ttl=datetime.timedelta(seconds=3600),
            priority='high',
            notification=messaging.AndroidNotification(
                icon='stock_ticker_update',
                color='#f45342'
            ),
        ),
        apns=messaging.APNSConfig(
            payload=messaging.APNSPayload(
                aps=messaging.Aps(badge=42),
            ),
        ),
    )

    # Xabar yuborish
    response = messaging.send(message)
    return response

# firebase_token = 'crIcQxyF1U_kToJXqRnK6L:APA91bFTzEd4xWGVm3KYANb0zFxecHHiKS41nfSPRVYqdVIX5xUi_hhcYRWj8JeBmCPBZUBxgabUPrGnmoNLR2IiXjmgxh51iOK4eGSnTvOo5KnDTJomLX2QKBze3XkCZrx4wNTZU25c'
# firebase_token = 'cTac_K0sQAuupIAM-AES87:APA91bGjMPhVruYx7odJpzLpc0HafmCEvPGLPVyKlLMo7u8Z4DRKQo_wWkAqW05aLxvkVyjHE88hk3WOn7m3nDIbY-kpObsJGN61CCIY4k79OkMKK_bmYscj1-F3UkosIeE2e7_oUuYo'
# firebase_token = 'crIcQxyF1U_kToJXqRnK6L:APA91bFTzEd4xWGVm3KYANb0zFxecHHiKS41nfSPRVYqdVIX5xUi_hhcYRWj8JeBmCPBZUBxgabUPrGnmoNLR2IiXjmgxh51iOK4eGSnTvOo5KnDTJomLX2QKBze3XkCZrx4wNTZU25c'
# title = 'Yangi Xabar'
# body = 'Bu sizning birinchi Firebase xabaringiz!'
# response = send_firebase_message(firebase_token, title, body)
# print(response, 'ssssssssssssssssssssssssss')
