import logging

from provision.profile import Profile


class arch(Profile):
    class Meta:
        description = "Arch Installer"
        downloads = {}
        software = {}
        requires = []

    def install_construct(self):
        logging.info('Installing {}'.format(self.__class__.__name__))

    def install(self):
        logging.info('Starting installer')

        # Set the system time
        self.system('timedatectl set-ntp true')

        # Specify drive
        self.system('DRIVE=/dev/sda')

        # Format drive
        self.system('sudo dd if=/dev/zero of=$DRIVE bs=512 count=1')
        self.system('sudo parted --script -s $DRIVE mklabel gpt mkpart ' +
                    ' primary 1MiB 512MiB mkpart primary 512MiB 1024MiB ' +
                    'mkpart primary 1024MiB 6048MiB')
        self.system('sudo partprobe /dev/sda')
        self.system('sudo mkfs.ext2 /dev/sda1')
        self.system('sudo swapon /dev/sda2')
        self.system('sudo swapon /dev/sda2')
        self.system('sudo mkfs.ext4 /dev/sda3')
        self.system('sudo parted /dev/sda1 set 1 boot on')
        self.system('sudo partprobe /dev/sda')

        # Mount the drive
        self.system('mount /dev/sda3 /mnt')
        self.system('mkdir /mnt/boot')
        self.system('mount /dev/sda1 /mnt/boot')

        # Install Arch
        self.system('pacstrap /mnt base')
        self.system('genfstab -U /mnt >> /mnt/etc/fstab')
        self.system('arch-chroot /mnt')

        # Link
        self.system('ln -sf /usr/share/zoneinfo/US/Pacific /etc/localtime')
        self.system('hwclock --systohc')
        self.system('locale-gen')

        # Setup kernal
        self.system('sudo touch /etc/hostname')
        self.system('sudo echo "brain" > /etc/hostname')
        self.system('mkinitcpio -p linux')

        # Set root user
        self.system('echo "Please set your root password:"')
        self.system('passwd')

        # Install the things
        self.system('pacman -S syslinux gptfdisk')
        self.system('syslinux-install_update -i -a -m')

    def install_desconstructor(self):
        logging.info('Finished installing {}'.format(self.__class__.__name__))


if __name__ == "__main__":
    runner = arch()
    runner.run()
