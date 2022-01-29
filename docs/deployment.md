# How does deployment work?

This app makes static pages for the public, but provide the admin UI at a different, sererless endpoint.

### How do we serve the built static version of the site?

It's simple enough to serve to S3 compatible storage. But once you have done that, you need to then be able to serve the content over SSL at more accessible domain.

You can access the site by default at the link below - note how it is *not* HTTPS

To make it HTTPS, you would put it behind Cloudflare, or some option that serves SSL connections.

If you use Cloudflare, then it will need to be able access the S3 objects, so it can cache them.

https://stackoverflow.com/questions/47966890/how-to-serve-files-from-s3-via-cloudflare

## How to do this

One option is to set up a CNAME, then rely on a service like cloudflare for caching and serving the static files.

https://stackoverflow.com/questions/47966890/how-to-serve-files-from-s3-via-cloudflare

## Getting this into object storage

First of all, create a bucket:

```
aws s3 mb s3://BUCKET_NAME_WITH_TLD
```

Next, set the bucket to act like a website. The config we'd store in a json file, telling the bucket what to do with index and 404 requests:

```
aws s3api put-bucket-website --bucket BUCKET_NAME_WITH_TLD --website-configuration file://LOCAL/PATH/TO/BUCKET_WEBSITE.json
```

You can now use the django bakery commands to publish content. This will take the local contents and upload it to the bucket:

```bash
# build local files
./manage.py publish

# sync with the bucket
./manage.py publish
```

### Seeing the published static files.

This is a gotcha - if you are using object storage from scaleway, then the website and bucket urls are different.

You can access individual files at in the bucket at the region you have uploaded to:

https://BUCKET_WITH_TLD.s3.pl-waw.scw.cloud/path/to/file.html

But you won't be able to visit the link below - you'll get an error

https://BUCKET_WITH_TLD.s3.pl-waw.scw.cloud/

You will need to make sure that `website`  is in the domain:

https://BUCKET_WITH_TLD.s3-website.pl-waw.scw.cloud/

Below is a concrete example:

```bash
# does not work
http://blog.chrisadams.me.uk.s3.pl-waw.scw.cloud

# does work
http://blog.chrisadams.me.uk.s3-website.pl-waw.scw.cloud
```

