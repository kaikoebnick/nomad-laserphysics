from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

import datetime
import xml

from nomad.datamodel.data import (
    ArchiveSection,
    EntryDataCategory,
    Schema,
)
from nomad.datamodel.data import Author as NomadAuthor
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum

#from nomad.datamodel.metainfo.basesections import ElementalComposition
from nomad.metainfo import (
    Category,
    Datetime,
    Quantity,
    SchemaPackage,
    Section,
    SubSection,
)

from nomad_laserphysics.schema_packages.tip_schema import laserphysicsTip

# from nomad.datamodel.metainfo.datamdel import EntryArchiveReference
# from nomad.datamodel.results import System

m_package = SchemaPackage(name='laserphysics ELN schema')


class ToolsCategory(EntryDataCategory):
    m_def = Category(label='Basic ELN', categories=[EntryDataCategory])


def remove_tags(text):
    return ''.join(xml.etree.ElementTree.fromstring(text).itertext())


class Author(ArchiveSection):
    m_def = Section(a_eln=ELNAnnotation(overview=True))

    first_name = Quantity(
        type=str,
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.StringEditQuantity, label='First Name'
        ),
        description='First name of the author',
    )

    last_name = Quantity(
        type=str,
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.StringEditQuantity, label='Last Name'
        ),
        description='Last name of the author.',
    )


class Evaluation(ArchiveSection):
    m_def = Section(a_eln=ELNAnnotation(overview=True))

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

    name = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        description='Human readable name for the reference.',
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

class Tags(ArchiveSection):
    m_def = Section(a_display=
    {'visible': False, 'editable': False}#, a_eln=ELNAnnotation()
    )

    tag = Quantity(
        type=str,
        a_display={'visible': False, 'editable': False},
    )

class Measurement(ArchiveSection):
    m_def = Section(a_eln=ELNAnnotation(overview=True))

    tip = Quantity(
        type=laserphysicsTip,
        description="""Type of the tip.""",
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.ReferenceEditQuantity,
            showSectionLabel=True,
        ),
    )

    voltage = Quantity(
        type=float,
        unit='volt',
        description="""Voltage in V.""",
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
        ),
    )

    laserpower = Quantity(
        type=float,
        unit='milliwatt',
        description="""Laserpower in mW.""",
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='milliwatt'
        ),
    )

    wavelength = Quantity(
        type=float,
        unit='nanometer',
        description="""Wavelength in nm.""",
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='nanometer'
        ),
    )

    u_p = Quantity(
        type=float,
        label='U_p',
        unit='electron_volt',
        description="""U_p in V.""",
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
        ),
    )

    multiphoton_peaks = Quantity(
        type=bool,
        description="""Check if there are multiphoton peaks.""",
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )

    plateau = Quantity(
        type=bool,
        description="""Check if there is a plateau.""",
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )

    voltage_sweep = Quantity(
        type=bool,
        description="""Check if there is a voltage sweep.""",
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )

    power_sweep = Quantity(
        type=bool,
        description="""Check if there is a power sweep.""",
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )

    cep_sweep = Quantity(
        type=bool,
        description="""Check if there is a CEP sweep.""",
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )

    electrons = Quantity(
        type=bool,
        description="""Check if there are electrons.""",
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )

    ions = Quantity(
        type=bool,
        description="""Check if there are ions.""",
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )

    photons = Quantity(
        type=bool,
        description="""Check if there are photons.""",
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )

    ToF_gauge_measurement = Quantity(
        type=bool,
        description="""Check if this is a ToF gauge measurement.""",
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )

    adc = Quantity(
        label='ADC',
        type=bool,
        description="""Check if the measurement uses an ADC""",
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )

    cfd = Quantity(
        labe='CFD',
        type=bool,
        description="""Check if the measurment uses CFD.""",
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )

    description = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
        description='Extra details about the measurement.',
    )

    evaluations = SubSection(section=Evaluation, repeats=True)

    tags = SubSection(section=Tags, repeats=True,
    a_display={'visible': False, 'editable': False}
    )

    def normalize(self, archive, logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)

        boolean_to_tag_map = {
            'multiphoton_peaks': self.multiphoton_peaks,
            'plateau': self.plateau,
            'voltage_sweep': self.voltage_sweep,
            'power_sweep': self.power_sweep,
            'cep_sweep': self.cep_sweep,
            'electrons': self.electrons,
            'ions': self.ions,
            'photons': self.photons,
            'ToF_gauge_measurement': self.ToF_gauge_measurement,
            'adc': self.adc,
            'cfd': self.cfd,
        }

        for boolean_name, boolean_value in boolean_to_tag_map.items():
            # Check wether tag exists
            existing_tags = [tag.tag for tag in self.tags]

            if boolean_value and boolean_name not in existing_tags:
                # Bool True but Tag does not yet exist -> add
                new_tag = Tags(tag=boolean_name)
                self.tags.append(new_tag)
            elif not boolean_value and boolean_name in existing_tags:
                # Boll False, but Tag does exist -> delete
                self.tags = [tag for tag in self.tags if tag.tag != boolean_name]


class laserphysicsELN(Schema):
    m_def = Section(
        label='laserphysics ELN',
        categories=[ToolsCategory],
        a_eln=ELNAnnotation(),
    )

    name = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        label='name/title',
        description='Short name of the ELN.',
    )

    # entry_reference = Quantity(
    #    type=Reference,
    #    a_eln=ELNAnnotation(component=ELNComponentEnum.ReferenceEditQuantity),
    #    label='Reference to other entry',
    #    description='Reference to other entry.',
    # )

    date = Quantity(
        type=Datetime,
        a_eln=ELNAnnotation(component=ELNComponentEnum.DateEditQuantity),
        label='measurement date',
        description='The date of the measurement.',
    )

    description = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
        description='Short description of the ELN. You can add pictures!',
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

    authors = SubSection(section=Author, repeats=True)

    measurement = SubSection(section=Measurement, repeats=True)


    # archiveReference = SubSection(section=EntryArchiveReference, repeats=True)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)

        if self.name:
            archive.metadata.entry_name = self.name

        """if self.description:
            if self.description.startswith('<'):
                comment = remove_tags(self.description)
            else:
                comment = self.description

            archive.metadata.comment = comment"""

        if self.authors:
            archive.metadata.entry_coauthors = [
                NomadAuthor(**author.m_to_dict()) for author in self.authors
            ]
        if self.date is None:
            self.date = datetime.datetime.now()
        if self.date:
            archive.metadata.upload_create_time = self.date
        if self.tip:
            self.tip.m_def.label=self.tip.tip_label




m_package.__init_metainfo__()
