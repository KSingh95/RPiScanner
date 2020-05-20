import os
import subprocess
import sys
import re

from blogsite import models


class wifi_scans:
    def __init__(self):
        self.data = os.popen('nmcli device wifi' + ' '.join(sys.argv[1:]))
        self.lines =self.data.readlines()
        self.s = []
        self.d = {}
        self.num_of_lines=len(self.lines)

    def get_scans(self):
        for i in range(0, self.num_of_lines):
            self.s.append(list(filter(None, self.lines[i].split('  '))))
            print(self.s)
            if i > 0:
                self.d['SSID'] = self.s[i][1]
                self.d['CHAN'] = self.s[i][3]
                self.d['SIGNAL']=self.s[i][5]
        return self.d

    # def wifi_all(self):
    #     Data.save_to_sql( table_name, d)
    #
    # def insert_to_sql(self, table_name, d):
    #     __tablename__ == wifi_data
    #     data = Data(self.d['SSID'], self.d['CHAN'], self.d['SIGNAL'])
    #     db.session.add(data)
    #     db.session.commit()
    @staticmethod
    def view_all():
        wifi_data = models.wifi.query.all()
        return wifi_data