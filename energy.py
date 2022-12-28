#!/usr/bin/env python3
import os
import argparse
from codecarbon import OfflineEmissionsTracker
def encoding2(envid):
    tracker = OfflineEmissionsTracker(measure_power_secs = 0.3, country_iso_code="FRA")
    #tracker = EmissionsTracker()
    tracker.start()

    os.system(envid)

    tracker.stop()

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video_path", help="Path to dataset")
args = vars(ap.parse_args())
encoding2(args['video_path'])
