from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import App, Column, Columns, FilterMenus, FilterMenu, FilterMenuActions, FilterMenuActionCheckbox

app_entry_point = AppEntryPoint(
    name='custom_app',
    description='Was abgespacetes.',
    app=App(
        label='Lehrstuhl fuer Laserphysik',
        path='lfl',
        category='Elektronisches Laborbuch',
        description='Elektronisches Laborbuch des Lehrstuhls für Laserphysik',
        columns=Columns(
            selected=['entry_name'],
            options={
                'entry_name': Column(),
            },
        ),
        filter_menus=FilterMenus(
            options={
                'schoener_peak': FilterMenu(label='Schoener Peak', actions=FilterMenuActions(options={"Kategorie1":FilterMenuActionCheckbox(type="checkbox",label="irgendwas",quantity="entry_id")})),
                'gute_messung': FilterMenu(label='Gute Messung'),
            }
        ),
    ),
)
