import logging

from provision.profile import Profile


class pythonserver(Profile):
    software = []

    class Meta:
        description = "My custom profile for installing my python server environment"
        downloads = {}
        software = {
            'brew': [
                ('install', 'postgres', ()),
                ('install', 'python3', ())
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
            ('apm', [
                'autocomplete-python',
                'linter-pylint'
            ], ()),
            ('pip', [
                'virtualenv',
                'virtualenvwrapper'
            ], ()),
            ('pip3', [
                'virtualenv',
                'virtualenvwrapper'
            ], ()),
        ])

    def install_desconstructor(self):
        logging.info('Finished installing {}'.format(self.__class__.__name__))


if __name__ == "__main__":
    runner = pythonserver()
    runner.run()
