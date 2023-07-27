"""
Generate TBS for Occupational Health data
"""
import pandas as pd
import flowsa

repo = 'https://github.com/ZhehanHuang/Occupational-health-calculation/raw/main/data/'
file = 'developed_dataset/Dataset%20of%20direct%20impact%20factors%20of%20occupational%20health%20impacts.xlsx'

year = '2018'

## USEEIO TBS format
cols = [
    'Sector',
    'SectorName',
    'Flowable',
    'Year',
    'FlowAmount',
    'DataReliability',
    'TemporalCorrelation',
    'GeographicalCorrelation',
    'TechnologicalCorrelation',
    'DataCollection',
    'Location',
    'Context',
    'Unit',
    'FlowUUID',
    'MetaSources',
    ]


def generate_OH_totals(file, year):
    df = (pd.read_excel(file, sheet_name=year)
          .filter(['USEEIO Code', 'Total Impact'])
          .assign(Sector = lambda x: x['USEEIO Code'].apply(str))
          .rename(columns={'Total Impact': 'FlowAmount'})
          .assign(Unit = 'DALY / $')
          .assign(Year = year)
          .assign(Flowable = 'Injury and illness')
          .assign(MetaSources = 'TBD')
          .assign(Location = 'US'))

    fba = (flowsa.getFlowByActivity('BEA_GDP_GrossOutput', year)
           .filter(['FlowAmount', 'ActivityProducedBy'])
           .rename(columns={'ActivityProducedBy': 'Sector',
                            'FlowAmount': 'Output'})
           )

    ## Multiple OH data (coefficients) by industry output
    df2 = (df.merge(fba, on='Sector')
           .assign(FlowAmount = lambda x: x['FlowAmount']*x['Output'])
           .assign(Unit = 'DALY')
           )
    return df2.reindex(columns=cols)

df_illness = generate_OH_totals(file=f'{repo}/{file}', year=year)
# df_illness.to_csv('')
