import hashlib
import qrcode

def generate_certificate_hash(application_id, applicant_name, instrument_type, instrument_id):
    certificate_data = (
        f"{application_id}-"
        f"{applicant_name}-"
        f"{instrument_type}-"
        f"{instrument_id}"
    )
    certificate_hash = hashlib.sha256(
        certificate_data.encode()
    ).hexdigest()
    return certificate_hash


def generate_qr_code(certificate_hash):
    qr = qrcode.make(certificate_hash)
    file_name = f"certificate_{certificate_hash[:8]}.png"
    qr.save(file_name)
    return file_name