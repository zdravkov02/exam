# Fun Facts
A simple project to be used for the final practice exam for the [**DevOps - Containerization, CI/CD & Monitoring (2022.02)**](https://softuni.bg/trainings/3670/devops-containerization-ci-cd-monitoring-february-2022) and [**DevOps - Containerization, CI/CD & Monitoring (2022.09)**](https://softuni.bg/trainings/3888/devops-containerization-ci-cd-monitoring-september-2022) courses at **SoftUni**. 

It is a set of three Docker containers, each with a dedicated role. Together they form a simple web application. 

The general setup looks like:

![general setup](setup.png)

If the images have the following names (***img-client***, ***img-storage***, and ***img-generator***), then the correct commands to run the application in ***test mode*** would be:

```bash
# Run the client component
docker container run -d --name con-client --net fun-facts -p 8080:5000 img-client

# Run the storage component
docker container run -d --name con-storage --net fun-facts -e MYSQL_ROOT_PASSWORD='ExamPa$$w0rd' img-storage

# Run the generator component
docker container run -d --name con-generator --net fun-facts img-generator

```

If all is set up corectly then the result would be something like this:

![sample result](result.png)

For successful completion of the challenge, you will have to create a pipeline that implements the following steps:
 - build the images;
 - run the containers in ***test mode*** (client published on port 8080)
 - test that the client is accessible;
 - publish the images to a registry (for example, Docker Hub);
 - run the application from the published images in ***production mode*** (client published on port 80);
 - ensure the containers are part of the same network.

Please note that:
 - each container should be named after the following rule - ***con-role***, where ***role*** is either ***client***, ***storage***, or ***generator***. For example, ***con-client***;
 - database password is expected to be **ExamPa$$w0rd**. It can be changed via environment variables (***DB_PASS*** for the ***client*** and ***generator*** and ***MYSQL_ROOT_PASSWORD*** for the ***storage***);
 - web content is delivered by the **client** on port **5000**. It may be redirected to an arbitrary port on the host, for example on port 80 or port 8080;
 - there is no particular order to follow when starting the containers.

*More specific details could be found in the downloadable **Practice Exam** document available in the **Regular Exam** section of the course.*

*The solution for this is in the exam.rar archive, automated deployment*
Modified on 2022-11-13 10:03:58
