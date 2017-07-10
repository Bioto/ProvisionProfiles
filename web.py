import logging

from provision.profile import Profile


class web(Profile):
    software = []

    class Meta:
        description = "My custom profile for installing my web development environment"
        downloads = {}
        software = {
            'brew': [
                ('install', 'node', ()),
                ('install', 'postgres', ())
            ],
            'npm': [
                ('install', 'gulp', ('-g', ))
            ]
        }
        requires = [
            ('https://github.com/Bioto/ProvisionProfiles', 'atom')
        ]

    def install_construct(self):
        logging.info('Installing {}'.format(self.__class__.__name__))

    def install(self):
        logging.info('Installing atom packages...')

        self.packages('install', [
            ('apm', 'Sublime-Style-Column-Selection', ()),
            ('apm', 'atom-beautify', ()),
            ('apm', 'atom-typescript', ()),
            ('apm', 'emmet', ())
        ])

    def install_desconstructor(self):
        logging.info('Finished installing {}'.format(self.__class__.__name__))


if __name__ == "__main__":
    runner = web()
    runner.run()
