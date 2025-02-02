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

m_package = SchemaPackage(name='FEM Correlation Chamber schema')

class ToolsCategory(EntryDataCategory):
    m_def = Category(label='Basic ELN', categories=[EntryDataCategory])

class FIM_test_chamber(Measurement):
    m_def = Section(
        label='FEM Correalation chamber',
        categories=[ToolsCategory],
        a_eln=ELNAnnotation(),
    )


m_package.__init_metainfo__()
