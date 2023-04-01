class SymmetricEncryption:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        encoded_key = self.key.encode('utf-8')
        plaintext_bytes = plaintext.encode('utf-8')
        key_len = len(encoded_key)
        cipher = bytearray(plaintext_bytes)
        for i, val in enumerate(plaintext_bytes):
            cipher[i] ^= encoded_key[i % key_len]
        return cipher

    def decrypt(self, ciphertext):
        encoded_key = self.key.encode('utf-8')
        key_len = len(encoded_key)
        plaintext_bytes = bytearray(ciphertext)
        for i, val in enumerate(ciphertext):
            plaintext_bytes[i] ^= encoded_key[i % key_len]
        return plaintext_bytes.decode('utf-8')
