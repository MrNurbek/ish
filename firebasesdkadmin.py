import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

cred = credentials.Certificate('firebase-sdk.json')  # Maxfiy kalit faylining yo'li
firebase_admin.initialize_app(cred)


def send_firebase_message(firebase_token, title, body):
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
# firebase_token = 'dC28nelZZ8OLShGvEkH2mS:APA91bGIvJ8eGkx2mRKwetWhAl514w4C0q8Q9s2nAHKvIRCiZW9lZBdNJldzv6MSwS3G0AymYmyyBbQFaPSkIR7XZMNwD7BK032sCdcCo_-RN2rzWaTJ2ePd9NbLARzQn4jzL4J931Pp'
# firebase_token = 'db_U1ph4IV9BSnzf8C9-b3:APA91bHC7tPaZi9BcGrHzb_LCfkmMH9YInqm4UR7CXAIeXDtKIdA8Af-eNj4In3ZMNUeJRpdAwUN0jxTEWcNcFZxy7ycWb7CsjeM7WuVuIxhh_-PHfgVruu2TCDxs6C5SynWVRtP2smw'
# title = 'Yangi Xabar'
# body = 'Bu sizning birinchi Firebase xabaringiz!'
# response = send_firebase_message(firebase_token, title, body)
# print(response, 'ssssssssssssssssssssssssss')
