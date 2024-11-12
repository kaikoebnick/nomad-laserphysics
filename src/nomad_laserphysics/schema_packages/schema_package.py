from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

import datetime
import xml

from ase.data import chemical_symbols
from nomad.datamodel.data import (
    ArchiveSection,
    EntryDataCategory,
    Schema,
)
from nomad.datamodel.data import Author as NomadAuthor
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum

#from nomad.datamodel.metainfo.basesections import System
from nomad.metainfo import (
    Category,
    Datetime,
    MEnum,
    Quantity,
    SchemaPackage,
    Section,
    SubSection,
)

# from nomad.datamodel.metainfo.datamdel import EntryArchiveReference
# from nomad.datamodel.results import System
from nomad.metainfo.elasticsearch_extension import (
    Elasticsearch,
    material_type,
)

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


class Measurement(ArchiveSection):
    m_def = Section(a_eln=ELNAnnotation(overview=True))

    #material_1 = SubSection(section=ElementalComposition, repeats=True)

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

    def normalize(self, archive, logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)

        if self.element not in archive.results.material.elements:
            for el in self.material:
                archive.results.material.elements += [el]

        #if self.material:
        #    for el in self.material:
        #        archive.ElementalComposition.element = el


class laserphysicsELN(Schema):
    m_def = Section(
        label='laserphysics ELN schema',
        categories=[ToolsCategory],
        a_eln=ELNAnnotation(),
    )

    name = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        label='Name/Title',
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
        label='Last update',
        description='The date of the last update.',
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


    """number_of_people_killed_during_measurement = Quantity(
        type=int,
        description='''Let us hope it is zero.''',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.SliderEditQuantity,
            minValue=0,
            maxValue=50,
        )
    )"""

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




m_package.__init_metainfo__()
