import logging

from provision.profile import Profile


class web(Profile):
    software = []

    class Meta:
        description = "My custom profile for installing my web development environment"

    def install_construct(self, resume):
        logging.info('Installing {}'.format(self.__class__.__name__))

    def install(self, resume):
        logging.info('Installing atom packages...')
        print(resume)
        
    def install_desconstructor(self, resume):
        logging.info('Finished installing {}'.format(self.__class__.__name__))


if __name__ == "__main__":
    runner = web()
    runner.run()
