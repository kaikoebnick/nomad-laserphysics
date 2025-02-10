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
from nomad.datamodel.results import ELN, Material, Results
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

from nomad_laserphysics.tools.counter import NomadCounter

m_package = SchemaPackage(name='object schema')


class ToolsCategory(EntryDataCategory):
    m_def = Category(
        label='A collection of Laserphysics schemas',
        categories=[EntryDataCategory]
    )


def remove_tags(text):
    return ''.join(xml.etree.ElementTree.fromstring(text).itertext())


class Object(Schema):
    m_def = Section(
        label='object',
        categories=[ToolsCategory],
        a_eln=ELNAnnotation(),
    )

    name = Quantity(
        type=str,
        description='Laserphysics name, automatically set.',
    )

    laserphysics_id = Quantity(
        type=str,
        description='Laserphysics id.',
    )

    object_type = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        label='type',
        description='Type of the object.',
    )

    number_of_that_type = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        label='number of that object',
        description='Number of that object.',
    )

    date = Quantity(
        type=Datetime,
        a_eln=ELNAnnotation(component=ELNComponentEnum.DateEditQuantity),
        label='date',
        description='Date of the object-creation.',
    )

    material = Quantity(
        type=MEnum(chemical_symbols),
        shape= ['0..*'],
        default=[],
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.EnumEditQuantity
        ),
        description="Chemical elements of the material.",
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

        counter = NomadCounter() #set laserphysics_id
        if not self.laserphysics_id:
            entry_id = archive.metadata.entry_id
            self.laserphysics_id = counter.get_counter_and_update(entry_id)

        if not archive.results:
            archive.results = Results(
                a_display={'visible': False, 'editable': False}
                )
        if not archive.results.material: #make elements in material searchable
            archive.results.material = Material(
                a_display={'visible': False, 'editable': False}
                )
        if self.material:
            archive.results.material.elements = list(
                el
                for el in self.material
            )
        logger.info(f"Set elements to {self.material}")
        if not archive.results.eln: # make laserphysics_id searchable
            archive.results.eln = ELN(
                a_display={'visible': False, 'editable': False}
                )
        archive.results.eln.lab_ids = [self.laserphysics_id]
        logger.info(f"Set lab_ids to {self.laserphysics_id}")

        if self.date is None: #make date searchable
            self.date = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        if self.date:
            archive.metadata.upload_create_time = self.date
            logger.info(f"Set upload_create_time to {self.date}")

        if self.date and (self.object_type or self.number_of_that_type): #set name
            d = self.date.replace(tzinfo=pytz.utc)
            d = d.astimezone(pytz.timezone('Europe/Berlin')).strftime("%d-%m-%y")
            a = f"{self.object_type}_{self.number_of_that_type}_{d}"
            archive.metadata.entry_name = a
            self.name = archive.metadata.entry_name
            logger.info(f"Set entry name to {archive.metadata.entry_name}")




m_package.__init_metainfo__()
