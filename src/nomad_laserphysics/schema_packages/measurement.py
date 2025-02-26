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
from nomad.datamodel.results import ELN, Results
from nomad.metainfo import (
    Category,
    Datetime,
    Quantity,
    SchemaPackage,
    Section,
)
from nomad.metainfo.elasticsearch_extension import (
    Elasticsearch,
)

from nomad_laserphysics.schema_packages.tip_sample import TipSample

m_package = SchemaPackage(name='Measurement schema')


class ToolsCategory(EntryDataCategory):
    m_def = Category(
        label='A collection of Laserphysics schemas',
        categories=[EntryDataCategory]
    )


def remove_tags(text):
    return ''.join(xml.etree.ElementTree.fromstring(text).itertext())


class MyELN(ELN): #for making values searchable
    m_def = Section(extends_base_section=True)
    voltage = Quantity(
        type=float,
        unit='volt',
        description="Voltage in V.",
        a_elasticsearch=[
            Elasticsearch(material_type, many_all=True),
            Elasticsearch(suggestion="simple")
        ]
    )
    laserpower = Quantity(
        type=float,
        unit='milliwatt',
        description="Laserpower in mW.",
    )
    wavelength = Quantity(
        type=float,
        unit='nanometer',
        description="Wavelength in nm.",
    )
    u_p = Quantity(
        type=float,
        unit='electron_volt',
        description="U_p in V.",
    )


class Measurement(Schema):
    m_def = Section(
        label='measurement',
        categories=[ToolsCategory],
        a_eln=ELNAnnotation(),
    )

    name = Quantity(
        type=str,
        description='Laserphysics name, automatically set.',
    )

    measurement_type = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        label='measurement type',
        description='Type of the measurement.',
    )

    measurement_number_of_that_type = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        label='measurement number of that type',
        description='Measurement number of that type.',
    )

    date = Quantity(
        type=Datetime,
        a_eln=ELNAnnotation(component=ELNComponentEnum.DateEditQuantity),
        label='date',
        description='Date of the measurement.',
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

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)

        if not archive.results:
            archive.results = Results(eln = ELN())
        if not archive.results.eln:
            archive.results.eln = ELN()
        archive.results.eln.tags = list( #make tags searchable
            quant.name
            for quant in self.m_def.quantities
            if str(quant.type) == "m_bool(bool)" and getattr(self, str(quant.name))
        )
        logger.info(f"Set tags to {archive.results.eln.tags}")

        #make values searchable
        if self.voltage:
            archive.results.eln.voltage = self.voltage
        if self.laserpower:
            archive.results.eln.laserpower = self.laserpower
        if self.wavelength:
            archive.results.eln.wavelength = self.wavelength
        if self.u_p:
            archive.results.eln.u_p = self.u_p

        if not self.date: #make date searchable
            self.date = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        if self.date:
            archive.metadata.upload_create_time = self.date

        if self.date and (
            self.measurement_type or
            self.measurement_number_of_that_type): #set name
            d = self.date.replace(tzinfo=pytz.utc)
            d = d.astimezone(pytz.timezone('Europe/Berlin')).strftime("%d-%m-%y")
            a = f"{self.measurement_type}_{self.measurement_number_of_that_type}_{d}"
            archive.metadata.entry_name = a
            self.name = archive.metadata.entry_name
            logger.info(f"Set entry name to {archive.metadata.entry_name}")


m_package.__init_metainfo__()
