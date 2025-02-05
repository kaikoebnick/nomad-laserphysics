from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

import datetime
import xml

import pytz
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

from nomad_laserphysics.tools.id_generator import generate_id

m_package = SchemaPackage(name='tip sample schema')


class ToolsCategory(EntryDataCategory):
    m_def = Category(
        label='A collection of Laserphysics schemas',
        categories=[EntryDataCategory]
    )


def remove_tags(text):
    return ''.join(xml.etree.ElementTree.fromstring(text).itertext())



class TipSample(Schema):
    m_def = Section(
        label='tip Sample',
        categories=[ToolsCategory],
        a_eln=ELNAnnotation(),
    )

    name = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity,),
     description='Laserphysics name.',
    )

    laserphysics_id = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
      description='Laserphysics id.',
    )

    title = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        label='title',
        description='title/type of the tip.',
    )

    date = Quantity(
        type=Datetime,
        a_eln=ELNAnnotation(component=ELNComponentEnum.DateTimeEditQuantity),
        label='date and time',
        description='Date and time of the tip-creation.',
    )

    material = Quantity(
        type=MEnum(chemical_symbols),
        shape= ['0..*'],
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
        description='Short description. You can add pictures!',
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)

        if not self.name:
            self.name = 'Will be set automatically'

        if not self.laserphysics_id:
            self.laserphysics_id = 'Will be set automatically'

        if self.material: #make elements in material searchable
            if not archive.results:
                archive.results = Results(
                    a_display={'visible': False, 'editable': False}
                    )
            if not archive.results.material:
                archive.results.material = Material(
                    a_display={'visible': False, 'editable': False}
                    )
            archive.results.material.elements = list(
                el
                for el in self.material
            )

        if self.date is None: #make date and time searchable
            self.date = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        if self.date:
            archive.metadata.upload_create_time = self.date

        if self.date and self.title: #set name as title_date
            d = self.date.replace(tzinfo=pytz.utc)
            d = d.astimezone(pytz.timezone('Europe/Berlin')).strftime("%d-%m-%y_%H:%M")
            archive.metadata.entry_name = f"{self.title}_{d}"
            self.name = f"{self.title}_{d}"
            logger.info(f"Set entry name to {archive.metadata.entry_name}")

        if self.title:
            self.laserphysics_id = f't{generate_id(self.name)}'




m_package.__init_metainfo__()
