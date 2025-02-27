from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

import datetime
import xml

import pytz
from nomad.datamodel.data import (
    EntryDataCategory,
    Schema,
)
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
from nomad.metainfo import (
    Category,
    Datetime,
    Quantity,
    SchemaPackage,
    Section,
)

from nomad_laserphysics.schema_packages.measurement import Measurement

m_package = SchemaPackage(name='Evaluation schema')

class ToolsCategory(EntryDataCategory):
    m_def = Category(
        label='A collection of Laserphysics schemas',
        categories=[EntryDataCategory]
    )


def remove_tags(text):
    return ''.join(xml.etree.ElementTree.fromstring(text).itertext())


class Evaluation(Schema):
    m_def = Section(
        label='evaluation',
        categories=[ToolsCategory],
        a_eln=ELNAnnotation(overview=True),
        )

    name = Quantity(
        type=str,
        description='Laserphysics name, automatically set.',
    )

    title = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        description='Title of the evaluation.',
    )

    date = Quantity(
        type=Datetime,
        a_eln=ELNAnnotation(component=ELNComponentEnum.DateEditQuantity),
        label='measurement date and time',
        description='Date and time of the evaluation.',
    )

    measurement = Quantity(
        type=Measurement,
        description="Evaluated measurement.",
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.ReferenceEditQuantity,
            showSectionLabel=True,
        ),
    )

    kind = Quantity(
        type=str,
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.EnumEditQuantity,
            props=dict(
                suggestions=[
                    'local file url',
                    'article url',
                    'dataset url',
                    'video url',
                    'picture url',
                    'documentation',
                    'other',
                ]
            ),
        ),
    )

    description = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
        description='Extra details about the reference.',
    )

    uri = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.URLEditQuantity, label='URI'),
        description='External URI for the reference.',
    )

    version = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        description='Optional field for adding version information.',
    )


    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)

        if self.date is None: #make date and time searchable
            self.date = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        if self.date:
            archive.metadata.upload_create_time = self.date

        if self.date and self.title: #set name
            d = self.date.replace(tzinfo=pytz.utc)
            d = d.astimezone(pytz.timezone('Europe/Berlin')).strftime("%d-%m-%y")
            archive.metadata.entry_name = f"{self.title}_{d}"
            self.name = f"{self.title}_{d}"
            logger.info(f"Set entry name to {archive.metadata.entry_name}")


m_package.__init_metainfo__()
