from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

import datetime
import xml

from ase.data import chemical_symbols
from nomad.datamodel.data import (
    EntryDataCategory,
    Schema,
)
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum

from nomad.datamodel.results import Material, Results
from nomad.metainfo import (
    Category,
    Datetime,
    MEnum,
    Quantity,
    SchemaPackage,
    Section,
)
from nomad.metainfo.elasticsearch_extension import (
    Elasticsearch,
    material_type,
)

m_package = SchemaPackage(name='laserphysics tip Sample schema')


class ToolsCategory(EntryDataCategory):
    m_def = Category(label='Basic ELN', categories=[EntryDataCategory])


def remove_tags(text):
    return ''.join(xml.etree.ElementTree.fromstring(text).itertext())



class tipSample(Schema):
    m_def = Section(
        label='tip Sample',
        categories=[ToolsCategory],
        a_eln=ELNAnnotation(),
    )

    tip_type = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        label='type',
        description='Type of the tip.',
    )

    date = Quantity(
        type=Datetime,
        a_eln=ELNAnnotation(component=ELNComponentEnum.DateTimeEditQuantity),
        label='date and time',
        description='Date and time of the tip.',
    )

    material = Quantity(
        type=MEnum(chemical_symbols),
        shape= ['0..*'], #['n_atoms'],
        default=[],
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.EnumEditQuantity
        ),
        description="""Chemical elements of the material.""",
        a_elasticsearch=[
            Elasticsearch(material_type, many_all=True),
            Elasticsearch(suggestion='simple'),
        ],
    )

    description = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
        description='Short description of the ELN. You can add pictures!',
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)

        if self.material:
            if not archive.results:
                archive.results = Results(
                    a_display={'visible': False, 'editable': False}
                    )
            if not archive.results.material:
                archive.results.material = Material(
                    a_display={'visible': False, 'editable': False}
                    )

        for el in self.material:
            if el not in archive.results.material.elements:
                archive.results.material.elements += [el]

        if self.date is None:
            self.date = datetime.datetime.now()
        if self.date:
            archive.metadata.upload_create_time = self.date

        if self.date and self.tip_type:
            archive.metadata.name = f"{self.date}_{self.tip_type}"
            logger.info(f"Set entry name to {archive.metadata.name}")




m_package.__init_metainfo__()
