from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


from nomad.datamodel.data import (
    EntryDataCategory,
)
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
from nomad.metainfo import (
    Category,
    Quantity,
    SchemaPackage,
    Section,
)

from nomad_laserphysics.schema_packages.measurement import Measurement

m_package = SchemaPackage(
    name='FEM Correlation Chamber schema',
    label='FEM Correlation Chamber schema'
    )

class ToolsCategory(EntryDataCategory):
    m_def = Category(
        label='A collection of Laserphysics schemas',
        categories=[EntryDataCategory]
    )

class FEMCorrelationChamber(Measurement):
    m_def = Section(
        label='FEM correalation chamber',
        categories=[ToolsCategory],
        a_eln=ELNAnnotation(),
    )

    extra = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        label='extra',
        description='extra.',
    )


m_package.__init_metainfo__()
