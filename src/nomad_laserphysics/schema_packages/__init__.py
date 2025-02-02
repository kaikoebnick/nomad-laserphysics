from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class EvaluationSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_laserphysics.schema_packages.evaluation import m_package

        return m_package

class MeasurementSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_laserphysics.schema_packages.measurement import m_package

        return m_package

class FIMTestChamberSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_laserphysics.schema_packages.FIM_test_chamber import (
            m_package,
        )

        return m_package

class FEMCorrelationChamberSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_laserphysics.schema_packages.FEM_correlation_chamber import (
            m_package,
        )

        return m_package

class TipSampleSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_laserphysics.schema_packages.tip_sample import m_package

        return m_package


evaluation_schema_package_entry_point = EvaluationSchemaPackageEntryPoint(
    name='evaluation schema',
    description='New schema package entry point configuration.',
    plugin_package='schema_packages',
)

measurement_schema_package_entry_point = \
        MeasurementSchemaPackageEntryPoint(
    name='Measurement schema',
    description='New schema package entry point configuration.',
    plugin_package='schema_packages',
)

FIM_test_chamber_schema_package_entry_point = \
        FIMTestChamberSchemaPackageEntryPoint(
    name='FIM test chamber schema',
    description='New schema package entry point configuration.',
    plugin_package='schema_packages',
)

FEM_correlation_chamber_schema_package_entry_point = \
        FEMCorrelationChamberSchemaPackageEntryPoint(
    name='FEM correlation chamber schema',
    description='New schema package entry point configuration.',
    plugin_package='schema_packages',
)

tip_sample_schema_package_entry_point = TipSampleSchemaPackageEntryPoint(
    name='tip sample schema',
    description='New schema package entry point configuration.',
    plugin_package='schema_packages',
)
