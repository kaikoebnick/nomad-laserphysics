from nomad.datamodel.data import (
    EntryDataCategory,
)
from nomad.datamodel.metainfo.annotations import ELNAnnotation
from nomad.metainfo import (
    Category,
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
        quantities=[*Measurement.m_def.quantities]
    )


m_package.__init_metainfo__()
