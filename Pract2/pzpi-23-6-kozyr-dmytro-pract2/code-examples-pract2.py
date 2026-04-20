class DeviceKeyService:
    def get_recipient_devices(self, recipient_id):
        return [
            {"device_id": "phone", "public_key": "pk_phone"},
            {"device_id": "laptop", "public_key": "pk_laptop"},
            {"device_id": "tablet", "public_key": "pk_tablet"},
        ]


class EncryptionService:
    def encrypt_for_device(self, plaintext, public_key):
        return f"encrypted({plaintext})_for_{public_key}"


class DeliveryService:
    def deliver(self, recipient_id, device_id, ciphertext):
        print(f"Send to {recipient_id}:{device_id} -> {ciphertext}")


def send_message_multi_device(sender_id, recipient_id, plaintext):
    device_service = DeviceKeyService()
    crypto = EncryptionService()
    delivery = DeliveryService()

    recipient_devices = device_service.get_recipient_devices(recipient_id)

    for device in recipient_devices:
        ciphertext = crypto.encrypt_for_device(
            plaintext,
            device["public_key"]
        )
        delivery.deliver(recipient_id, device["device_id"], ciphertext)


send_message_multi_device("user_A", "user_B", "Привіт!")