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
        label='Electronic laboratory notebook',
        path='enl_laserphysics',
        category='Chair for Laserphysics',
        description='ELN of the Chair for Laser Physics"',
        columns=Columns(
            selected=['entry_name','upload_create_time'],
            options={
                'entry_name': Column(),
                'upload_create_time': Column(),
            },
        ),
        filter_menus=FilterMenus(
            options={
                'calibration': FilterMenu(
                    label='entry_name', actions=FilterMenuActions(
                        options={"Kategorie1":FilterMenuActionCheckbox(
                            type="checkbox",label="some_quantity",quantity="entry_id"
                            )
                        }
                    )
                ),
                'entry_id': FilterMenu(label='real_measurement'),
            }
        ),
    ),
)
