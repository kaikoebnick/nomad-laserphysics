from nomad.datamodel.data import (
    EntryDataCategory,
    Schema,
)
from nomad.datamodel.metainfo.annotations import ELNAnnotation
from nomad.metainfo import (
    Category,
    SchemaPackage,
    Section,
)

m_package = SchemaPackage(name='ML Evaluation Procedure schema')

class ToolsCategory(EntryDataCategory):
    m_def = Category(
        label='A collection of Laserphysics schemas',
        categories=[EntryDataCategory]
    )


class MLEvaluationProcedure(Schema):
    m_def = Section(
        label='ML evaluation procedure',
        categories=[ToolsCategory],
        a_eln=ELNAnnotation(),
        )


m_package.__init_metainfo__()
