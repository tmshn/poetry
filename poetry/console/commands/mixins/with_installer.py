from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from poetry.installation.installer import Installer


class WithInstaller(object):

    _installer = None

    @property
    def installer(self):  # type: () -> Installer
        return self._installer

    def set_installer(self, installer):  # type: (Installer) -> None
        self._installer = installer
