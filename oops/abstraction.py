import sys
from mail_service import MailService

def main(args):
    ms = MailService()
    ms.sendEmail()

if __name__ == '__main__':
    main(sys.argv[1:])    