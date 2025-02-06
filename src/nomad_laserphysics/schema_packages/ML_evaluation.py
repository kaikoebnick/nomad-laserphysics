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

from nomad_laserphysics.schema_packages.evaluation import Evaluation
from nomad_laserphysics.schema_packages.ML_evaluation_procedure import (
    MLEvaluationProcedure,
)

m_package = SchemaPackage(name='ML Evaluation schema')

class ToolsCategory(EntryDataCategory):
    m_def = Category(
        label='A collection of Laserphysics schemas',
        categories=[EntryDataCategory]
    )


class MLEvaluation(Evaluation):
    m_def = Section(
        label='ML evaluation',
        categories=[ToolsCategory],
        a_eln=ELNAnnotation(),
        quantities=[*Evaluation.m_def.quantities]
        )

    """procedure = Quantity(
        type=MLEvaluationProcedure,
        description="Used procedure.",
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.ReferenceEditQuantity,
            showSectionLabel=True,
        ),
    )"""


m_package.__init_metainfo__()
