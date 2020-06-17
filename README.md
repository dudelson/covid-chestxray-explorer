# COVID-19 Chest X-Ray Image Dataset Explorer

This webapp allows you to explore the images and associated metadata from the
[COVID-19 chest xray image open
dataset](https://github.com/ieee8023/covid-chestxray-dataset). I built it as a
way of teaching myself fullstack web development using [Vue](https://vuejs.org/)
and [Django](https://www.djangoproject.com/). There is a [live instance](https://covid-chestxray-explorer.vercel.app/) for people to
play around with.

*Note*: Upon accessing the live instance, you may see no images displayed for as
long as 15 seconds after page load. This has to do with limitations of Heroku's
free tier.

## Functionality

The app displays a paginated gallery of all of the images contained in the
dataset. Clicking on an image will display a detail view where a larger version
of the selected image is displayed alongside detailed metadata for that image.

## Deployment

The app is setup to be deployed in two parts: the backend to [heroku](https://www.heroku.com/), and the
frontend to [vercel](https://vercel.com/). In the case of the frontend, the repo
currently contains no vercel-specific configuration, so in principle the
frontend could be deployed to any frontend deployment platform, *provided* that
the platform supports ignoring the python configuration (or simply detects the
node config first). This is currently an issue on netlify, for example.

## Future Directions

While this app is primarily for demonstration purposes, there are hypothetically
a lot of ways in which it could be enhanced. The most useful unimplemented
feature would be a set of filters, allowing the user to selected a subset of
images that share one or more metadata fields. The queries could take advantage
of the client-side routing that's already in place, allowing them to be
bookmarked and shared with others. If user accounts were added, this could
potentially evolve into a diagnostic tool, where users are able to upload their
own xray photos, and a ML model on the backend tries to provide a diagnosis of
the image. (However in principle this would perhaps be unwise, because as the
dataset README states, one should not implement a diagnostic ML model without a
clinical trial, and I am not a doctor.)
