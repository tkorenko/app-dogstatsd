#!/usr/bin/env python3

from datadog import initialize, statsd
import hashlib
import math
import os
import time

options = {
    'statsd_host': '127.0.0.1',
    'statsd_port': 8125
}

options['statsd_host'] = os.getenv('DOGSTATSD_HOST', '127.0.0.1')
options['statsd_port'] = os.getenv('DOGSTATSD_PORT', '8125')

start_time = time.time()
default_instance_id = hashlib.md5(str(time.time()).encode('utf-8')).hexdigest()
app_instance_id = os.getenv('APP_INSTANCE_ID', default_instance_id)

tags = [
    "environment:local",
    "app_instance_id:%s" % str(app_instance_id)[0:8]
]


print(options)

initialize(**options)

while(1):
    curr_time = time.time()
    diff_time = curr_time - start_time
    # sin() with 10min period
    y = 10.0 * math.sin(6.28 * diff_time / 600.0)

    statsd.increment('custom_metrics.app_dogstatsd.counter', 1, tags=tags)
    statsd.gauge('custom_metrics.app_dogstatsd.gauge', y, tags=tags)

    print('%12.6f  %12.6f' % (diff_time, y))
    time.sleep(10)
