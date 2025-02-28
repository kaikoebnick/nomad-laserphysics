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
    MenuItemOption,
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
    upload_ids = _plugins['entry_points']['options']['nomad_laserphysics.apps:measurements_app_entry_point'][
        'upload_ids'
    ]
except KeyError:
    upload_ids = None

if upload_ids:
    filters_locked = {
        'upload_id': upload_ids,
        'section_defs.definition_qualified_name': [
            'nomad_laserphysics.schema_packages.measurement.Measurement',
        ],
    }
else:
    filters_locked = {
        'section_defs.definition_qualified_name': [
           'nomad_laserphysics.schema_packages.measurement.Measurement',
        ]
    }

Measurements = App(
    label='Measurments app',
    description='Search Laserphysics measurements',
    path='measurements',
    category='Chair for Laserphysics',
    filters=Filters(
        include=[
            '*#nomad_laserphysics.schema_packages.measurement.Measurement',
            '*#nomad_laserphysics.schema_packages.FEM_correlation_chamber.FEMCorrelationChamber',
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
    ],

    menu=Menu(
        title='filter-menu',
        items=[
            MenuItemHistogram(
                title='date of the last update',
                x='upload_create_time',
            ),
            Menu(
                title='FEM Correlation Chamber',
                items=[
                    MenuItemTerms(
                        title='kind',
                        search_quantity='entry_type',
                        options={'FEMCorrelationChamber': MenuItemOption(
                                label='FEM Correlation Chamber'
                            )
                        },
                        show_input=False
                    ),
                    MenuItemTerms(
                        title='measurement type',
                        search_quantity='data.measurement_type#nomad_laserphysics.schema_packages.FEM_correlation_chamber.FEMCorrelationChamber'
                    ),
                    MenuItemHistogram(
                        title='measurement number of that type',
                        x='data.measurement_number_of_that_type#nomad_laserphysics.schema_packages.FEM_Correlation_chamber.FEMCorrelationChamber'
                    ),
                    Menu(
                        title='tags',
                        items=[
                            MenuItemTerms(
                                title='tags',
                                search_quantity='data.tags.tag#nomad_laserphysics.schema_packages.FEM_correlation_chamber.FEMCorrelationChamber'
                            ),
                        ],
                    ),
                    Menu(
                        title='values',
                        items=[
                            MenuItemHistogram(
                                x='data.voltage#nomad_laserphysics.schema_packages.FEM_Correlation_chamber.FEMCorrelationChamber',
                            ),
                            MenuItemHistogram(
                                x='data.laserpower#nomad_laserphysics.schema_packages.FEM_Correlation_chamber.FEMCorrelationChamber',
                            ),
                            MenuItemHistogram(
                                x='data.wavelength#nomad_laserphysics.schema_packages.FEM_Correlation_chamber.FEMCorrelationChamber',
                            ),
                            MenuItemHistogram(
                                x='data.u_p#nomad_laserphysics.schema_packages.FEM_correlation_chamber.FEMCorrelationChamber',
                            ),
                        ],
                    ),
                ],
            ),
            Menu(
                title='FIM Test Chamber',
                items=[
                    MenuItemTerms(
                        title='kind',
                        search_quantity='entry_type',
                        options={'FIMTestChamber': MenuItemOption(
                                label='FIM Test Chamber'
                            )
                        },
                        show_input=False
                    ),
                    MenuItemTerms(
                        title='measurement type',
                        search_quantity='data.measurement_type#nomad_laserphysics.schema_packages.FIM_test_chamber.FIMTestChamber'
                    ),
                    MenuItemHistogram(
                        title='measurement number of that type',
                        x='data.measurement_number_of_that_type#nomad_laserphysics.schema_packages.FIM_test_chamber.FIMTestChamber'
                    ),
                    Menu(
                        title='tags',
                        items=[
                            MenuItemTerms(
                                title='tags',
                                search_quantity='data.tags.tag#nomad_laserphysics.schema_packages.FIM_test_chamber.FIMTestChamber'
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
                ],
            ),
            #Menu(
            #    title='objects',
            #    items=[
            #    ],
            #),
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
