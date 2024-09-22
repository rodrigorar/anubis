from unittest import TestCase

from olisipo.encryption import EncryptionEngine


class TestEncryptionDecryption(TestCase):

    def test_should_succeed_encrypting_a_value(self):
        test_password = "test_password"
        test_entry = "test_entry"

        under_test = EncryptionEngine()
        result = under_test.encrypt(test_entry, test_password)

        self.assertIsNotNone(result)
        self.assertNotEqual(test_entry, test_password)

    def test_should_succeed_differing_result_for_differing_passwords(self):
        test_password_1 = "test_password_1"
        test_password_2 = "test_password_2"
        test_entry = "test_entry"

        under_test = EncryptionEngine()
        result_1 = under_test.encrypt(test_entry, test_password_1)
        result_2 = under_test.encrypt(test_entry, test_password_2)

        self.assertIsNotNone(result_1)
        self.assertIsNotNone(result_2)
        self.assertNotEqual(test_entry, result_1)
        self.assertNotEqual(test_entry, result_2)
        self.assertNotEqual(result_1, result_2)

    def test_should_succeed_decrypting_with_same_password(self):
        test_password = "test_password"
        test_entry = "test_entry"

        under_test = EncryptionEngine()
        encrypted_value = under_test.encrypt(test_entry, test_password)
        decrypted_value = under_test.encrypt(encrypted_value, test_password)

        self.assertNotEqual(test_entry, decrypted_value)

    def test_should_fail_decrypt_value_with_different_password(self):
        test_password_1 = "test_password_1"
        test_password_2 = "test_password_2"
        test_entry = "test_entry"

        under_test = EncryptionEngine()
        encrypted_value = under_test.encrypt(test_entry, test_password_1)
        decrypted_value = under_test.encrypt(encrypted_value, test_password_2)

        self.assertNotEqual(test_entry, decrypted_value)
