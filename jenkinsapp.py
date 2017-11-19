import jenkins

server = jenkins.Jenkins('http://localhost:8080', username='oladimillion', password='oladimillion')
user = server.get_whoami()
jobs = server.get_jobs()
print(user["fullName"]);
print()
print(jobs);

