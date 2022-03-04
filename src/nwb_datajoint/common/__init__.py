# Reorganize this into hierarchy
# Note: users will have their own tables... permission system
import os

import spikeinterface as si

from .common_backup import CuratedSpikeSortingBackUp, SpikeSortingBackUp
from .common_behav import (HeadDir, LinPos, PositionSource, RawPosition, Speed,
                           StateScriptFile, VideoFile)
from .common_curation import (AutomaticCurationParameters,
                              AutomaticCurationSelection,
                              AutomaticCurationSorting, CuratedSpikeSorting,
                              CuratedSpikeSortingSelection, SelectedUnits,
                              SelectedUnitsParameters)
from .common_device import CameraDevice, DataAcquisitionDevice, Probe
from .common_dio import DIOEvents
from .common_ephys import (LFP, Electrode, ElectrodeGroup, LFPBand,
                           LFPBandSelection, LFPSelection, Raw, SampleCount)
from .common_filter import FirFilter
from .common_interval import (IntervalList, SortInterval, interval_list_censor,
                              interval_list_contains,
                              interval_list_contains_ind,
                              interval_list_excludes,
                              interval_list_excludes_ind,
                              interval_list_intersect, interval_list_union,
                              intervals_by_length)
from .common_lab import Institution, Lab, LabMember, LabTeam
from .common_metrics import MetricParameters, MetricSelection, QualityMetrics
from .common_nwbfile import (AnalysisNwbfile, AnalysisNwbfileKachery, Nwbfile,
                             NwbfileKachery)
from .common_region import BrainRegion
from .common_sensors import SensorData
from .common_session import ExperimenterList, Session
from .common_sortingview import SortingviewWorkspace
from .common_spikesorting import (SortGroup, Sortings, SpikeSorterParameters,
                                  SpikeSorting,
                                  SpikeSortingPreprocessingParameters,
                                  SpikeSortingRecording,
                                  SpikeSortingRecordingSelection,
                                  SpikeSortingSelection)
from .common_artifact import (ArtifactDetection, ArtifactDetectionParameters,
                              ArtifactDetectionSelection,
                              ArtifactRemovedIntervalList)
from .common_subject import Subject
from .common_task import Task, TaskEpoch
from .common_waveforms import WaveformParameters, Waveforms, WaveformSelection
from .nwb_helper_fn import (close_nwb_files, estimate_sampling_rate,
                            get_data_interface, get_electrode_indices,
                            get_nwb_file, get_raw_eseries, get_valid_intervals)
from .populate_all_common import populate_all_common

si.set_global_tmp_folder(os.environ['KACHERY_TEMP_DIR'])
