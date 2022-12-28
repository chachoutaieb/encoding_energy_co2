#!/usr/bin/env python3
import os
import argparse
from codecarbon import OfflineEmissionsTracker
def encoding2(envid, sec, country):
    print(sec, sec, country)
    tracker = OfflineEmissionsTracker(measure_power_secs = float(sec), country_iso_code=country)
    #tracker = EmissionsTracker()
    tracker.start()

    os.system(envid)

    tracker.stop()

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video_path", help="Path to dataset")
ap.add_argument("-s", "--mps", help="Path to dataset")
ap.add_argument("-c", "--country", help="Path to dataset")
args = vars(ap.parse_args())

encoding2(args['video_path'], args['mps'], args['country'])
