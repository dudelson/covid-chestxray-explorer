# It turns out that cloudinary automatically appends 6 random letters to the
# end of the filename when you upload a file (so e.g. "test.jpg" would be
# uploaded as "test_gqktwm.jpg"). This meant that the filenames in the database
# didn't match the filenames on cloudinary, which broke all my images. So I
# opted to fix it on the cloudinary side by writing this script, which uses the
# cloudinary API to bulk rename the image files used by the app, removing the 6
# letters appended by cloudinary.

# To run the script, the API key and API secret have to be passed in as envvars.
# If you want to see what the script will do before actually performing any
# operations on cloudinary, also pass in the envvar DRY_RUN=1.

import os
import cloudinary
import cloudinary.uploader as cloudup
import cloudinary.api as cloudapi

cloudinary.config(
    cloud_name = "dmcs4ohin",
    api_key = os.environ['CLOUDINARY_API_KEY'],
    api_secret = os.environ['CLOUDINARY_API_SECRET']
)


def parse_name(name):
    ''' Accepts the full public ID of a cloudinary resource and returns a
    version with the trailing 6 random letters removed. '''
    prefix, filename = os.path.split(name)
    filename_parts = filename.split('_')
    new_filename = '_'.join(filename_parts[:-1])
    # simple sanity check
    if len(new_filename) + 7 != len(filename):
        print('WARNING: New filename "{}" failed sanity check! (Old filename: "{}")'
              .format(new_filename, filename))
    return name, os.path.join(prefix, new_filename)


if __name__ == '__main__':
    next_cursor = None
    while True:
        response = cloudapi.resources(type="upload",
                                      prefix="covid-chestxray-dataset/",
                                      next_cursor=next_cursor,
                                      max_results=100)
        if 'next_cursor' in response and response['next_cursor'] is not None:
            next_cursor = response['next_cursor']
        pub_ids = [r['public_id'] for r in response['resources']]
        for pub_id in pub_ids:
            old_id, new_id = parse_name(pub_id)
            if 'DRY_RUN' in os.environ:
                print('Would rename "{}" to "{}"'.format(old_id, new_id))
                continue
            result = cloudup.rename(old_id, new_id)
            if result['public_id'] != new_id:
                print('ERROR: "{}" not successfully renamed to "{}"'
                      .format(old_id, new_id))
                # don't break, bc then we'd have some images renamed and some not,
                # which would be a mess. it's highly likely that if this error
                # occurs, it will occur on all images at once.
            else:
                print('Successfully renamed "{}" to "{}"'.format(old_id, new_id))
        print('Renamed {} files\n'.format(len(response['resources'])))
        if len(response['resources']) < 100:
            # this was the last batch, quit
            break
