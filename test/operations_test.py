from unittest import TestCase, expectedFailure
from unittest.mock import Mock

from olisipo.data import Secret
from olisipo.operations import Operations


class TestAddEntry(TestCase):

    def test_should_succeed_adding_new_entry(self):
        mocked_repository = Mock()
        mocked_repository.save = Mock(return_value=None)
        mocked_encryption_engine = Mock()
        mocked_encryption_engine.encrypt = Mock(return_value="encrypted-value")
        mocked_password_provider = Mock(return_value="password-value")

        under_test = Operations(
            repository = mocked_repository,
            encryption_engine=mocked_encryption_engine,
            password_provider=mocked_password_provider
        )
        under_test.add_entry(Secret(name="test-name", value="test-value"))

        mocked_repository.save.assert_called_once()
        mocked_encryption_engine.encrypt.assert_called_once()
        mocked_password_provider.assert_called_once()

    def test_should_fail_null_entry(self):
        mocked_repository = Mock()
        mocked_encryption_engine = Mock()
        mocked_password_provider = Mock(return_value="password-value")

        under_test = Operations(
            repository=mocked_repository,
            encryption_engine=mocked_encryption_engine,
            password_provider=mocked_password_provider
        )

        self.assertRaises(AssertionError, lambda: under_test.add_entry(secret=None))


class TestGetEntry(TestCase):

    def test_should_succeed_get_new_entry(self):
        db_result = Secret(name="test-name", value="encrypted_value")
        mocked_repository = Mock()
        mocked_repository.get = Mock(return_value=db_result)
        mocked_encryption_engine = Mock()
        mocked_encryption_engine.decrypt = Mock(return_value="decrypted_value")
        mocked_password_provider = Mock(return_value="password_value")

        under_test = Operations(
            repository=mocked_repository,
            encryption_engine=mocked_encryption_engine,
            password_provider=mocked_password_provider
        )
        result = under_test.get_entry(secret_id=db_result.name)

        self.assertEqual(result.name, db_result.name)
        self.assertEqual(result.value, "decrypted_value")

        mocked_repository.get.assert_called_once()
        mocked_encryption_engine.decrypt.assert_called_once()
        mocked_password_provider.assert_called_once()

    def test_should_succeed_null_entry(self):
        mocked_repository = Mock()
        mocked_encryption_engine = Mock()
        mocked_password_provider = Mock(return_value="password_value")

        under_test = Operations(
            repository=mocked_repository,
            encryption_engine=mocked_encryption_engine,
            password_provider=mocked_password_provider
        )
        self.assertRaises(AssertionError, lambda: under_test.get_entry(secret_id=None))


class TestRemoveEntry(TestCase):

    def test_should_succeed_remove_new_entry(self):
        mocked_repository = Mock()
        mocked_repository.delete = Mock()
        mocked_encryption_engine = Mock()
        mocked_password_provider = Mock()

        under_test = Operations(
            repository=mocked_repository,
            encryption_engine=mocked_encryption_engine,
            password_provider=mocked_password_provider
        )
        under_test.remove_entry(secret_id="key")

        mocked_repository.delete.assert_called_once()

    def test_should_succeed_null_entry(self):
        mocked_repository = Mock()
        mocked_repository.delete = Mock()
        mocked_encryption_engine = Mock()
        mocked_password_provider = Mock()

        under_test = Operations(
            repository=mocked_repository,
            encryption_engine=mocked_encryption_engine,
            password_provider=mocked_password_provider
        )
        self.assertRaises(AssertionError, lambda: under_test.remove_entry(secret_id=None))
