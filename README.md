Kinesis IO Streams
==================

This repository contains a [humilis][humilis] layer that deploys
a pair of [Kinesis streams][kinesis] that act as input/output buffers for
a Lambda pipeline. It also deploys a [Kinesis Firehose][firehose] delivery
stream to send all output events to S3 and Redshift. Note that this repository
is not intended to stand on its own but to be part of a larger humilis
_environment_. See [humilis][humilis] documentation for more information.

[firehose]: http://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html
[kinesis]: https://aws.amazon.com/documentation/kinesis/
[humilis]: https://github.com/InnovativeTravel/humilis


## Requirements

You need to install [humilis][humilis] and configure a local profile:

```
humilis configure --local
```

The command above will create a `.humilis.ini` file that you can keep with the
rest of your code. This repository contains one such file with values that make
sense for people working at Innovative Travel.


## Development

Assuming you have [virtualenv][venv] installed:

[venv]: https://virtualenv.readthedocs.org/en/latest/

```
make develop
```


## Testing

To run the local test suite:

```
make test
```


## Development

Assuming you have [virtualenv][virtualenv] installed:

[virtualenv]: https://virtualenv.readthedocs.org/en/latest/

```
make develop
```


## Testing

To run the test suite (requires deployment):

```
make test
```

This layer does not contain any logic beyond the deployment of several AWS 
resources. Therefore there is no local test suite and the tests simply assess 
that the deployment work as expected. This means that you cannot run the test 
suite without deploying first. Keep reading for deployment instructions.


## Deployment

```
make create 
```

This will deploy to a _humilis_ stage called `TEST`. You can decide
to deploy on a different stage (e.g. `DEV`) by running:

```
make STAGE=DEV create
```

Note however that the test suite expects a deployment in a `TEST` stage.

Remember to delete the deployment when you are done with testing:

```
make delete
```

Alternatively you can just run `make clean` to delete the deployment and the
development virtualenv.

To deploy updates to an existing deployment run:

```
make update
```


## More information

See [humilis][humilis] documentation.


## Who do I ask?

Ask [German](mailto:german@innovativetravel.eu)
