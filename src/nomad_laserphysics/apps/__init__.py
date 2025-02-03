from nomad.config.models.plugins import AppEntryPoint

from nomad_laserphysics.apps.FEM_correlation_chambers import FEMCorrelationChambers

FEM_correlation_chambers_app_entry_point = AppEntryPoint(
    label='FEM Correlation Chambers',
    description='App defined using the new plugin mechanism.',
    app=FEMCorrelationChambers
)