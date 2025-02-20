from nomad.config.models.plugins import AppEntryPoint

from nomad_laserphysics.apps.evaluations import Evaluations
from nomad_laserphysics.apps.FEM_correlation_chambers import FEMCorrelationChambers
from nomad_laserphysics.apps.FIM_test_chambers import FIMTestChambers
from nomad_laserphysics.apps.measurements import Measurements
from nomad_laserphysics.apps.objects import Objects
from nomad_laserphysics.apps.tip_samples import Tip_samples

measurements_app_entry_point = AppEntryPoint(
    label='Measurements',
    description='App defined using the new plugin mechanism.',
    app=Measurements
)
FEM_correlation_chambers_app_entry_point = AppEntryPoint(
    label='FEM Correlation Chambers',
    description='App defined using the new plugin mechanism.',
    app=FEMCorrelationChambers
)
FIM_test_chambers_app_entry_point = AppEntryPoint(
    label='FIM Test Chambers',
    description='App defined using the new plugin mechanism.',
    app=FIMTestChambers
)
evaluations_app_entry_point = AppEntryPoint(
    label='Evaluations',
    description='App defined using the new plugin mechanism.',
    app=Evaluations
)
objects_app_entry_point = AppEntryPoint(
    label='Objects',
    description='App defined using the new plugin mechanism.',
    app=Objects
)
tip_sample_app_entry_point = AppEntryPoint(
    label='Tip Samples',
    description='App defined using the new plugin mechanism.',
    app=Tip_samples
)
