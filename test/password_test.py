from unittest import TestCase
from unittest.mock import Mock, patch

from anubis.core.password import PasswordProvider


class TestPasswordProviderGetPassword(TestCase):

    def test_should_succeed_without_cached_password(self):
        input_password = "input-password"
        password_repository = Mock()
        password_repository.get = Mock()
        password_repository.get.side_effect = [None, "input-password"]
        password_repository.save = Mock()
        password_input = Mock(return_value=input_password)

        under_test = PasswordProvider(password_repository = password_repository, password_input = lambda: password_input())
        result = under_test.get_password()

        assert result == input_password
        password_repository.get.assert_called()
        password_repository.save.assert_called_once()
        password_input.assert_called_once()

    def test_should_succeed_with_cached_password(self):
        input_password = "input-password"
        password_repository = Mock()
        password_repository.get = Mock(return_value=input_password)
        password_repository.save = Mock()
        password_input = Mock()

        under_test = PasswordProvider(password_repository = password_repository, password_input = lambda: password_input)
        result = under_test.get_password()

        assert result == input_password
        password_repository.get.assert_called()
        password_repository.save.assert_not_called()
        password_input.assert_not_called()