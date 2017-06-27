import logging

from provision.profile import Profile


class node(Profile):
    software = []

    class Meta:
        description = "Profile for installing npm."
        homepage = "https://www.npmjs.com/"
        downloads = {}
        #requires = ['Bioto/profiles/atom']

    def install_construct(self):
        logging.info('Installing {}'.format(self.__class__.__name__))

    def install(self):
        return self.install_package('brew', 'node')

    def install_linux(self):
        return self.install_package(['pacman', 'yum'],
                                    ['nodejs', 'npm'])

    def install_desconstructor(self):
        logging.info('Finished installing {}'.format(self.__class__.__name__))


if __name__ == "__main__":
    a = node()
    a.run()
