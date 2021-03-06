import time
import jenkins


def connect_jenkins_api():
    server = jenkins.Jenkins('http://localhost:8080', 
            username='oladimillion', password='oladimillion')

    return server


def get_jobs_info():

    job_list = []

    server = connect_jenkins_api()
    jobs = server.get_jobs()

    for job_name in jobs:

        job_info = server.get_job_info(job_name['name']);

        name = job_info['name']
        url = job_info['url']
        health_report = job_info['healthReport']

        builds = job_info['builds']
        lastBuild = job_info['lastBuild']
        lastSuccessfulBuild = job_info['lastSuccessfulBuild']
        lastUnsuccessfulBuild  = job_info['lastUnsuccessfulBuild']
        lastStableBuild = job_info['lastStableBuild']

        last_build_number = None
        last_successful_build_number = None
        last_unsuccessful_build_number = None
        last_stable_build_number = None

        health_description = None
        health_score = None
        health_color = None

        checked_at = None

        if len(health_report):

            health_description = health_report[0]['description']
            health_score = health_report[0]['score']
            health_color = job_info['color']

            if lastBuild:
                last_build_number = lastBuild['number']
            if lastSuccessfulBuild:
                last_successful_build_number = lastSuccessfulBuild['number']
            if lastUnsuccessfulBuild:
                last_unsuccessful_build_number = lastUnsuccessfulBuild['number']
            if lastStableBuild:
                last_stable_build_number = lastStableBuild['number']


        name = str(name)
        url = str(url)

        last_build_number = str(last_build_number)
        last_successful_build_number = str(last_successful_build_number)
        last_unsuccessful_build_number = str(last_unsuccessful_build_number)
        last_stable_build_number = str(last_stable_build_number)

        health_color = str(health_color)
        health_description = str(health_description)
        health_score = str(health_score)

        checked_at = time.ctime()

        job_list.append((name, url, last_build_number, last_successful_build_number,
                        last_unsuccessful_build_number, last_stable_build_number,
                        health_color, health_description, health_score, checked_at))

    return job_list

