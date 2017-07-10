import logging
import platform


from provision.profile import Profile


class atom(Profile):
    software = []

    class Meta:
        description = "Atom Installer \w atom cli + apm cli"
        downloads = {
            'mac': 'http://atom.io/download/mac'
        }
        software = {}
        requires = []

    def install_construct(self):
        logging.info('Installing {}'.format(self.__class__.__name__))

    def install(self):
        if platform.system() == 'Darwin':
            self.move(self.downloads.mac.unzip() + '/*', '/Applications/')
            self.system('ln -s /Applications/Atom.app/Contents/Resources/app/atom.sh /usr/local/bin/atom')
            self.system('ln -s /Applications/Atom.app/Contents/Resources/app/apm/bin/apm /usr/local/bin/apm')

    def install_desconstructor(self):
        logging.info('Finished installing {}'.format(self.__class__.__name__))


if __name__ == "__main__":
    profile = atom()
    profile.run()
