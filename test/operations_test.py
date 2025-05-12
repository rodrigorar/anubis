from unittest import TestCase
from unittest.mock import Mock

from anubis.core.secrets import Secret
from anubis.core.operations import Operations


class TestAddEntry(TestCase):

    def test_should_succeed_adding_new_entry(self):
        mocked_repository = Mock()
        mocked_repository.save = Mock(return_value=None)
        mocked_encryption_engine = Mock()
        mocked_encryption_engine.encrypt = Mock(return_value="encrypted-value")
        mocked_password_provider = Mock()
        mocked_password_provider.get_password = Mock(return_value="password-value")

        under_test = Operations(
            repository = mocked_repository,
            encryption_engine=mocked_encryption_engine,
            password_provider=mocked_password_provider
        )
        under_test.add_entry(Secret(name="test-name", value="test-value"))

        mocked_repository.save.assert_called_once()
        mocked_encryption_engine.encrypt.assert_called_once()
        mocked_password_provider.get_password.assert_called_once()

    def test_should_fail_null_entry(self):
        mocked_repository = Mock()
        mocked_encryption_engine = Mock()
        mocked_password_provider = Mock()
        mocked_password_provider.get_password = Mock(return_value="password-value")

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
        mocked_password_provider = Mock()
        mocked_password_provider.get_password = Mock(return_value="password-value")

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
        mocked_password_provider.get_password.assert_called_once()

    def test_should_succeed_null_entry(self):
        mocked_repository = Mock()
        mocked_encryption_engine = Mock()
        mocked_password_provider = Mock()
        mocked_password_provider.get_password = Mock(return_value="password-value")

        under_test = Operations(
            repository=mocked_repository,
            encryption_engine=mocked_encryption_engine,
            password_provider=mocked_password_provider
        )
        self.assertRaises(AssertionError, lambda: under_test.get_entry(secret_id=None))


class TestListEntries(TestCase):

    def test_should_succeed_list_entries(self):
        db_result = [
            Secret(name="test_entry_1", value="encrypted_entry_1"),
            Secret(name="test_entry_2", value="encrypted_entry_2"),
            Secret(name="test_entry_3", value="encrypted_entry_3")
        ]

        mocked_repository = Mock()
        mocked_repository.list = Mock(return_value=db_result)
        mocked_encryption_engine = Mock()
        mocked_password_provider = Mock()
        mocked_password_provider.get_password = Mock(return_value="password-value")

        under_test = Operations(
            repository=mocked_repository,
            encryption_engine=mocked_encryption_engine,
            password_provider=mocked_password_provider
        )
        result = under_test.list_entries()

        self.assertEqual(len(result), len(db_result))

        mocked_repository.list.assert_called_once()

    def test_should_succeed_empty_list(self):
        mocked_repository = Mock()
        mocked_repository.list = Mock(return_value=[])
        mocked_encryption_engine = Mock()
        mocked_password_provider = Mock()
        mocked_password_provider.get_password = Mock(return_value="password-value")

        under_test = Operations(
            repository=mocked_repository,
            encryption_engine=mocked_encryption_engine,
            password_provider=mocked_password_provider
        )
        result = under_test.list_entries()

        self.assertTrue(len(result) == 0)

        mocked_repository.list.assert_called_once()



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
