from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import (
    App,
    Column,
    Columns,
    FilterMenu,
    FilterMenuActionCheckbox,
    FilterMenuActions,
    FilterMenus,
)

app_entry_point = AppEntryPoint(
    name='custom_app',
    description='App zum Testen',
    app=App(
        label='Elektronisches Laborbuch',
        path='lfl',
        category='Lehrstuhl fuer Laserphysik',
        description='Elektronisches Laborbuch des Lehrstuhls für Laserphysik',
        columns=Columns(
            selected=['entry_name','upload_create_time'],
            options={
                'entry_name': Column(),
                'upload_create_time': Column(),
            },
        ),
        filter_menus=FilterMenus(
            options={
                'schoener_peak': FilterMenu(
                    label='Schoener Peak', actions=FilterMenuActions(
                        options={"Kategorie1":FilterMenuActionCheckbox(
                            type="checkbox",label="irgendwas",quantity="entry_id"
                            )
                        }
                    )
                ),
                'gute_messung': FilterMenu(label='Gute Messung'),
            }
        ),
    ),
)
