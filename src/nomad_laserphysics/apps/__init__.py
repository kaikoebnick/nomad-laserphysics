# ruff: noqa: E501
from nomad.config import _plugins
from nomad.config.models.plugins import AppEntryPoint
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
    upload_ids = _plugins['entry_points']['options']['nomad_laserphysics.apps:app_entry_point'][
        'upload_ids'
    ]
except KeyError:
    upload_ids = None

if upload_ids:
    filters_locked = {
        'upload_id': upload_ids,
        'section_defs.definition_qualified_name': [
            'nomad_laserphysics.schema_packages.FEM_correlation_chamber_schema.FEMCorrelationChamber'
        ],
    }
else:
    filters_locked = {
        'section_defs.definition_qualified_name': [
           'nomad_laserphysics.schema_packages.FEM_correlation_chamber_schema.FEMCorrelationChamber'
        ]
    }

app_entry_point = AppEntryPoint(
    name='Laserphysics',
    description='App defined using the new plugin mechanism.',
    app=App(
        label='Laserphysics',
        description='Search Laserphysics notebooks',
        path='laserphysics',
        category='Chair for Laserphysics',
        filters=Filters(
            include=['*#nomad_laserphysics.schema_packages.FEM_correlation_chamber_schema.FEMCorrelationChamber'],
        ),
        filters_locked=filters_locked,

        columns=[
            Column(search_quantity='entry_id'),
            Column(search_quantity='entry_type', align=AlignEnum.LEFT),
            Column(search_quantity='authors', align=AlignEnum.LEFT, selected=True),
            Column(search_quantity='data.name#nomad_laserphysics.schema_packages.FEM_correlation_chamber_schema.FEMCorrelationChamber',
                label='Name', align=AlignEnum.LEFT, selected=True
            ),
            Column(search_quantity='data.category#nomad_laserphysics.schema_packages.FEM_correlation_chamber_schema.FEMCorrelationChamber',
                label='Category', selected=True
            ),
            Column(search_quantity='data.date#nomad_laserphysics.schema_packages.FEM_correlation_chamber_schema.FEMCorrelationChamber',
                label='Measurement date',
                align=AlignEnum.LEFT,
                format=Format(mode=ModeEnum.DATE),
                selected=True
            ),
            Column(search_quantity='data.measurement.voltage#nomad_laserphysics.schema_packages.FEM_correlation_chamber_schema.FEMCorrelationChamber'),
            Column(search_quantity='data.measurement.laserpower#nomad_laserphysics.schema_packages.FEM_correlation_chamber_schema.FEMCorrelationChamber'),
            Column(search_quantity='data.measurement.wavelength#nomad_laserphysics.schema_packages.FEM_correlation_chamber_schema.FEMCorrelationChamber'),
            Column(search_quantity='data.measurement.u_p#nomad_laserphysics.schema_packages.FEM_correlation_chamber_schema.FEMCorrelationChamber'),
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
                        MenuItemTerms(
                          title='category',
                         search_quantity='data.category#nomad_laserphysics.schema_packages.FEM_correlation_chamber_schema.FEMCorrelationChamber',
                        ),
                        MenuItemTerms(
                          title='author\'s first name',
                         search_quantity='data.authors.first_name#nomad_laserphysics.schema_packages.FEM_correlation_chamber_schema.FEMCorrelationChamber',
                        ),
                        MenuItemTerms(
                          title='author\'s last name',
                         search_quantity='data.authors.last_name#nomad_laserphysics.schema_packages.FEM_correlation_chamber_schema.FEMCorrelationChamber',
                        ),
                    ],
                ),
                Menu(
                    title='values',
                    items=[
                        MenuItemHistogram(
                            x='data.measurement.voltage#nomad_laserphysics.schema_packages.FEM_correlation_chamber_schema.FEMCorrelationChamber',
                        ),
                        MenuItemHistogram(
                            x='data.measurement.laserpower#nomad_laserphysics.schema_packages.FEM_correlation_chamber_schema.FEMCorrelationChamber',
                        ),
                        MenuItemHistogram(
                            x='data.measurement.wavelength#nomad_laserphysics.schema_packages.FEM_correlation_chamber_schema.FEMCorrelationChamber',
                        ),
                    ],
                ),
                Menu(
                    title='tags',
                    items=[
                        MenuItemTerms(
                            title='tags',
                            search_quantity='data.measurement.tags.tag#nomad_laserphysics.schema_packages.FEM_correlation_chamber_schema.FEMCorrelationChamber'
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
    ),
)
