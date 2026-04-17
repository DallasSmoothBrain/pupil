"""
(*)~----------------------------------------------------------------------------------
 Pupil LSL Relay
 Copyright (C) 2012 Pupil Labs

 Distributed under the terms of the GNU Lesser General Public License (LGPL v3.0).
 License details are in the file license.txt, distributed as part of this software.
----------------------------------------------------------------------------------~(*)
"""
from typing import Sequence
from .channel import (
    gaze_on_surface_confidence_channel,
    gaze_on_surface_norm_pos_channels,
    gaze_on_surface_on_surf_channel,
    gaze_on_surface_timestamp_channel,
    gaze_on_surface_name_channel,
    gaze_on_surface_uid_channel,
)
from .outlet import Outlet


class GazeOnSurface(Outlet):
    @property
    def name(self) -> str:
        return "pupil_capture_gaze_on_surface"

    @property
    def event_key(self) -> str:
        return "gaze_on_surface"

    def setup_channels(self) -> Sequence[object]:
        return (
            gaze_on_surface_confidence_channel(),
            *gaze_on_surface_norm_pos_channels(),
            gaze_on_surface_on_surf_channel(),
            gaze_on_surface_timestamp_channel(),
            gaze_on_surface_name_channel(),
            gaze_on_surface_uid_channel(),
        )
