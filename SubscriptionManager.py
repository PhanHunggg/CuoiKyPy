import json
import datetime

from prettytable import PrettyTable
class SubscriptionManager:
    def __init__(self):
        self.subscribers = []
        self.load_data()

    def load_data(self):
        try:
            with open('DuLieu.txt', 'r') as f:
                self.subscribers = json.load(f)
        except FileNotFoundError:
            self.subscribers = []

    def save_data(self):
        # write
        with open('DuLieu.txt', 'w') as f:
            json.dump(self.subscribers, f)

    def add_subscriber(self, subscriber):
        for s in self.subscribers:
            if s['SoDKy'] == subscriber.SoDKy:
                print("Error: Subscriber already exists.")
                return
        self.subscribers.append(subscriber.__dict__)
        self.save_data()

    def edit_subscriber(self, SoDKy, new_data):
        for s in self.subscribers:
            if s['SoDKy'] == SoDKy:
                s.update(new_data)
                self.save_data()
                return
        print("Error: Subscriber not found.")

    def delete_subscriber(self, SoDKy):
        self.subscribers = [s for s in self.subscribers if s['SoDKy'] != SoDKy]
        self.save_data()

    def view_subscribers_by_household_type(self, LoaiHo):
        subscribers = self.get_subscribers_by_household_type(LoaiHo)
        table = PrettyTable(['STT', 'SoDKy', 'HoTen', 'DateOfBirth', 'Phai', 'DiaChi', 'MaSoDienKe', 'DiaChiLapDat', 'LoaiHo'])
        for i, subscriber in enumerate(subscribers):
            table.add_row([i, subscriber['SoDKy'], subscriber['HoTen'], subscriber['DateOfBirth'], subscriber['Phai'], subscriber['DiaChi'], subscriber['MaSoDienKe'], subscriber['DiaChiLapDat'], subscriber['LoaiHo']])
        print(table)

    def view_raw_data(self):
        data = self.get_raw_data()
        # table = PrettyTable(['STT', 'SoDKy', 'HoTen', 'DateOfBirth', 'Phai', 'DiaChi', 'MaSoDienKe', 'DiaChiLapDat', 'LoaiHo'])
        # for i, item in enumerate(data):
        #     table.add_row([i, item['SoDKy'], item['HoTen'], item['DateOfBirth'], item['Phai'], item['DiaChi'], item['MaSoDienKe'], item['DiaChiLapDat'], item['LoaiHo']])
        print(data)
        

    def get_subscribers_by_household_type(self, LoaiHo):
        return [subscriber for subscriber in self.subscribers if subscriber['LoaiHo'] == LoaiHo]
    def get_raw_data(self):
        return self.subscribers
    
    @staticmethod
    def validate_date(date_text):
        try:
            datetime.datetime.strptime(date_text, '%d/%m/%Y')
            return True
        except ValueError:
            return False
        
    def validate_SoDKy(self, soDKy):
        for s in self.subscribers:
            if s['SoDKy'] == soDKy:
                return False
        return True