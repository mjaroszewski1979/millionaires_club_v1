import pandas_datareader as pdr
import numpy as np
from threading import Thread

# Creating a base class
class CpiData:
    def __init__(self):

        self.cpi = []
        
        # Countries and associated symbols 
        self.countries = {
        'UNITED STATES' : 'ticker=CPIUS',
        'CHINA' : 'ticker=CPICN',
        'JAPAN' : 'ticker=CPIJP',
        'GERMANY' : 'ticker=CPIDE',
        'FRANCE' : 'ticker=CPIFR',
        'INDIA' : 'ticker=CPIIN',
        'ITALY' : 'ticker=CPIIT',
        'BRAZIL' : 'ticker=CPIBR', 
        'SOUTH KOREA' : 'ticker=CPIKR',
        'CANADA' : 'ticker=CPICA',
        'RUSSIAN FEDERATION' : 'ticker=CPIRU',
        'SPAIN' : 'ticker=CPIES',
        'MEXICO' : 'ticker=CPIMX',
        'INDONESIA' : 'ticker=CPIID',
        'NETHERLANDS' : 'ticker=CPINL',
        'SAUDI ARABIA' : 'ticker=CPISA',
        'TURKEY' : 'ticker=CPITR',
        'SWITZERLAND' : 'ticker=CPICH',
        'TAIWAN' : 'ticker=CPITW',
        'POLAND' : 'ticker=CPIPL',
        'SWEDEN' : 'ticker=CPISE',
        'BELGIUM' : 'ticker=CPIBE',
        'ARGENTINA' : 'ticker=CPIAR',
        'THAILAND' : 'ticker=CPITH',
        'AUSTRIA' : 'ticker=CPIAT',
        'IRAN' : 'ticker=CPIIR',
        'NORWAY' : 'ticker=CPINO',
        'UNITED ARAB EMIRATES' : 'ticker=CPIAE',
        'NIGERIA' : 'ticker=CPING',
        'IRELAND' : 'ticker=CPIIE',
        'ISRAEL' : 'ticker=CPIIL',
        'SOUTH AFRICA' : 'ticker=CPIZA',
        'SINGAPORE' : 'ticker=CPISG',
        'HONG KONG' : 'ticker=CPIHK',
        'MALAYSIA' : 'ticker=CPIMY',
        'DENMARK' : 'ticker=CPIDK',
        'COLOMBIA' : 'ticker=CPICO',
        'PHILIPPINES' : 'ticker=CPIPH',
        'PAKISTAN' : 'ticker=CPIPK',
        'CHILE' : 'ticker=CPICL',
        'BANGLADESH' : 'ticker=CPIBD',
        'FINLAND' : 'ticker=CPIFI',
        'EGYPT' : 'ticker=CPIEG',
        'CZECH REPUBLIC' : 'ticker=CPICZ',
        'VIETNAM' : 'ticker=CPIVN',
        'PORTUGAL' : 'ticker=CPIPT',
        'ROMANIA' : 'ticker=CPIRO',
        'PERU' : 'ticker=CPIPE',
        'IRAQ' : 'ticker=CPIIQ',
        'GREECE' : 'ticker=CPIGR',
        'QATAR' : 'ticker=CPIQA',
        'ALGERIA' : 'ticker=CPIDZ',
        'KAZAKHSTAN' : 'ticker=CPIKZ',
        'HUNGARY' : 'ticker=CPIHU',
        'KUWAIT' : 'ticker=CPIKW',
        'UKRAINE' : 'ticker=CPIUA',
        'MOROCCO' : 'ticker=CPIMA',
        'ECUADOR' : 'ticker=CPIEC',
        'SLOVAKIA' : 'ticker=CPISK',
        'ANGOLA' : 'ticker=CPIAO',
        'VENEZUELA' : 'ticker=CPIVE',
        'SRI LANKA' : 'ticker=CPILK',
        'KENYA' : 'ticker=CPIKE',
        'DOMINICAN REPUBLIC' : 'ticker=CPIDO',
        'ETHIOPIA' : 'ticker=CPIET',
        'OMAN' : 'ticker=CPIOM',
        'GUATEMALA' : 'ticker=CPIGT',
        'LUXEMBOURG' : 'ticker=CPILU',
        'MYANMAR' : 'ticker=CPIMM',
        'GHANA' : 'ticker=CPIGH',
        'BULGARIA' : 'ticker=CPIBG',
        'PANAMA' : 'ticker=CPIPA',
        'CROATIA' : 'ticker=CPIHR',
        'URUGUAY' : 'ticker=CPIUY',
        'BELARUS' : 'ticker=CPIBY',
        'TANZANIA' : 'ticker=CPITZ',
        'LEBANON' : 'ticker=CPILB',
        'MACAO' : 'ticker=CPIMO',
        'SLOVENIA' : 'ticker=CPISI',
        'LITHUANIA' : 'ticker=CPILT',
        'UNITED KINGDOM' : 'ticker=CPIUK'
    }

    # Fetching data from Econdb API and returning current inflation pace
    def get_cpi_all(self, ticker):
        data = pdr.DataReader(ticker, 'econdb')
        data = data.values
        
        # Comparing latest reading with 1 year average
        if np.mean(data[-12:]) < data[-1]:
            return 'ABOVE ITS 12-MONTH AVERAGE INDICATING INFLATION'
        else:
            return 'BELOW ITS 12-MONTH AVERAGE INDICATING DEFLATION'

    def get_cpi(self, symbol):
        g5_countries  = {
                'ticker=CPICN' : 'CHINA',
                'ticker=CPIDE' : 'GERMANY',
                'ticker=CPIIN' : 'INDIA',
                'ticker=CPIJP' : 'JAPAN',
                'ticker=CPIUS' : 'UNITED STATES'
            }
        data = pdr.DataReader(symbol, 'econdb').values
        if np.mean(data[-12:]) < data[-1]:
            result = ['INFLATION', g5_countries[symbol]]
        else:
            result = ['DEFLATION', g5_countries[symbol]]
        if result not in self.cpi:
            self.cpi.append(result)
            self.cpi.sort(key=lambda x: x[1])

    # Creating individual thread for each call to Econdb API
    def get_cpi_g5(self):

        threads = []
        tickers = ['ticker=CPICN', 'ticker=CPIDE', 'ticker=CPIIN', 'ticker=CPIJP', 'ticker=CPIUS']


        for ticker in tickers:
            thread = Thread(target=self.get_cpi, args=[ticker])
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        return self.cpi
