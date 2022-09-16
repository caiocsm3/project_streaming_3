# project_streaming_3
Deprecation Notice
This is used for building images for version 5.3.x or lower, and should not be used for adding new images.

For the 5.4.0 release and greater the images have been migrated to the following repositories:

common-docker
control-center-images
kafkacat-images
kafka-images
kafka-mqtt-images
kafka-replicator-images
kafka-rest-images
kafka-streams-examples
ksql-images
schema-registry-images
Docker Images for Confluent Plaform
Docker images for deploying and running the Confluent Platform. The images are currently available on DockerHub. They are currently only available for Confluent Platform 3.0.1 and after.

Full documentation for using the images can be found here.

Networking and Kafka on Docker
When running Kafka under Docker, you need to pay careful attention to your configuration of hosts and ports to enable components both internal and external to the docker network to communicate. You can see more details in this article.

Known issues on Mac/Windows
For more details on known issues when running these images on Mac/Windows, you can refer to the following links:

Hostname Issue
Host networking on Docker for Mac: link 1, link 2, link 3
Building
Use make to perform various builds and tests

Docker Utils
See Docker Utils

Contribute
Start by reading our guidelines on contributing to this project found here.

Source Code: https://github.com/confluentinc/cp-docker-images
Issue Tracker: https://github.com/confluentinc/cp-docker-images/issues
License
The project is licensed under the Apache 2 license. For more information on the licenses for each of the individual Confluent Platform components packaged in the images, please refer to the respective Confluent Platform documentation for each component.
