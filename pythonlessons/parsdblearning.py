

#!/usr/bin/env python
# -*-coding : utf-8-*-
import odoorpc
import argparse
import boto3


def createParser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-db', '--db_name', default='default_name',
        help="Database name| --db_name=<your_db_name>"
    )
    parser.add_argument(
        '-p', '--password', default='admin',
        help="Database password| --password=<your_password>"
    )

    return parser


# data for creating database
data = createParser().parse_args()

# Odoo connection
SUPER_PWD = 'admin'
HOST = 'localhost'
PORT = 8069
DB = data.db_name
USER = 'admin'
PWD = data.password
LANG = 'eu_US'
# COMPANY = u"TEST COMPANY"
# TIMEZONE = u"Europe/Paris"
MODULES_TO_INSTALL = [
    # 'sale'
]


def get_session(login=True):
    odoo = odoorpc.ODOO(HOST, port=PORT)
    odoorpc.config['timeout'] = None
    if login:
        odoo.login(DB, USER, PWD)
    return odoo


def create_database():
    odoo = get_session(login=False)
    if DB not in odoo.db.list():
        odoo.db.create(
            SUPER_PWD, DB, demo=False, lang=LANG, admin_password=PWD)


def install_modules():
    odoo = get_session()
    # Installation
    Module = odoo.env['ir.module.module']
    for module_name in MODULES_TO_INSTALL:
        module_ids = Module.search(
            [('name', '=', module_name),
             ('state', 'not in', ['installed', 'to upgrade'])])
        if module_ids:
            Module.button_immediate_install(module_ids)


def create_domain():
    client = boto3.client('route53')
    response = client.change_resource_record_sets(
        HostedZoneId='/hostedzone/Z02137002W3QGLFCS9R1V',
        ChangeBatch={
            'Comment': 'Creation Subdomain',
            'Changes': [
                {
                    'Action': 'CREATE',
                    'ResourceRecordSet': {
                        'Name': f'{DB}.ibdgestion.com',
                        'Type': 'A',
                        'TTL': 60,
                        'ResourceRecords': [
                            {
                                'Value': '18.205.25.249'
                            }
                        ]
                    }
                }
            ]
        }
    )


def main():
    create_database()
    create_domain()
    install_modules()


if __name__ == '__main__':
    main()
