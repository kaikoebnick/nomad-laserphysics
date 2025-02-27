from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

import datetime

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

    name = Quantity(
        type=str,
        description='Laserphysics name, automatically set.',
    )

    title = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        label='title',
        description='Title of teh procedure.',
    )

    date = Quantity(
        type=Datetime,
        a_eln=ELNAnnotation(component=ELNComponentEnum.DateEditQuantity),
        label='date and time',
        description='Date and time of the procedure-creation.',
    )

    description = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
        description='Short description. You can add pictures!',
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
