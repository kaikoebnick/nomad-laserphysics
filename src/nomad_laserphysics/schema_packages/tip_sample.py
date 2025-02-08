from nomad.datamodel.data import (
    EntryDataCategory,
)
from nomad.datamodel.metainfo.annotations import ELNAnnotation
from nomad.metainfo import (
    Category,
    # Quantity,
    SchemaPackage,
    Section,
)

from nomad_laserphysics.schema_packages.object import Object

m_package = SchemaPackage(name='tip sample schema')


class ToolsCategory(EntryDataCategory):
    m_def = Category(
        label='A collection of Laserphysics schemas',
        categories=[EntryDataCategory]
    )


class TipSample(Object):
    m_def = Section(
        label='tip Sample',
        categories=[ToolsCategory],
        a_eln=ELNAnnotation(),
        quantities=[*Object.m_def.quantities]
    )

    """object_type = Quantity(
        description='Type of the tip.',
    )

    number_of_that_type = Quantity(
        label='number of that tip',
        description='Number of that tip.',
    )

    date = Quantity(
        description='Date of the tip-creation.',
    )"""


m_package.__init_metainfo__()
