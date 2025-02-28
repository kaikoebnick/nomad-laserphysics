# ruff: noqa: E501
from nomad.config import _plugins
from nomad.config.models.ui import (
    AlignEnum,
    App,
    Column,
    Filters,
    Format,
    Menu,
    MenuItemCustomQuantities,
    MenuItemHistogram,
    MenuItemPeriodicTable,
    MenuItemTerms,
    MenuItemVisibility,
    ModeEnum,
    RowActions,
    RowActionURL,
    RowDetails,
    Rows,
    RowSelection,
)

# Workaround: read the upload_ids from plugin's raw config.
try:
    upload_ids = _plugins['entry_points']['options']['nomad_laserphysics.apps:FIM_test_chambers_app_entry_point'][
        'upload_ids'
    ]
except KeyError:
    upload_ids = None

if upload_ids:
    filters_locked = {
        'upload_id': upload_ids,
        'section_defs.definition_qualified_name': [
            'nomad_laserphysics.schema_packages.FIM_test_chamber.FIMTestChamber',
        ],
    }
else:
    filters_locked = {
        'section_defs.definition_qualified_name': [
           'nomad_laserphysics.schema_packages.FIM_test_chamber.FIMTestChamber',
        ]
    }

FIMTestChambers = App(
    label='FIM test chambers app',
    description='Search Laserphysics FIM test chamber measurements',
    path='FIM_test_chambers',
    category='Chair for Laserphysics',
    filters=Filters(
        include=[
            '*#nomad_laserphysics.schema_packages.FIM_test_chamber.FIMTestChamber',
            ],
    ),
    filters_locked=filters_locked,

    columns=[
        Column(search_quantity='entry_type', align=AlignEnum.LEFT),
        Column(search_quantity='authors', align=AlignEnum.LEFT, selected=True),
        Column(search_quantity='entry_name', align=AlignEnum.LEFT, selected=True
        ),
        Column(search_quantity='upload_create_time',
            align=AlignEnum.LEFT,
            format=Format(mode=ModeEnum.DATE),
            selected=True
        ),
        Column(search_quantity='data.voltage#nomad_laserphysics.schema_packages.FIM_test_chamber.FIMTestChamber'),
        Column(search_quantity='data.laserpower#nomad_laserphysics.schema_packages.FIM_test_chamber.FIMTestChamber'),
        Column(search_quantity='data.wavelength#nomad_laserphysics.schema_packages.FIM_test_chamber.FIMTestChamber'),
        Column(search_quantity='data.u_p#nomad_laserphysics.schema_packages.FIM_test_chamber.FIMTestChamber'),
    ],

    menu=Menu(
        title='filter-menu',
        items=[
            Menu(
                title='basic data',
                items=[
                    MenuItemHistogram(
                        title='date of the last update',
                        x='upload_create_time',
                    ),
                ],
            ),
            Menu(
                title='values',
                items=[
                    MenuItemHistogram(
                        x='data.voltage#nomad_laserphysics.schema_packages.FIM_test_chamber.FIMTestChamber',
                    ),
                    MenuItemHistogram(
                        x='data.laserpower#nomad_laserphysics.schema_packages.FIM_test_chamber.FIMTestChamber',
                    ),
                    MenuItemHistogram(
                        x='data.wavelength#nomad_laserphysics.schema_packages.FIM_test_chamber.FIMTestChamber',
                    ),
                    MenuItemHistogram(
                        x='data.u_p#nomad_laserphysics.schema_packages.FIM_test_chamber.FIMTestChamber',
                    ),
                ],
            ),
            Menu(
                title='tags',
                items=[
                    MenuItemTerms(
                        title='tags',
                        search_quantity='results.eln.tags'
                    ),
                ],
            ),
            Menu(
                title='elemental table',
                items=[
                    MenuItemPeriodicTable(
                    title='periodic table menu',
                    search_quantity='results.material.elements',
                    ),
                ],
            ),
            MenuItemVisibility(
                title='visibility',
            ),
            MenuItemCustomQuantities(
                title='custom quantities',
            ),
        ],
    ),

    rows=Rows(
        actions=RowActions(
            enabled=True,
            options={
                'launch': RowActionURL(
                    path="data.references[?kind=='hub'].uri",
                    description='Launch Jupyter notebook',
                )
            },
        ),
        details=RowDetails(enabled=True),
        selection=RowSelection(enabled=True),
    ),
)
