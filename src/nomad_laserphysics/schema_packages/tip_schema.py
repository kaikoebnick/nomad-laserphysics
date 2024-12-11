from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

import xml

from ase.data import chemical_symbols
from nomad.datamodel.data import (
    #Schema,
    ArchiveSection,
    EntryDataCategory,
)

#from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
#from nomad.datamodel.metainfo.basesections import ElementalComposition
from nomad.datamodel.results import Material, Results
from nomad.metainfo import (
    Category,
    MEnum,
    #Msection,
    Quantity,
    SchemaPackage,
    Section,
)

# from nomad.datamodel.metainfo.datamdel import EntryArchiveReference
# from nomad.datamodel.results import System
#from nomad.metainfo.elasticsearch_extension import (
#    Elasticsearch,
    #material_type,
#)

m_package = SchemaPackage(name='laserphysics tip schema')


class ToolsCategory(EntryDataCategory):
    m_def = Category(label='Basic ELN', categories=[EntryDataCategory])


def remove_tags(text):
    return ''.join(xml.etree.ElementTree.fromstring(text).itertext())


class laserphysicsTip(ArchiveSection):
    m_def = Section(validate=False,
        #label='laserphysics Tip',
        #categories=[ToolsCategory],
        #a_eln=ELNAnnotation(),
    )

    tip_type = Quantity(
        type=str,
        #a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        label='type',
        description='Type of the tip.',
    )

    material = Quantity(
        type=MEnum(chemical_symbols),
        shape= ['0..*'], #['n_atoms'],
        default=[],
        #a_eln=ELNAnnotation(
        #    component=ELNComponentEnum.EnumEditQuantity
        #),
        description="""Chemical elements of the material.""",
        #a_elasticsearch=[
        #    Elasticsearch(material_type, many_all=True),
        #    Elasticsearch(suggestion='simple'),
        #],
    )

    description = Quantity(
        type=str,
        #a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
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




m_package.__init_metainfo__()
