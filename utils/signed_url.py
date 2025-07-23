from django.core.signing import TimestampSigner, BadSignature, SignatureExpired

signer = TimestampSigner()

def generate_signed_token(video_uid):
    return signer.sign(video_uid)

def verify_signed_token(token, max_age=600):  # 600 = 10 minutes validity
    try:
        return signer.unsign(token, max_age=max_age)
    except (BadSignature, SignatureExpired):
        return None
