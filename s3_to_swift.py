#!/usr/bin/env/python
#
# A python script to transfer files from S3 to RAX CF.
#
# Tested and working
#
# Requires boto and pyrax
#
# Written by: Joe Engel
#

import os
import boto
import pyrax
import pyrax.exceptions as exc
import pyrax.utils as utils

# S3 Creds
S3_ACCESS_KEY = ''
S3_SECRET_KEY = ''

# Buckets and Containers
S3_BUCKET = ''
RAX_CONTAINER = ''

# RAX container connection
pyrax.set_setting("identity_type", "rackspace")
creds_file = os.path.expanduser('~/.rackspace_cloud_credentials')
pyrax.set_credential_file(creds_file)
cf = pyrax.cloudfiles
cont = cf.get_container(RAX_CONTAINER)
print "Retrieved RAX container: %s" % RAX_CONTAINER

# S3 bucket connection
s3 = boto.connect_s3(S3_ACCESS_KEY,S3_SECRET_KEY)

# Retrieve S3 bucket
bucket = s3.get_bucket(S3_BUCKET)
print "Retrieved S3 Bucket: %s" % S3_BUCKET

# Get contents of S3 bucket
for key in bucket.list():
    try:
        # Download key from the S3 bucket
        to_upload = key.get_contents_to_filename(key.name)
        # Store this then, to CF and confirm
        obj = cf.store_object(cont, key.name, key.name)
        print "Stored object: %s as %s" % (obj, key.name)
        os.remove(key.name)
    except Exception as e:
        print e
        print "%s failed to download!" % key.name
