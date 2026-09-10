from calibration_choreography.screen_marker_plugin import ScreenMarkerChoreographyPlugin
from calibration_choreography.base_plugin import ChoreographyMode
from random import shuffle
import numpy as np

# Just calibrate and validate on the inner half
# randomly sample the order

class CustomScreenMarkerChoreography(ScreenMarkerChoreographyPlugin):
    label = "Custom Screen Marker"

    @classmethod
    def selection_label(cls) -> str:
        return "Custom Screen Marker"

    @staticmethod
    def get_list_of_markers_to_show(mode: ChoreographyMode) -> list:
        points = np.array([
            [0.5, 0.5],
            [0.25, 0.5],
            [0.5, 0.75],
            [0.75, 0.5],
            [0.5, 0.25],
            [0.25, 0.25],
            [0.25, 0.75],
            [0.75, 0.25],
            [0.75, 0.75],
        ])

        # shuffle the order
        np.random.shuffle(points)

        # # apply a random rotation to the points
        # angle = np.random.uniform(0, 2 * np.pi)
        # rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        # points = points @ rotation_matrix.T

        return [(point[0], point[1]) for point in points]
