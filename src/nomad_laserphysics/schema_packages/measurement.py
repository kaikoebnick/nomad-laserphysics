from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

import datetime
import xml

import pytz
from nomad.datamodel.data import (
    ArchiveSection,
    EntryDataCategory,
    Schema,
)
from nomad.datamodel.data import Author as NomadAuthor
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
from nomad.metainfo import (
    Category,
    Datetime,
    Quantity,
    SchemaPackage,
    Section,
    SubSection,
)

from nomad_laserphysics.schema_packages.tip_sample import TipSample
from nomad_laserphysics.tools.id_generator import generate_id

m_package = SchemaPackage(name='Measurement schema')


class ToolsCategory(EntryDataCategory):
    m_def = Category(
        label='A collection of Laserphysics schemas',
        categories=[EntryDataCategory]
    )


def remove_tags(text):
    return ''.join(xml.etree.ElementTree.fromstring(text).itertext())


class Author(ArchiveSection):
    m_def = Section(
        a_eln=ELNAnnotation(overview=True),
        )

    first_name = Quantity(
        type=str,
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.StringEditQuantity,
        ),
        label='First Name',
        description='First name of the author',
    )

    last_name = Quantity(
        type=str,
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.StringEditQuantity,
        ),
        label='Last Name',
        description='Last name of the author.',
    )


class Tags(ArchiveSection): #used to make tags searchable
    m_def = Section(a_display=
    {'visible': False, 'editable': False}
    )

    tag = Quantity(
        type=str,
        a_display={'visible': False, 'editable': False},
    )


class Measurement(Schema):
    m_def = Section(
        label='measurement',
        categories=[ToolsCategory],
        a_eln=ELNAnnotation(),
        a_display={'order': list('name', 'laserphysics_id')}
    )

    name = Quantity(
        type=str,
        a_display={'visible': True, 'editable': False},
        description='Laserphysics name.',
    )

    laserphysics_id = Quantity(
        type=str,
        a_display={'visible': True, 'editable': False},
        description='Laserphysics id.',
    )

    title = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        label='title',
        description='Short title of the measurement.',
    )

    date = Quantity(
        type=Datetime,
        a_eln=ELNAnnotation(component=ELNComponentEnum.DateTimeEditQuantity),
        label='date and time',
        description='Date and time of the measurement.',
    )

    idea_behind_measurement = Quantity(
        type=str,
        label='idea behind measurement',
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
        description='Short description on why the measurement was taken.',
    )

    tip = Quantity(
        type=TipSample,
        description="Name of the tip.",
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.ReferenceEditQuantity,
            showSectionLabel=True,
        ),
    )

    voltage = Quantity(
        type=float,
        unit='volt',
        description="Voltage in V.",
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
        ),
    )

    laserpower = Quantity(
        type=float,
        unit='milliwatt',
        description="Laserpower in mW.",
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='milliwatt'
        ),
    )

    wavelength = Quantity(
        type=float,
        unit='nanometer',
        description="Wavelength in nm.",
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='nanometer'
        ),
    )

    u_p = Quantity(
        type=float,
        label='U_p',
        unit='electron_volt',
        description="U_p in V.",
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
        ),
    )

    multiphoton_peaks = Quantity(
        type=bool,
        label='multiphoton peaks',
        description="Check if there are multiphoton peaks.",
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )

    plateau = Quantity(
        type=bool,
        label='plateu',
        description="Check if there is a plateau.",
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )

    voltage_sweep = Quantity(
        type=bool,
        label='voltage_sweep',
        description="Check if there is a voltage sweep.",
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )

    power_sweep = Quantity(
        type=bool,
        label='power_sweep',
        description="Check if there is a power sweep.",
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )

    cep_sweep = Quantity(
        type=bool,
        label='cep_sweep',
        description="Check if there is a CEP sweep.",
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )

    electrons = Quantity(
        type=bool,
        label='electrons',
        description="Check if there are electrons.",
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )

    ions = Quantity(
        type=bool,
        label='ions',
        description="Check if there are ions.",
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )

    photons = Quantity(
        type=bool,
        label='photons',
        description="Check if there are photons.",
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )

    ToF_gauge_measurement = Quantity(
        type=bool,
        label='ToF_gauge_measurement',
        description="Check if this is a ToF gauge measurement.",
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )

    adc = Quantity(
        type=bool,
        label='ADC',
        description="Check if the measurement uses an ADC",
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )

    cfd = Quantity(
        type=bool,
        label='CFD',
        description="Check if the measurment uses CFD.",
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )

    description = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
        description='Extra details about the measurement.',
    )

    description = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
        description='Short description. You can add pictures!',
    )

    category = Quantity(
        type=str,
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.EnumEditQuantity,
            props=dict(
                suggestions=[
                    'measurement',
                    'calibration',
                    'other',
                ]
            ),
        ),
    )

    co_authors = SubSection(section=Author, repeats=True)

    tags = SubSection( #make tags searchable
        section=Tags,
        repeats=True,
        a_display={'visible': False, 'editable': False}
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)

        #make tags searchable
        self.tags = list(
            Tags(tag=quant.name)
            for quant in self.m_def.quantities
            if str(quant.type) == "m_bool(bool)" and getattr(self, str(quant.name))
        )

        #make co_authors searchable
        if self.co_authors:
            archive.metadata.entry_coauthors = [
                NomadAuthor(**author.m_to_dict()) for author in self.co_authors
            ]

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

        if self.name:
            self.laserphysics_id = generate_id(self.name)


m_package.__init_metainfo__()
