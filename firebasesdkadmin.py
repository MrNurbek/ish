import datetime
import firebase_admin
from firebase_admin import credentials, auth
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
# firebase_token = 'eFiLdzvySmmlghQ47Ox8DX:APA91bFOXN6XlPShA5_0wEqxDumzj04SXQUMLuW8q7wNnl5LvJIIUy_pPu7Nr2huSKpOM1JZ92Odpv6zlW-O7Mah2M9Go6ofmDh--q_lsfJbNkBro0A15L5ZB2pY82yivJk7SGZ0hi-Z'
# firebase_token = 'ePbe7B-0TkOHbff1HaMLEJ:APA91bF2EpmjUKiqF43mJSmde1l-YyTzrfxEBUIOgRuZ1kfTsOd-EuRfUPb6C8qqS7YEX7qO-dYFDVLsgTeI7xNBuyfgz3hW8JwCNrb7Y8BPo_Mq_X7TYMuCkjF6FAviOjUR-cjmbBtB'
# firebase_token = 'eFiLdzvySmmlghQ47Ox8DX:APA91bFOXN6XlPShA5_0wEqxDumzj04SXQUMLuW8q7wNnl5LvJIIUy_pPu7Nr2huSKpOM1JZ92Odpv6zlW-O7Mah2M9Go6ofmDh--q_lsfJbNkBro0A15L5ZB2pY82yivJk7SGZ0hi-Z'
# firebase_token = 'ejCBwuRJTja012XxyVTU0Y:APA91bEJ4t1mADDGrJPMAxdOmbH4rd3H8rbQlWY3sE2hNPvjLpWP1VRCdG1bFFx9EYMmIkbeyOICzthX7t7nqTn3ZdZOymwDxJRPAZIK782QST_UV8Vkwx-wV_n8-5bglAaJJZLJxN_z'
# firebase_token = 'erhwsPnDTjeLmjfyJ8zRI_:APA91bEtM2Z-AUc4xnC1g0QVJPRYg_KZtpAvJ5oahxoKErKJpovHWuD3BPSBvwPJnEZ5IGPsBrfBP1_6BLrlK3ILZUnAOb9Of7szAXtDFlwbYWZdoOmzWCEVNYSmJknxPTvnoW7iSQL0'
# firebase_token = 'eFiLdzvySmmlghQ47Ox8DX:APA91bFOXN6XlPShA5_0wEqxDumzj04SXQUMLuW8q7wNnl5LvJIIUy_pPu7Nr2huSKpOM1JZ92Odpv6zlW-O7Mah2M9Go6ofmDh--q_lsfJbNkBro0A15L5ZB2pY82yivJk7SGZ0hi-Z'
# decoded_token = auth.verify_id_token(firebase_token)
# title = 'Yangi Xabar'
# body = 'Bu sizning birinchi Firebase xabaringiz!'
# response = send_firebase_message(firebase_token, title, body)
# print(response, 'ssssssssssssssssssssssssss')
