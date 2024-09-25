from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import App, Column, Columns, FilterMenu, FilterMenus

app_entry_point = AppEntryPoint(
    name='custom_app',
    description='Was abgespacetes.',
    app=App(
        label='Lehrstuhl fuer Laserphysik',
        path='app',
        category='Elektronisches Laborbuch',
        description='Kurze Beschreibung',
        columns=Columns(
            selected=['entry_id'],
            options={
                'entry_id': Column(),
            },
        ),
        filter_menus=FilterMenus(
            options={
                'schoener_peak': FilterMenu(label='Schoener Peak'),
                'gute_messung': FilterMenu(label='Gute Messung'),
            }
        ),
    ),
)
