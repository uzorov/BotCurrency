import datetime
import sqlite3


class DBAdapter:
    connection = None

    def __init__(self):

        self.createDb()

    def createDb(self):
        connection = sqlite3.connect('currency.db')
        cursor = connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS USD (
        id INTEGER PRIMARY KEY,
        dateUpdate DATE NOT NULL,
        timeUpdate TIME NOT NULL,
        valToRub INTEGER NOT NULL
        )
        ''')
        connection.commit()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS CNY (
            id INTEGER PRIMARY KEY,
            dateUpdate DATE NOT NULL,
            timeUpdate TIME NOT NULL,
            valToRub DOUBLE NOT NULL
            )
            ''')
        connection.commit()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS CGN (
            id INTEGER PRIMARY KEY,
            dateUpdate DATE NOT NULL,
            timeUpdate TIME NOT NULL,
            valToRub DOUBLE NOT NULL
            )
            ''')
        connection.commit()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS STL (
            id INTEGER PRIMARY KEY,
            dateUpdate DATE NOT NULL,
            timeUpdate TIME NOT NULL,
            valToRub DOUBLE NOT NULL
            )
            ''')
        connection.commit()
        connection.close()

    def getCurrencyDataFromDb(self, currency):
        connection = sqlite3.connect('currency.db')
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {currency}')
        lis = cursor.fetchall()
        connection.close()
        return lis

    def getCurrencyValueFromDb(self, currency):
        connection = sqlite3.connect('currency.db')
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {currency}')
        lis = cursor.fetchall()
        connection.close()
        return lis[-1][3]

    def storeCurrency(self, currency, date, value):
        connection = sqlite3.connect('currency.db')
        cursor = connection.cursor()
        time = datetime.datetime.now().strftime("%H:%M:%S")
        cursor.execute(f'INSERT INTO {currency} (dateUpdate, timeUpdate , valToRub) VALUES (?, ?, ?)',
                       (date, time, value))
        connection.commit()
        connection.close()

    def clearDb(self):
        connection = sqlite3.connect('currency.db')
        cursor = connection.cursor()
        cursor.execute('DELETE FROM USD')
        cursor.execute('DELETE FROM CNY')
        cursor.execute('DELETE FROM CGN')
        cursor.execute('DELETE FROM STL')
        connection.commit()
        connection.close()

    def updateValue(self, title, value):
        # print("#", value, title)
        connection = sqlite3.connect('currency.db')
        cursor = connection.cursor()
        if not self.isExistForToday(title):
            self.storeCurrency(title, datetime.date.today(), value)
            return
        cursor.execute(f'UPDATE {title} SET valToRub = ? WHERE date = ?', (value, datetime.date.today()))
        cursor.execute(f'UPDATE {title} SET timeUpdate = ? WHERE date = ?',
                       (value, datetime.datetime.now().strftime("%H:%M:%S")))
        connection.commit()
        connection.close()

    def isExistForToday(self, currency):
        data = self.getCurrencyDataFromDb(currency)
        if len(data) != 0 and data[-1][1] == datetime.date.today():
            return True
        return False

    def fillDb(self):
        self.storeCurrency("USD", "01-02-2024", 89.67)
        self.storeCurrency("USD", "02-02-2024", 90.23)
        self.storeCurrency("USD", "03-02-2024", 90.67)
        self.storeCurrency("USD", "04-02-2024", 89.67)
        self.storeCurrency("USD", "05-02-2024", 89.67)
        self.storeCurrency("USD", "06-02-2024", 91.24)
        self.storeCurrency("USD", "07-02-2024", 90.68)
        self.storeCurrency("USD", "08-02-2024", 91.15)
        self.storeCurrency("USD", "09-02-2024", 91.26)

        self.storeCurrency("CNY", "01-02-2024", 12.46)
        self.storeCurrency("CNY", "02-02-2024", 12.56)
        self.storeCurrency("CNY", "03-02-2024", 12.6)
        self.storeCurrency("CNY", "04-02-2024", 12.61)
        self.storeCurrency("CNY", "05-02-2024", 12.62)
        self.storeCurrency("CNY", "06-02-2024", 12.63)
        self.storeCurrency("CNY", "07-02-2024", 12.59)
        self.storeCurrency("CNY", "08-02-2024", 12.65)
        self.storeCurrency("CNY", "09-02-2024", 12.64)

    def getMetalDataFomDb(self, metal):
        connection = sqlite3.connect('currency.db')
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {metal}')
        lis = cursor.fetchall()
        return lis