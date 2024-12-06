# ruff: noqa: E501
from nomad.config import _plugins
from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import (
    AlignEnum,
    App,
    #BreakpointEnum,
    Column,
    Columns,
    #Dashboard,
    #FilterMenu,
    #FilterMenus,
    #FilterMenuSizeEnum,
    Filters,
    Format,
    #Layout,
    Menu,
    MenuItemCustomQuantities,
    #MenuItemDefinitions,
    MenuItemHistogram,
    #MenuItemOptimade,
    #MenuItemOption,
    MenuItemPeriodicTable,
    MenuItemTerms,
    MenuItemVisibility,
    ModeEnum,
    RowActions,
    RowActionURL,
    RowDetails,
    Rows,
    RowSelection,
    #ScaleEnum,
    #WidgetPeriodicTable,
    #WidgetTerms,
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
            'nomad_laserphysics.schema_packages.schema_package.laserphysicsELN'
        ],
    }
else:
    filters_locked = {
        'section_defs.definition_qualified_name': [
           'nomad_laserphysics.schema_packages.schema_package.laserphysicsELN'
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
            include=['*#nomad_laserphysics.schema_packages.schema_package.laserphysicsELN'],
            #exclude=['*#nomad.datamodel.metainfo.eln.BasicEln'],
        ),
        filters_locked=filters_locked,

        columns=Columns(
            include=[
                'entry_id',
                'entry_type',
                'authors',
                'data.name#nomad_laserphysics.schema_packages.schema_package.laserphysicsELN',
                'data.category#nomad_laserphysics.schema_packages.schema_package.laserphysicsELN',
                'data.date#nomad_laserphysics.schema_packages.schema_package.laserphysicsELN',
            ],
            selected=[
                'data.name#nomad_laserphysics.schema_packages.schema_package.laserphysicsELN',
                'authors',
                'data.category#nomad_laserphysics.schema_packages.schema_package.laserphysicsELN',
                'data.date#nomad_laserphysics.schema_packages.schema_package.laserphysicsELN',
            ],
            options={
                'entry_id': Column(),
                'entry_type': Column(label='Entry type', align=AlignEnum.LEFT),
                'authors': Column(label='Authors', align=AlignEnum.LEFT),
                'data.name#nomad_laserphysics.schema_packages.schema_package.laserphysicsELN': Column(
                    label='Name', align=AlignEnum.LEFT
                ),
                'data.category#nomad_laserphysics.schema_packages.schema_package.laserphysicsELN': Column(
                    label='Category'
                ),
                'data.date#nomad_laserphysics.schema_packages.schema_package.laserphysicsELN': Column(
                    label='Last update',
                    align=AlignEnum.LEFT,
                    format=Format(mode=ModeEnum.DATE),
                ),
            },
        ),

        menu=Menu(
            title='filter-menu',
            items=[
                Menu(
                    title='Basic data',
                    items=[
                        MenuItemHistogram(
                            title='date of the last update',
                            x='upload_create_time',
                        ),
                        MenuItemTerms(
                          title='category',
                         search_quantity='data.category#nomad_laserphysics.schema_packages.schema_package.laserphysicsELN',
                        ),
                        MenuItemTerms(
                          title='author\'s first name',
                         search_quantity='data.authors.first_name#nomad_laserphysics.schema_packages.schema_package.laserphysicsELN',
                        ),
                        MenuItemTerms(
                          title='author\'s last name',
                         search_quantity='data.authors.last_name#nomad_laserphysics.schema_packages.schema_package.laserphysicsELN',
                        ),
                    ],
                ),
                Menu(
                    title='value data',
                    items=[
                        MenuItemHistogram(
                            x='data.measurement.voltage#nomad_laserphysics.schema_packages.schema_package.laserphysicsELN',
                        ),
                        MenuItemHistogram(
                            x='data.measurement.laserpower#nomad_laserphysics.schema_packages.schema_package.laserphysicsELN',
                        ),
                        MenuItemHistogram(
                            x='data.measurement.wavelength#nomad_laserphysics.schema_packages.schema_package.laserphysicsELN',
                        ),
                    ],
                ),
                Menu(
                    title='tag data',
                    items=[
                        MenuItemTerms(
                            title='tags',
                            search_quantity='data.material.tags#nomad_laserphysics.schema_packages.schema_package.laserphysicsELN'
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
                    title='visibility menu',
                ),
                MenuItemCustomQuantities(
                    title='custom quantity menu',
                ),
            ],
        ),

        #filter_menus=FilterMenus(
        #    options={
        #        'custom_quantities': FilterMenu(
        #            label='Quantity filters', size=FilterMenuSizeEnum.L
        #        ),
        #        'author': FilterMenu(label='Metadata', size=FilterMenuSizeEnum.M),
        #        'metadata': FilterMenu(label='Visibility / IDs'),
        #    }
        #),
        #dashboard=Dashboard(
        #    widgets=[
        #        WidgetTerms(
        #            type='terms',
        #            quantity='data.category#nomad_laserphysics.schema_packages.schema_package.laserphysicsELN',
        #            scale=ScaleEnum.POW1,
        #            layout={
        #                BreakpointEnum.XXL: Layout(h=6, w=6, x=0, y=0),
        #                BreakpointEnum.XL: Layout(h=6, w=6, x=0, y=0),
        #                BreakpointEnum.LG: Layout(h=6, w=6, x=0, y=0),
        #                BreakpointEnum.MD: Layout(h=6, w=6, x=0, y=0),
        #                BreakpointEnum.SM: Layout(h=6, w=6, x=0, y=0),
        #            },
        #        ),
        #        WidgetPeriodicTable(
        #            type='periodictable',
        #            title='Material',
        #            quantity='results.material.elements',
        #            scale='linear',
        #            layout={
        #               'lg': Layout(h=9, w=15, x=0, y=0),
        #                'md': Layout(h=8, w=11, x=0, y=0),
        #                'sm': Layout(h=6, w=9, x=0, y=0),
        #                'xl': Layout(h=9, w=19, x=0, y=0),
        #                'xxl': Layout(h=10, w=25, x=0, y=0),
        #            },
        #        ),
                #WidgetTerms(
                #    type='terms',
                #    quantity='data.systems.name#nomad_aitoolkit.schema.schema_package.AIToolkitNotebook',
                #    title='Systems',
                #    scale=ScaleEnum.POW1,
                #    layout={
                #        BreakpointEnum.XXL: Layout(h=6, w=6, x=12, y=0),
                #        BreakpointEnum.XL: Layout(h=6, w=6, x=12, y=0),
                #        BreakpointEnum.LG: Layout(h=6, w=6, x=12, y=0),
                #        BreakpointEnum.MD: Layout(h=6, w=6, x=12, y=0),
                #        BreakpointEnum.SM: Layout(h=6, w=6, x=12, y=0),
                #    },
                #),
        #    ]
        #),
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
