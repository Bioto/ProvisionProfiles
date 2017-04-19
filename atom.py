import logging

from provision import distribution
from provision.tools import does_package_exist
from provision.managers.packages import Yum
from provision.profiles import BaseProfile


class atom(BaseProfile):
    software = []
#        {
#            'manager': 'yaourt',
#            'install': ['wget'],
#            'uninstall': ['wget']
#        }

    class Meta:
        description = "Profile for installing atom."
        homepage = "https://atom.io/"
        downloads = {
            'mac': 'http://atom.io/download/mac',
            'debian': 'https://atom.io/download/deb'
        }

    def install_pre(self):
        logging.info('Installing atom')

    def install_mac(self):
        self.move(self.downloads.mac.unzip(), '/Applications/')

    def install_linux(self):
        print(distribution)
        if distribution is 'arch':
            return self.install_package(['pacman'], 'atom')

        if does_package_exist('yum'):
            installer = Yum()
            installer._raw_install(self.downloads.debian)

        if any(x in distribution for x in ['debian', 'ubuntu']):
            self.system(
                'cd {} && dpkg -i {}'.format(self.downloads.debian.folder(),
                                             self.downloads.debian))

        return

    def install_post(self):
        logging.info('Finished installing atom')


if __name__ == "__main__":
    a = atom()
    a.run()
